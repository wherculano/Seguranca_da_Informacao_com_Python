import hashlib

txt = input('Texto: ')

hashes = {
    1: ('MD5', hashlib.md5), 
    2: ('SHA1', hashlib.sha1), 
    3: ('SHA256', hashlib.sha256), 
    4: ('SHA512', hashlib.sha512)
    }

# menu = int(input(
#     ''' #### MENU - ESCOLHA O TIPO DE HASH ####
#     1) MD5
#     2) SHA1
#     3) SHA256
#     4) SHA512
#     Digite o nº correspondente ao hash desejado: '''
#     ))

for i in range(1, 5):
    resultado = hashes[i][1](txt.encode('utf-8'))

    print(f'\nHash {hashes[i][0]}: {resultado.hexdigest()}')