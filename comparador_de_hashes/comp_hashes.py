import hashlib

file1 = 'file_1.txt'
file2 = 'file_2.txt'

hash1 = hashlib.new('ripemd160')
hash1.update(open(file1, 'rb').read())

hash2 = hashlib.new('ripemd160')
hash2.update(open(file2, 'rb').read())

if hash1.digest() != hash2.digest():  # resume dados passados ao update
    print(f'O arquivo: {file1} é diferente do arquivo: {file2}\n')
    print(f'Hash1: {hash1.hexdigest()}\nHash2: {hash2.hexdigest()}\n')
else:
    print(f'O arquivo: {file1} é igual ao arquivo: {file2}\n')
    print(f'Hash1: {hash1.hexdigest()}\nHash2: {hash2.hexdigest()}\n')