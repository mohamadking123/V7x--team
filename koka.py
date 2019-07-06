import os
os.system ('clear')
import socket
import sys
print ("=======>| V7X |<=======")
print ("Enter your Target==>")
hostname=input()
ip=socket.gethostbyname(hostname)
print('Hostname:',hostname,'/n' 'IP:',ip)


