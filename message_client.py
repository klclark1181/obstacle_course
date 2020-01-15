import socket
import threading

# Are these correct?
OpponentIPAddress = '127.0.0.1'
OpponentPort = 0
Message = 'You can come up with something really clever to say here.'

# Do not touch
EndSequence = '1234567890)(*&^%$#@!'

       
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind(('0.0.0.0', 0))
    sock.connect((OpponentIPAddress, OpponentPort))
    data = Message.encode(encoding = 'utf-8') + EndSequence.encode(encoding = 'utf-8')
    sock.send(data)
         
        
    

