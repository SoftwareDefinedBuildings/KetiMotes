# TinyOS Installation

* TODO: clean up directory structure and rename files appropriately (rename RH/CO2 etc -- fix fanlings errors)
* TODO: use https://github.com/SoftwareDefinedBuildings/KMEG/blob/master/keti_work/Mjolnir/Sensor/100THSensor/THSensorC.nc for TH sensors
* TODO: supervisor scripts for KETI smap deployment
* TODO: instructions for KETI smap

## Configuring environment

To facilitate creating a build/flash environment for KETImotes and tiny-os, we have instructions for Ubuntu

### Native Ubuntu

Run the `install.sh` script.  Copy it onto your Ubuntu installation
(12.04 or later should work), change the `$HOME` variable on line 3 to where
you want the base installation to be located, and run

```
sudo su root
. install.sh
```

and the process will take care of itself.

```
sudo su root # should be passwordless
cd KMEG/tinyos-main
export TOSROOT=`pwd`
export TOSDIR="$TOSROOT/tos"
export MAKERULES="$TOSROOT/support/make/Makerules"
export CLASSPATH="$TOSROOT/support/sdk/java/tinyos.jar:."
export PYTHONPATH="$TOSROOT/support/sdk/python:$PYTHONPATH"
export PATH="$TOSROOT/support/sdk/c:$PATH"
export PATH="$TOSROOT/tools/platforms/msp430/motelist:$PATH"
export PATH="$TOSROOT/tools/platforms/msp430/pybsl:$PATH"
chmod +x "$TOSROOT/tools/platforms/msp430/motelist/motelist"
chmod +x "$TOSROOT/tools/platforms/msp430/pybsl/tos-bsl"
```

## Building Apps

Now, go to the apps folder for the KETI-motes. For the temperature/humidity/illumination/co2 sensors, this is `Temp_RH_CO2_Sensor`.

```
cd $TOSROOT/apps/Temp_RH_CO2_Sensor
make tmote blip
```

This should compile the application for the tmote/telosb architecture, and you can find the resulting app
in the `build/telosb` folder relative to your current path.

To install the app on a mote (e.g. 'flash the mote'), first do

```
ls /dev/ttyUSB*
```

which should PROBABLY give you `/dev/ttyUSB0`, which should be your programmer unit. Make this world writeable:

```
sudo chmod 777 /dev/ttyUSB0
```

Now, unplug the board from the KETImote and plug it into the programmer. Inside the `Temp_RH_CO2_Sensor` folder,
run

```
make tmote reinstall,<node num>
```

`<node num>` should be unique for this mote and is just an arbitrary integer (2 or greater. 1 is reserved). Write this down and label the
mote with it so that you know which mote is which ID. The above command flashed the mote, and if all was
successful, you should see something like

```
Mass Erase...
Transmit default password...
... more stuff here
Reset device...
etc...
```

### Types of Motes

There are 3 types of motes (which should be labeled on the cover of the mote):

* TH (Temperature + Relative Humidity)
* CO2 (Carbon Dioxide)
* PIR (Passive infrared -- occupancy)

To flash a TH mote, use the `Temp_RH_CO2_Sensor` application, and make sure the Makefile contains these lines:

```
CFLAGS += -DTH
CFLAGS += -DRH
CFLAGS += -DIll
#CFLAGS += -DCO2
#CFLAGS += -DPIR
```

and then run `make tmote blip` and `make tmote reinstall,<mote id>` etc.

---

To flash a CO2 mote, use the `Temp_RH_CO2_Sensor` application, and make sure to edit the Makefile so that it reads:

```
#CFLAGS += -DTH
#CFLAGS += -DRH
#CFLAGS += -DIll
CFLAGS += -DCO2
#CFLAGS += -DPIR
```

(then run `make tmote blip` etc)

---

To flash a PIR mote, use the `PIR_sensor` application and make/install as per usual. No edits to the Makefile.



## Talking to Motes

Get a Telos mote or attach one of the KETI boards to programmer and plug it in to your computer (if you are using Virtualbox, you will have
to do the trick where you halt the VM, add the USB device, and then restart the VM.

We are going to flash our mote with the ability to act as a router between the motes and our computer. Go to the `PPPRouter` application:

```
cd $TOSROOT/apps/PPPRouter
make tmote blip
```

Unplug any other programmers from your computer, and then to install, run

```
make tmote reinstall,1
```

Keep the mote plugged in, but in a separate window, run (as root)

```
pppd debug passive noauth nodetach 115200 /dev/ttyUSB0 nocrtscts nocdtrcts lcp-echo-interval 0 noccp noip ipv6 ::23,::24
```

This will not exit, but if it is successful, you should see some output like

```
[bunch of stuff here]
Script /etc/ppp/ipv6-up started (pid 3033)
Script /etc/ppp/ipv6-up finished (pid 3033), status = 0x0
```

Then in another window, run

```
sudo ifconfig ppp0 add fec0::100/64
```

which should exit cleanly. When you run `ifconfig`, you should see `ppp0` as an interface now.

Eventually, I plan on having some cleaner code to help read the output of these motes, but for now, go to `Temp_RH_CO2_Sensor/util` folder
and look at the `Listener.py` file. We will run the Listener script with an argument that tells it which USB device to read output from.
This USB device should be the `/dev/ttyUSB` where the Telos is.

```
cd $TOSROOT/apps/Temp_RH_CO2_Sensor/util
python Listener.py
```

You should see some output from this.

OR

if you want some nicer output, you should be able to do

```
cd $TOSROOT/apps/Temp_RH_CO2_Sensor/util
python readketi.py
```

which will use the type of mote to convert the returned values so you tell if it is reporting correct values

## KETI Mote sMAP source


