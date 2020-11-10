#!/bin/bash                               
                                          
import sys #allows us to enter command line
import socket                             
from datetime import datetime             


if len(sys.argv) == 2:
 target = socket.gethostbyname(sys.argv[1]) #Translates a hostname to IPV4
                                                                          

else:
 print("invalid amount of argument")
 print ("syntax: python-scanner.py")
 sys.exit()

#Adding target
print("-" * 50)
print("Scaninng target" + target)
print("Time started" + str(datetime.now()))
print("-" * 50)

try:
 for port in range(50,85):
  s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
  socket.setdefaulttimeout(1) # A float
  result=s.connect_ex((target,port))
  print("Checking port{}".format(port))
  if result == 0:
   print("port{} is open".format(port))
  s.close()

except KeyboardInterrupt:
 print("\nExiting Terminal")
 sys.exit()

except socket.gaierror:
 print("\nHostname colud not be resolved.") 
 sys.exit()

except socket.error:
 print("Couldn't connect to Server.")
 sys.exit()                                   
                                              
