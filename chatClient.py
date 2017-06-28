import socket,sys 
clientsocket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(('localhost',1234))
print 'Connected !'
Cname=raw_input('Chatname: ')
while 1:
        msg=raw_input(' Send:')
        clientsocket.send(' %s: %s \n'%(Cname,msg))
        db=clientsocket.recv(1000024)
        sys.stdout.flush()
        print db,
        print '\r',
