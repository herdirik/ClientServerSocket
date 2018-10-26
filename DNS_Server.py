
import sys
import socket
#create a socket
dns_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address=('localhost',5353)
dns_server.bind(server_address)
dns_server.listen(1)


domain_Dict={}
with open("network.txt","r") as DNStable :
    for satir in DNStable:
        domain, ip = satir.strip().split(" ")
        domain_Dict[domain]=ip

while True:
   clientsocket,addr = dns_server.accept() #istegi kabul ettik.
   r_domain = clientsocket.recv(128) #gelen istegin domainini aldik.
   print(r_domain)
   #print(domain_Dict)
   print(domain_Dict[r_domain])
   clientsocket.send(domain_Dict[r_domain]) #domainin ipsini karsiya gonderdik.



