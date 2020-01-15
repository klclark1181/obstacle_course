
# This program will port scan a range of TCP ports on a system, and tell
# you which ones are accepting connections, If you set the variables correctly

# Run by typing "sudo python3 port_scan.py"

import socket

def check_port(address, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((address, port))
            return True
        except:
            # print(port)
            return False

# Are these right? You decide
ip_addr = '127.0.0.1'
begin_port = 1
end_port = 700

for i in range(begin_port, end_port + 1):
    if check_port(ip_addr, i) == True:
        print('TCP Port %d is open on %s' % (i, ip_addr))

