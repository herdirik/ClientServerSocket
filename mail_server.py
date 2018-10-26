#TCP SERVER
import socket
import sys                                         

# create a socket object
mail_server= socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
server_address=('localhost',1100)
file = open('server_mail.txt','r+')
mail_server.bind(server_address)                                  
mail_server.listen(5)       
while True:
    connection, client_address = mail_server.accept()
    print ("Connected...")
    data = connection.recv(4)
    #print data
    if data=="pop3":
        for line in file:
            connection.send(line)
        connection.send("EOF")
        file.close()
        open('server_mail.txt','w+').close()
        file=open('server_mail.txt','r+')
    elif data=="imap":
	#print "imap"
        for line in file:
            #print line
            connection.sendall(line)
        connection.send('EOF')
	file.seek(0)
    else:
        print >>sys.stderr,'Unknown Protocol'  

connection.close()

