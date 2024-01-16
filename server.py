import os
import socket
import re
import time
import logging

# Configure logging to display INFO level messages and above
logging.basicConfig(level=logging.INFO, format='%(message)s')

# Read environment variables from .env file
with open('.env') as f:
   for line in f:
       name, value = line.strip().split('=', 1)
       os.environ[name] = value

# Create a socket object, bind it and listen for incoming connections
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((os.getenv('HOSTNAME'), int(os.getenv('PORT'))))
logging.info('Server listening on port %s', os.getenv('PORT'))
sock.listen(1) 

# Variables of general purpose
flag = True
counter = 1

# This will allow the server to always be looking for connections
while True:
   # Accept a connection from a client
   conn, addr = sock.accept() 
   # Begin the transactions
   while True:
       data = b''
       # Receive data from the client
       data = conn.recv(1024) 
       # Record the start time
       if flag is True:
           start_time = time.time()
           flag = False

       if data:
           data = data.decode()
           # Check if the data contains double 'a' (either lowercase or uppercase)
           if re.search(r'(aa|AA|aA|Aa)', data):
               message = "Double 'a' rule detected in string " + str(counter) + ">> '" + data + "'" + ": 1000\n"
               logging.info(message)
               conn.send(message.encode())
               counter += 1
           else:
               # Calculate the string weight metric
               letters = len(re.findall(r'[a-zA-Z]', data))
               numbers = len(re.findall(r'\d', data))
               spaces = len(data.split())
               response = str((letters * 1.5 + numbers * 2) / spaces)
               message = "String " + str(counter) + ": " + response + '\n'
               conn.send(message.encode())
               logging.info("String %s analisis sent to the client", counter)
               counter += 1 
       else:
           counter = 1
           # Record the end time
           end_time = time.time()
           break 
       
   conn.close() 
   
   # Calculate the total processing time
   total_time = end_time - start_time
   logging.info("Process completed in %s seconds", total_time)  
