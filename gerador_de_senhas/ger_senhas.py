import random
import string

tamanho = int(input('Digite o tamanho desejado da senha a ser criada: '))

chars = string.ascii_letters + string.digits + string.punctuation + 'çÇ'

rnd = random.SystemRandom()

print(''.join(rnd.choice(chars) for _ in range(tamanho)))
