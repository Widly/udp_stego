from socket import *
import struct
s = socket(AF_INET, SOCK_RAW, IPPROTO_UDP)

s_port_base = 47000
d_port = 9123   # arbitrary destination port
checksum = 0

def send_byte(byte_int):
    udp_header = struct.pack('!HHHH', s_port_base + byte_int, d_port, length, checksum)
    s.sendto(udp_header + str.encode(data), ('', 0))

stego_message = str.encode('STEGO')
data = 'string'
length = 8 + len(data)

send_byte(0) # start transmission

for stego_byte in bytearray(stego_message):
    send_byte(stego_byte)

send_byte(0) # stop transmission
