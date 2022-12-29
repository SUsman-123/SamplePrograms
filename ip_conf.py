import socket
s = socket.socket()
port = 40674
s.bind(('',port))
print("Socket binded to %s"%(port))
s.listen(5)
print("Socket is listening")
while True:
    c, addr = s.accept()#Single line multi variable assignment
    #print(c)
    print('Got connection from',addr)
    c.send(b'Thank You for connecting')
    c.close()













