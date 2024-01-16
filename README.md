# Client-Server using Sockets in Python
#### This aplication creates a file of random strings and processes the weight metric of each one by implementing client-server communication via sockets. 
## Tips for installation:
##### 1- Open your terminal and clone this repository: 
    git clone https://github.com/MajorasBoi/Client-Server-using-Sockets.git
##### 2- Change you actual directory in the terminal: 
    cd Client-Server-using-Sockets
##### 3- Create a file called .env and write the following in it:
    HOSTNAME=localhost
    PORT=8080
Change the HOSTNAME and PORT with the values you need.
##### 4- Split the terminal
##### 5- In one terminal run: 
    python server.py
##### 6- In the other run: 
    python client.py
##### 7- Especify the number of strings you want to create and run the script
##### 8- The result will create two text documents:
    - chains.txt contains the generated strings by the client.
    - analisis.txt contains each string weight metric.