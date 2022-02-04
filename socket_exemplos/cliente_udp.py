import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # ipv4, udp
print(' Client Socket created '.center(50, '#'))
print()

host = 'localhost'
port = 5433

msg = 'Hello server\n'

try:
    # print(f'Client: {msg}')
    s.sendto(msg.encode(), (host, 5432))  # porta do servidor

    data, server = s.recvfrom(4096)  # numero de bytes
    data = data.decode()
    print(f'Client: {data}')
finally:
    print()
    print(' Closing Client connection '.center(50, '#'))
    s.close()


