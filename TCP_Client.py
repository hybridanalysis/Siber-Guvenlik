import socket
target_host = "www.google.com"
target_port = 80

#Soket nesnesi oluştur.
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#istemciye bağlan
client.connect((target_host,target_port))

#birşeyler gönderelim
client.send("GET / HTTP/1.1\r\nHOST:google.com\r\n\r\n")

#Yanıt alalım
response = client.recv(4096)
print response