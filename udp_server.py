import socket, struct

# Setup socket object
s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_UDP)
s.bind(("127.0.0.1", 9123))
s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
trash_port = 50463
base_port = 47000
stego_message = bytearray()

while (True):
    data = s.recvfrom(65565)
    packet = data[0]
    address = data[1]

    header = struct.unpack('!BBHHHBBH4s4s', packet[14:34])
    msg = packet[28:]
    port = header[4]

    if port == trash_port:
        continue

    if port == base_port:
        if len(stego_message):
            print(stego_message)
        stego_message = bytearray()
        continue

    stego_message.append(port - base_port)
