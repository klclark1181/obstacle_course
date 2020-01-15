
# This program will scan a class C subnet (24 subnet bits) and tell you what
# responds to a ping, IF you get the variables correct

# Run by typing "sudo python3 ping_scan.py"

from ping3 import ping

# What should be here?
base = '127.0.0'
first_subnet_addr = 1
last_subnet_addr = 2

for i in range(first_subnet_addr, last_subnet_addr + 1):
    addr = base + str(i)
    if ping(addr, timeout = 2) != None:
        print('%s is ALIVE!' % (addr))
