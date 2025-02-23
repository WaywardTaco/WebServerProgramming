#import socket module
from socket import *
import sys # In order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket
#Fill in start
serverSocket.bind(('', 6969))
serverSocket.listen()
#Fill in end


while True:
    #Establish the connection
    print('CSNETWK Web Server is ready to serve...')
    #Fill in start     
    connectionSocket, addr = serverSocket.accept()
    #Fill in end
    
    try:
        #Fill in start 
        message = connectionSocket.recv(1024).decode()
        #Fill in end
        filename = message.split()[1]
        f = open(filename[1:])
        #Fill in start 
        outputdata = f.read()
        f.close()
        #Fill in end
        #Send one HTTP header line into socket
        #Fill in start
        connectionSocket.send('HTTP/1.0 200 OK\r\n\r\n'.encode())
        #Fill in end
        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
       
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
    
    except IOError:
        print("Error encountered")
        #Send response message for file not found
        #Fill in start
        connectionSocket.send('404 Not Found'.encode())
        #Fill in end
       
        #Close client socket
        #Fill in start
        connectionSocket.close()
        #Fill in end
serverSocket.close()
sys.exit()  #Terminate the program after sending the corresponding data