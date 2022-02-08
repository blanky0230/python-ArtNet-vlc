import socket
import os
from dotenv import load_dotenv
from stupidArtnet import StupidArtnet
import random
config = load_dotenv(".env")

UDP_IP = os.environ['UDP_IP']
UDP_PORT = os.environ['UDP_PORT']
NET = int(os.environ['NET'])

MESSAGE = [ord(c) for c in "Art Net"]
MESSAGE.extend([0x00 for i in range(100)])

MESSAGE[8] = 0x00
MESSAGE[9] = 0x50
MESSAGE[14] = 0x00
MESSAGE[15] = 0x00
MESSAGE[16] = 0x64
MESSAGE[99] = 0x01
MESSAGE[100] = 0x01


# print("UDP target IP: %s" % UDP_IP)
# print("UDP target port: %s" % UDP_PORT)
# print("message: %s" % MESSAGE)

# sock = socket.socket(socket.AF_INET, # Internet
#                      socket.SOCK_DGRAM) # UDP
# sock.sendto(bytes(MESSAGE), (UDP_IP, int(UDP_PORT)))
stupid = StupidArtnet(universe=1, broadcast=False)
stupid.set_simplified(False)

# Start persistent thread

stupid.set_single_value(address=99, value=12312)
stupid.set_single_value(address=100, value=0)
stupid.set_single_value(address=101, value=1)
stupid.set_single_value(address=102, value=1)
stupid.set_single_value(address=103, value=100)
stupid.set_single_value(address=104, value=0)
stupid.show()
