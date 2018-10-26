#TCP CLIENT
import socket

file =open('clientEmail.txt','a+')

domain= raw_input("Mail server adresinizi giriniz:")
#create socket object
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#connect the client
server_address_dns=('localhost',5353)
client.connect(server_address_dns)
#print(domain)
client.send(domain)
host=client.recv(100)
#print(host)
clientMail=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_address_mail=(host,1100)
clientMail.connect(server_address_mail)
protocol=raw_input("Protokol(pop3/imap):")
clientMail.send(protocol)
if protocol== "pop3":
    for line in  file:
        print(line)
while True:
    data = clientMail.recv(512)
    print data
    if data[-3:] == "EOF":
        data=data.replace("EOF","")
        if protocol == "pop3":
            file.write(data) 
        break
    
    if protocol == "pop3":
        file.write(data)
        
client.close()
clientMail.close()