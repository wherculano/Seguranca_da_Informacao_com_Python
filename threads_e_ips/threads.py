from threading import Thread
from time import sleep

def carro(velocidade, piloto):
    trajeto = 0
    while trajeto <= 100:
        print(f'Piloto: {piloto}, Km: {trajeto:.2f}\n')
        trajeto += velocidade
        sleep(0.5)
    print(f'Piloto: {piloto} finalizou a corrida!')


thread_car1 = Thread(target=carro, args=(10, 'Wagner'))
thread_car2 = Thread(target=carro, args=(20, 'Danielle'))

thread_car1.start()
thread_car2.start()