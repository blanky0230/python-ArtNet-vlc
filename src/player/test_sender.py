import socket, os
from dotenv import load_dotenv
config = load_dotenv(".env") 

UDP_IP=os.environ['UDP_IP']
UDP_PORT=os.environ['UDP_PORT']

MESSAGE = [ord(c) for c in "Art Net"] 
MESSAGE.extend([0x00 for i in range(100)])
        
MESSAGE[8] = 0x00
MESSAGE[9] = 0x50
MESSAGE[14] = 0x01
MESSAGE[15] = 0x00
MESSAGE[16] = 0x64
MESSAGE[99] = 0x01
MESSAGE[100] = 0x01


print("UDP target IP: %s" % UDP_IP)
print("UDP target port: %s" % UDP_PORT)
print("message: %s" % MESSAGE)

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.sendto(bytes(MESSAGE), (UDP_IP, int(UDP_PORT)))