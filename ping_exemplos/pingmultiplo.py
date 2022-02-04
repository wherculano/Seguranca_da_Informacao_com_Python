import os
import time

with open('hosts.txt') as file:
    dump = file.read()
    dump = dump.splitlines()
    
    param = 'c' if os.name == 'posix' else 'n'

    for ip in dump:
        print(f'\nVerificando o ip: {ip}')
        os.system(f'ping -{param} 2 {ip}')
        time.sleep(5) 
