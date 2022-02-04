import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('Socket created')

host = 'localhost'
port = 5432

s.bind((host, port))  # faz ligação entre cliente e servidor
msg = 'Server: Hello Client'

while True:
    data, path = s.recvfrom(4096)

    if data:
        print('\nServer sending message...')
        s.sendto(data + (msg.encode()), path)

