import socket
target_host = "127.0.0.1"
target_port = 80

#Soket nesnesi oluştur.
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


#birşeyler gönderelim
client.sendto("ABCD",(target_host,target_port))

#Yanıt alalım
data, addr = client.recvfrom(4096)
print data