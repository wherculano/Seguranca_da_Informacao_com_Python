import socket
import sys

def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)  #IP, TCP, TCP
    except socket.error as e:
        print('Conexao falhou!')
        print(f'Error: {e}')
        sys.exit(1) # 1 indica que houve um erro e por isso fechou. 0 seria saida sem erros

    print('Socket criado com sucesso!')

    host_alvo = input('Host/Ip a ser conectado: ')
    porta_alvo = int(input('Porta a ser conectada: '))
    
    try:
        s.connect((host_alvo, porta_alvo))
        print(f'Cliente TCP conectado com sucesso no host {host_alvo} e na porta {porta_alvo}')
        s.shutdown(2)  # aguarda 2s para fechar a conexão
    except socket.error as e:
        print(f'Não foi possível conectar no host {host_alvo}/porta {porta_alvo}')
        print(f'Erro: {e}')
        sys.exit(1)

if __name__ == '__main__':
    main()
