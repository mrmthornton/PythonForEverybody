'''
Created on Nov 25, 2015

@author: mike
'''
import socket

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addrAndPort = ('www.py4inf.com', 80)
mySocket.connect(addrAndPort)
#mySocket.send('GET http://www.py4inf.com/code/romeo.txt HTTP/1.0\n\n')
mySocket.send('GET http://www.pythonlearn.com/code/intro-short.txt HTTP/1.0\n\n')

while True:
    receivedData = mySocket.recv(512)
    if len(receivedData) < 1 :
        break
    print receivedData
mySocket.close()
