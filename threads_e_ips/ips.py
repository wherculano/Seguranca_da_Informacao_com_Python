import ipaddress

ip_1 = '192.168.0.1'
ip_2 = '192.168.0.0/24'  # de 0 a 32

endereco = ipaddress.ip_address(ip_1)
rede = ipaddress.ip_network(ip_2)
print(endereco)
for ip in rede:
    print(ip)