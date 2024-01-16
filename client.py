import random
import string
import socket
import os

# Read environment variables from .env file
with open('.env') as f:
   for line in f:
       name, value = line.strip().split('=', 1)
       os.environ[name] = value

# Function to generate a random string of characters, digits and spaces
def generate_string():
   # Generate a random length for the string
   length = random.randint(50, 100)
   # Generate the string using random choices from uppercase, lowercase and digits
   strng = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=length))

   # Add random spaces to the string
   spaces = random.randint(3, 5)
   for _ in range(spaces):
       position = random.randint(1, length-1) # Avoid spaces at the beginning and at the end
       strng = list(strng)
       strng.insert(position, ' ')
       strng = ''.join(strng)

   return strng

# Ask the user for the number of strings to generate
num_strings = input("Introduce the number for strings to generate: ")
# If no input is provided, default to 1000000
if num_strings == '':
   num_strings = 1000000
else:
 num_strings = int(num_strings)

# Open a file named 'chains.txt' in write mode and write the generated strings into it
with open('chains.txt', 'w') as f:
 for _ in range(num_strings):
    strng = generate_string()
    f.write(strng + '\n')

# Create a socket and connect it to the server running on localhost at port 8080
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((os.getenv('HOSTNAME'), int(os.getenv('PORT'))))

# List to store the analysis results
analisis = []
while True:
   # Open the 'chains.txt' file in read mode
   with open('chains.txt', 'r') as f:
       for line in f:
           # Send the string to the server
           sock.send(line.encode())
           # Receive data from the server
           data = b''
           data = sock.recv(1024)
           analisis.append(data.decode())
   break
# Close the socket connection
sock.close()

# Open a file named 'analisis.txt' in write mode and write the analysis results into it
with open('analisis.txt', 'w') as f:
   f.write(''.join(analisis))
