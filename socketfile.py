
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(s)
'''
from getmac import get_mac_address as gma
print(gma())'''
#UUID --> package/library class:
#uuid --> random objects :: 128-bits [random objects/MAC address]
'''
import uuid
#print(hex(uuid.getnode()))

print("The MAC address in formatted way is :",end=' ')
print(':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff)
for ele in range(0,8*6,8)][::-1]))#Negative indexing [::-1])'''








