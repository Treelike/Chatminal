import socket,os,os,sys,time
from thread import *
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
server.bind(('localhost',1234))
server.listen(5) 

def clientthread(conn):
    db=[cdup for cdup in open('db') if ':' in cdup]
    while True:
        try:
            data=conn.recv(1024)
            if len(thred) == 3:
                thred[1:]=[]
            if len(thred) == 1:
                data=data
            else:
                space=27*' '
                data=space+data
            i=data.index(':')
            if db:
                for idb in db:
                    name=idb.index(':')
                    if idb[:name].strip() == data[:i].strip():
                        conn.send('\nName %s is taken please choose another one!\n however you can still read the conversation\n'%idb[:name].strip())
                        data=''
            with open('db') as cfl:
                cfl=len(cfl.read())
            if cfl > 1024:
                sf=open('db')
                sf.seek((cfl/2))
                seeked=sf.read()
            else:
                seeked=open('db').read()
            if data[i+1:].isspace() or data == '':
                with open('db','w') as rw:
                    rw.write(seeked)
            else:
                s1=7*' '
                sent='%s-Sent on'%s1
                with open('db','a') as af:
                    af.write(data+sent+time.strftime('%T %a \n'))
            dat=open('db').read()
            conn.send(dat+'online:'.rjust(50)+str(len(soc)))
        except (socket.error,ValueError):
            soc.pop(0)
            break

soc=[]
thred=[]
while 1:
    conn,addr = server.accept()
    soc.append(conn)
    thred.append(conn)
    print 'Online: ' + addr[0]
    start_new_thread(clientthread ,(conn,))
