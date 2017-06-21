import socket

#define target
target_host = "0.0.0.0"
target_port = 9999

#create socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#client connection
client.connect((target_host,target_port))
#send data
client.send("uname -a")
#get some data
response = client.recv(4096)

print response
