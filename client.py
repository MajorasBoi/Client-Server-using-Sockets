import random
import string
import socket


def generar_cadena():
    # This section generates a string of random length
    longitud = random.randint(50, 100)
    cadena = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=longitud))

    # Add random spaces
    espacios = random.randint(3, 5)
    for _ in range(espacios):
        posicion = random.randint(1, longitud-1) # Avoid spaces at the beginning and at the end
        cadena = list(cadena)
        cadena.insert(posicion, ' ')
        cadena = ''.join(cadena)

    return cadena

# Ask the user for the number of strings to generate
num_cadenas = input("Introduce the number for strings to generate: ")
if num_cadenas == '':
    num_cadenas = 1000000
else:
  num_cadenas = int(num_cadenas)

# Create the file and write the strings in it
with open('chains.txt', 'w') as archivo:
 for _ in range(num_cadenas): # Generate the specified number of strings
     cadena = generar_cadena()
     archivo.write(cadena + '\n')

# Connect to the server
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 8080))

analisis = []
while True:
    with open('chains.txt', 'r') as archivo:
        for linea in archivo:
            sock.send(linea.encode())
            data = b''
            data = sock.recv(1024) # receive data from the client
            analisis.append(data.decode())
    break
sock.close()

with open('analisis.txt', 'w') as archivo:
    archivo.write(''.join(analisis))
