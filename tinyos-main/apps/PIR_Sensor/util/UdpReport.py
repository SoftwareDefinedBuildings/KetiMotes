#
# This class is automatically generated by mig. DO NOT EDIT THIS FILE.
# This class implements a Python interface to the 'UdpReport'
# message type.
#

import tinyos.message.Message

# The default size of this message type in bytes.
DEFAULT_MESSAGE_SIZE = 21

# The Active Message type associated with this message.
AM_TYPE = -1

class UdpReport(tinyos.message.Message.Message):
    # Create a new UdpReport of size 21.
    def __init__(self, data="", addr=None, gid=None, base_offset=0, data_length=21):
        tinyos.message.Message.Message.__init__(self, data, addr, gid, base_offset, data_length)
        self.amTypeSet(AM_TYPE)
    
    # Get AM_TYPE
    def get_amType(cls):
        return AM_TYPE
    
    get_amType = classmethod(get_amType)
    
    #
    # Return a String representation of this message. Includes the
    # message type name and the non-indexed field values.
    #
    def __str__(self):
        s = "Message <UdpReport> \n"
        try:
            s += "  [seqno=0x%x]\n" % (self.get_seqno())
        except:
            pass
        try:
            s += "  [sender=0x%x]\n" % (self.get_sender())
        except:
            pass
        try:
            s += "  [interval=0x%x]\n" % (self.get_interval())
        except:
            pass
        try:
            s += "  [ip.sent=0x%x]\n" % (self.get_ip_sent())
        except:
            pass
        try:
            s += "  [ip.forwarded=0x%x]\n" % (self.get_ip_forwarded())
        except:
            pass
        try:
            s += "  [ip.rx_drop=0x%x]\n" % (self.get_ip_rx_drop())
        except:
            pass
        try:
            s += "  [ip.tx_drop=0x%x]\n" % (self.get_ip_tx_drop())
        except:
            pass
        try:
            s += "  [ip.fw_drop=0x%x]\n" % (self.get_ip_fw_drop())
        except:
            pass
        try:
            s += "  [ip.rx_total=0x%x]\n" % (self.get_ip_rx_total())
        except:
            pass
        try:
            s += "  [ip.encfail=0x%x]\n" % (self.get_ip_encfail())
        except:
            pass
        try:
            s += "  [udp.sent=0x%x]\n" % (self.get_udp_sent())
        except:
            pass
        try:
            s += "  [udp.rcvd=0x%x]\n" % (self.get_udp_rcvd())
        except:
            pass
        try:
            s += "  [udp.cksum=0x%x]\n" % (self.get_udp_cksum())
        except:
            pass
        try:
            s += "  [readings=0x%s]\n" % (self.get_readings())
        except:
            pass
        return s

    # Message-type-specific access methods appear below.

    #
    # Accessor methods for field: readings
    #   Field type: int
    #   Offset (bits): 168
    #   Size (bits): 16
    #

    def get_readings(self):
        return self.getUIntElement(self.offsetBits_readings(), 16, 1)

    def offsetBits_readings(self):
        return 168


    #
    # Accessor methods for field: seqno
    #   Field type: int
    #   Offset (bits): 0
    #   Size (bits): 16
    #

    #
    # Return whether the field 'seqno' is signed (False).
    #
    def isSigned_seqno(self):
        return False
    
    #
    # Return whether the field 'seqno' is an array (False).
    #
    def isArray_seqno(self):
        return False
    
    #
    # Return the offset (in bytes) of the field 'seqno'
    #
    def offset_seqno(self):
        return (0 / 8)
    
    #
    # Return the offset (in bits) of the field 'seqno'
    #
    def offsetBits_seqno(self):
        return 0
    
    #
    # Return the value (as a int) of the field 'seqno'
    #
    def get_seqno(self):
        return self.getUIntElement(self.offsetBits_seqno(), 16, 1)
    
    #
    # Set the value of the field 'seqno'
    #
    def set_seqno(self, value):
        self.setUIntElement(self.offsetBits_seqno(), 16, value, 1)
    
    #
    # Return the size, in bytes, of the field 'seqno'
    #
    def size_seqno(self):
        return (16 / 8)
    
    #
    # Return the size, in bits, of the field 'seqno'
    #
    def sizeBits_seqno(self):
        return 16
    
    #
    # Accessor methods for field: sender
    #   Field type: int
    #   Offset (bits): 16
    #   Size (bits): 16
    #

    #
    # Return whether the field 'sender' is signed (False).
    #
    def isSigned_sender(self):
        return False
    
    #
    # Return whether the field 'sender' is an array (False).
    #
    def isArray_sender(self):
        return False
    
    #
    # Return the offset (in bytes) of the field 'sender'
    #
    def offset_sender(self):
        return (16 / 8)
    
    #
    # Return the offset (in bits) of the field 'sender'
    #
    def offsetBits_sender(self):
        return 16
    
    #
    # Return the value (as a int) of the field 'sender'
    #
    def get_sender(self):
        return self.getUIntElement(self.offsetBits_sender(), 16, 1)
    
    #
    # Set the value of the field 'sender'
    #
    def set_sender(self, value):
        self.setUIntElement(self.offsetBits_sender(), 16, value, 1)
    
    #
    # Return the size, in bytes, of the field 'sender'
    #
    def size_sender(self):
        return (16 / 8)
    
    #
    # Return the size, in bits, of the field 'sender'
    #
    def sizeBits_sender(self):
        return 16
    
    #
    # Accessor methods for field: interval
    #   Field type: int
    #   Offset (bits): 32
    #   Size (bits): 16
    #

    #
    # Return whether the field 'interval' is signed (False).
    #
    def isSigned_interval(self):
        return False
    
    #
    # Return whether the field 'interval' is an array (False).
    #
    def isArray_interval(self):
        return False
    
    #
    # Return the offset (in bytes) of the field 'interval'
    #
    def offset_interval(self):
        return (32 / 8)
    
    #
    # Return the offset (in bits) of the field 'interval'
    #
    def offsetBits_interval(self):
        return 32
    
    #
    # Return the value (as a int) of the field 'interval'
    #
    def get_interval(self):
        return self.getUIntElement(self.offsetBits_interval(), 16, 1)
    
    #
    # Set the value of the field 'interval'
    #
    def set_interval(self, value):
        self.setUIntElement(self.offsetBits_interval(), 16, value, 1)
    
    #
    # Return the size, in bytes, of the field 'interval'
    #
    def size_interval(self):
        return (16 / 8)
    
    #
    # Return the size, in bits, of the field 'interval'
    #
    def sizeBits_interval(self):
        return 16
    
    #
    # Accessor methods for field: ip.sent
    #   Field type: int
    #   Offset (bits): 48
    #   Size (bits): 16
    #

    #
    # Return whether the field 'ip.sent' is signed (False).
    #
    def isSigned_ip_sent(self):
        return False
    
    #
    # Return whether the field 'ip.sent' is an array (False).
    #
    def isArray_ip_sent(self):
        return False
    
    #
    # Return the offset (in bytes) of the field 'ip.sent'
    #
    def offset_ip_sent(self):
        return (48 / 8)
    
    #
    # Return the offset (in bits) of the field 'ip.sent'
    #
    def offsetBits_ip_sent(self):
        return 48
    
    #
    # Return the value (as a int) of the field 'ip.sent'
    #
    def get_ip_sent(self):
        return self.getUIntElement(self.offsetBits_ip_sent(), 16, 1)
    
    #
    # Set the value of the field 'ip.sent'
    #
    def set_ip_sent(self, value):
        self.setUIntElement(self.offsetBits_ip_sent(), 16, value, 1)
    
    #
    # Return the size, in bytes, of the field 'ip.sent'
    #
    def size_ip_sent(self):
        return (16 / 8)
    
    #
    # Return the size, in bits, of the field 'ip.sent'
    #
    def sizeBits_ip_sent(self):
        return 16
    
    #
    # Accessor methods for field: ip.forwarded
    #   Field type: int
    #   Offset (bits): 64
    #   Size (bits): 16
    #

    #
    # Return whether the field 'ip.forwarded' is signed (False).
    #
    def isSigned_ip_forwarded(self):
        return False
    
    #
    # Return whether the field 'ip.forwarded' is an array (False).
    #
    def isArray_ip_forwarded(self):
        return False
    
    #
    # Return the offset (in bytes) of the field 'ip.forwarded'
    #
    def offset_ip_forwarded(self):
        return (64 / 8)
    
    #
    # Return the offset (in bits) of the field 'ip.forwarded'
    #
    def offsetBits_ip_forwarded(self):
        return 64
    
    #
    # Return the value (as a int) of the field 'ip.forwarded'
    #
    def get_ip_forwarded(self):
        return self.getUIntElement(self.offsetBits_ip_forwarded(), 16, 1)
    
    #
    # Set the value of the field 'ip.forwarded'
    #
    def set_ip_forwarded(self, value):
        self.setUIntElement(self.offsetBits_ip_forwarded(), 16, value, 1)
    
    #
    # Return the size, in bytes, of the field 'ip.forwarded'
    #
    def size_ip_forwarded(self):
        return (16 / 8)
    
    #
    # Return the size, in bits, of the field 'ip.forwarded'
    #
    def sizeBits_ip_forwarded(self):
        return 16
    
    #
    # Accessor methods for field: ip.rx_drop
    #   Field type: short
    #   Offset (bits): 80
    #   Size (bits): 8
    #

    #
    # Return whether the field 'ip.rx_drop' is signed (False).
    #
    def isSigned_ip_rx_drop(self):
        return False
    
    #
    # Return whether the field 'ip.rx_drop' is an array (False).
    #
    def isArray_ip_rx_drop(self):
        return False
    
    #
    # Return the offset (in bytes) of the field 'ip.rx_drop'
    #
    def offset_ip_rx_drop(self):
        return (80 / 8)
    
    #
    # Return the offset (in bits) of the field 'ip.rx_drop'
    #
    def offsetBits_ip_rx_drop(self):
        return 80
    
    #
    # Return the value (as a short) of the field 'ip.rx_drop'
    #
    def get_ip_rx_drop(self):
        return self.getUIntElement(self.offsetBits_ip_rx_drop(), 8, 1)
    
    #
    # Set the value of the field 'ip.rx_drop'
    #
    def set_ip_rx_drop(self, value):
        self.setUIntElement(self.offsetBits_ip_rx_drop(), 8, value, 1)
    
    #
    # Return the size, in bytes, of the field 'ip.rx_drop'
    #
    def size_ip_rx_drop(self):
        return (8 / 8)
    
    #
    # Return the size, in bits, of the field 'ip.rx_drop'
    #
    def sizeBits_ip_rx_drop(self):
        return 8
    
    #
    # Accessor methods for field: ip.tx_drop
    #   Field type: short
    #   Offset (bits): 88
    #   Size (bits): 8
    #

    #
    # Return whether the field 'ip.tx_drop' is signed (False).
    #
    def isSigned_ip_tx_drop(self):
        return False
    
    #
    # Return whether the field 'ip.tx_drop' is an array (False).
    #
    def isArray_ip_tx_drop(self):
        return False
    
    #
    # Return the offset (in bytes) of the field 'ip.tx_drop'
    #
    def offset_ip_tx_drop(self):
        return (88 / 8)
    
    #
    # Return the offset (in bits) of the field 'ip.tx_drop'
    #
    def offsetBits_ip_tx_drop(self):
        return 88
    
    #
    # Return the value (as a short) of the field 'ip.tx_drop'
    #
    def get_ip_tx_drop(self):
        return self.getUIntElement(self.offsetBits_ip_tx_drop(), 8, 1)
    
    #
    # Set the value of the field 'ip.tx_drop'
    #
    def set_ip_tx_drop(self, value):
        self.setUIntElement(self.offsetBits_ip_tx_drop(), 8, value, 1)
    
    #
    # Return the size, in bytes, of the field 'ip.tx_drop'
    #
    def size_ip_tx_drop(self):
        return (8 / 8)
    
    #
    # Return the size, in bits, of the field 'ip.tx_drop'
    #
    def sizeBits_ip_tx_drop(self):
        return 8
    
    #
    # Accessor methods for field: ip.fw_drop
    #   Field type: short
    #   Offset (bits): 96
    #   Size (bits): 8
    #

    #
    # Return whether the field 'ip.fw_drop' is signed (False).
    #
    def isSigned_ip_fw_drop(self):
        return False
    
    #
    # Return whether the field 'ip.fw_drop' is an array (False).
    #
    def isArray_ip_fw_drop(self):
        return False
    
    #
    # Return the offset (in bytes) of the field 'ip.fw_drop'
    #
    def offset_ip_fw_drop(self):
        return (96 / 8)
    
    #
    # Return the offset (in bits) of the field 'ip.fw_drop'
    #
    def offsetBits_ip_fw_drop(self):
        return 96
    
    #
    # Return the value (as a short) of the field 'ip.fw_drop'
    #
    def get_ip_fw_drop(self):
        return self.getUIntElement(self.offsetBits_ip_fw_drop(), 8, 1)
    
    #
    # Set the value of the field 'ip.fw_drop'
    #
    def set_ip_fw_drop(self, value):
        self.setUIntElement(self.offsetBits_ip_fw_drop(), 8, value, 1)
    
    #
    # Return the size, in bytes, of the field 'ip.fw_drop'
    #
    def size_ip_fw_drop(self):
        return (8 / 8)
    
    #
    # Return the size, in bits, of the field 'ip.fw_drop'
    #
    def sizeBits_ip_fw_drop(self):
        return 8
    
    #
    # Accessor methods for field: ip.rx_total
    #   Field type: short
    #   Offset (bits): 104
    #   Size (bits): 8
    #

    #
    # Return whether the field 'ip.rx_total' is signed (False).
    #
    def isSigned_ip_rx_total(self):
        return False
    
    #
    # Return whether the field 'ip.rx_total' is an array (False).
    #
    def isArray_ip_rx_total(self):
        return False
    
    #
    # Return the offset (in bytes) of the field 'ip.rx_total'
    #
    def offset_ip_rx_total(self):
        return (104 / 8)
    
    #
    # Return the offset (in bits) of the field 'ip.rx_total'
    #
    def offsetBits_ip_rx_total(self):
        return 104
    
    #
    # Return the value (as a short) of the field 'ip.rx_total'
    #
    def get_ip_rx_total(self):
        return self.getUIntElement(self.offsetBits_ip_rx_total(), 8, 1)
    
    #
    # Set the value of the field 'ip.rx_total'
    #
    def set_ip_rx_total(self, value):
        self.setUIntElement(self.offsetBits_ip_rx_total(), 8, value, 1)
    
    #
    # Return the size, in bytes, of the field 'ip.rx_total'
    #
    def size_ip_rx_total(self):
        return (8 / 8)
    
    #
    # Return the size, in bits, of the field 'ip.rx_total'
    #
    def sizeBits_ip_rx_total(self):
        return 8
    
    #
    # Accessor methods for field: ip.encfail
    #   Field type: short
    #   Offset (bits): 112
    #   Size (bits): 8
    #

    #
    # Return whether the field 'ip.encfail' is signed (False).
    #
    def isSigned_ip_encfail(self):
        return False
    
    #
    # Return whether the field 'ip.encfail' is an array (False).
    #
    def isArray_ip_encfail(self):
        return False
    
    #
    # Return the offset (in bytes) of the field 'ip.encfail'
    #
    def offset_ip_encfail(self):
        return (112 / 8)
    
    #
    # Return the offset (in bits) of the field 'ip.encfail'
    #
    def offsetBits_ip_encfail(self):
        return 112
    
    #
    # Return the value (as a short) of the field 'ip.encfail'
    #
    def get_ip_encfail(self):
        return self.getUIntElement(self.offsetBits_ip_encfail(), 8, 1)
    
    #
    # Set the value of the field 'ip.encfail'
    #
    def set_ip_encfail(self, value):
        self.setUIntElement(self.offsetBits_ip_encfail(), 8, value, 1)
    
    #
    # Return the size, in bytes, of the field 'ip.encfail'
    #
    def size_ip_encfail(self):
        return (8 / 8)
    
    #
    # Return the size, in bits, of the field 'ip.encfail'
    #
    def sizeBits_ip_encfail(self):
        return 8
    
    #
    # Accessor methods for field: udp.sent
    #   Field type: int
    #   Offset (bits): 120
    #   Size (bits): 16
    #

    #
    # Return whether the field 'udp.sent' is signed (False).
    #
    def isSigned_udp_sent(self):
        return False
    
    #
    # Return whether the field 'udp.sent' is an array (False).
    #
    def isArray_udp_sent(self):
        return False
    
    #
    # Return the offset (in bytes) of the field 'udp.sent'
    #
    def offset_udp_sent(self):
        return (120 / 8)
    
    #
    # Return the offset (in bits) of the field 'udp.sent'
    #
    def offsetBits_udp_sent(self):
        return 120
    
    #
    # Return the value (as a int) of the field 'udp.sent'
    #
    def get_udp_sent(self):
        return self.getUIntElement(self.offsetBits_udp_sent(), 16, 1)
    
    #
    # Set the value of the field 'udp.sent'
    #
    def set_udp_sent(self, value):
        self.setUIntElement(self.offsetBits_udp_sent(), 16, value, 1)
    
    #
    # Return the size, in bytes, of the field 'udp.sent'
    #
    def size_udp_sent(self):
        return (16 / 8)
    
    #
    # Return the size, in bits, of the field 'udp.sent'
    #
    def sizeBits_udp_sent(self):
        return 16
    
    #
    # Accessor methods for field: udp.rcvd
    #   Field type: int
    #   Offset (bits): 136
    #   Size (bits): 16
    #

    #
    # Return whether the field 'udp.rcvd' is signed (False).
    #
    def isSigned_udp_rcvd(self):
        return False
    
    #
    # Return whether the field 'udp.rcvd' is an array (False).
    #
    def isArray_udp_rcvd(self):
        return False
    
    #
    # Return the offset (in bytes) of the field 'udp.rcvd'
    #
    def offset_udp_rcvd(self):
        return (136 / 8)
    
    #
    # Return the offset (in bits) of the field 'udp.rcvd'
    #
    def offsetBits_udp_rcvd(self):
        return 136
    
    #
    # Return the value (as a int) of the field 'udp.rcvd'
    #
    def get_udp_rcvd(self):
        return self.getUIntElement(self.offsetBits_udp_rcvd(), 16, 1)
    
    #
    # Set the value of the field 'udp.rcvd'
    #
    def set_udp_rcvd(self, value):
        self.setUIntElement(self.offsetBits_udp_rcvd(), 16, value, 1)
    
    #
    # Return the size, in bytes, of the field 'udp.rcvd'
    #
    def size_udp_rcvd(self):
        return (16 / 8)
    
    #
    # Return the size, in bits, of the field 'udp.rcvd'
    #
    def sizeBits_udp_rcvd(self):
        return 16
    
    #
    # Accessor methods for field: udp.cksum
    #   Field type: int
    #   Offset (bits): 152
    #   Size (bits): 16
    #

    #
    # Return whether the field 'udp.cksum' is signed (False).
    #
    def isSigned_udp_cksum(self):
        return False
    
    #
    # Return whether the field 'udp.cksum' is an array (False).
    #
    def isArray_udp_cksum(self):
        return False
    
    #
    # Return the offset (in bytes) of the field 'udp.cksum'
    #
    def offset_udp_cksum(self):
        return (152 / 8)
    
    #
    # Return the offset (in bits) of the field 'udp.cksum'
    #
    def offsetBits_udp_cksum(self):
        return 152
    
    #
    # Return the value (as a int) of the field 'udp.cksum'
    #
    def get_udp_cksum(self):
        return self.getUIntElement(self.offsetBits_udp_cksum(), 16, 1)
    
    #
    # Set the value of the field 'udp.cksum'
    #
    def set_udp_cksum(self, value):
        self.setUIntElement(self.offsetBits_udp_cksum(), 16, value, 1)
    
    #
    # Return the size, in bytes, of the field 'udp.cksum'
    #
    def size_udp_cksum(self):
        return (16 / 8)
    
    #
    # Return the size, in bits, of the field 'udp.cksum'
    #
    def sizeBits_udp_cksum(self):
        return 16
    
