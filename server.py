import socket
import re

# Create a socket and bind it to a specific address and port
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 8080))
print('Server listening on port 8080') 
sock.listen(1) # listen for incoming connections
conn, addr = sock.accept() # accept a connection from a client


counter = 1
cadenas = []
while True:
    data = b''
    data = conn.recv(1024) # receive data from the client

    if data:
        data = data.decode()
        # Check for double 'a' rule
        if re.search(r'(aa|AA|aA|Aa)', data):
            message = "Double 'a' rule detected in string " + str(counter) + ">> '" + data + "'" + ": 1000\n"
            conn.send(message.encode())
            counter += 1
        else:
            # Calculate string weight metric
            letters = len(re.findall(r'[a-zA-Z]', data))
            numbers = len(re.findall(r'\d', data))
            spaces = len(data.split())
            if spaces == 0:
                break
            response = str((letters * 1.5 + numbers * 2) / spaces)
            message = "String " + str(counter) + ": " + response + '\n'
            conn.send(message.encode())
            counter += 1      

conn.close() # close the connection
sock.close()
