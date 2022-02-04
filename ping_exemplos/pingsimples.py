import os

print('#'*40)

ip_ou_host = input('Digite o IP ou Host a ser verificado:\n')

print('#'*40)

param  = 'c' if os.name == 'posix' else 'n'

os.system('ping -{} 6 {}\n'.format(param, ip_ou_host))

