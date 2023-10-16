import socket
soc = socket.socket()
print('socket succesfully created')

port = 1234
soc.bind(('',port))
print(f'socket binded to port{port}')

soc.listen(5)
print('socket is listening')
while True:
    c, addr = soc.accept()
    print('Got connection from', addr)
    message = ('thank you for connecting')
    c.send(message.encode())
    c.close()