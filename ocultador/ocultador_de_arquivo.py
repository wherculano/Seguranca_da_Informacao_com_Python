import ctypes
import os

atributo_ocultar = 0x02  # significa que será ocultado
file_name = 'arquivo_a_ser_ocultado.txt'

if os.name != 'posix':
    retorno = ctypes.windll.kernel32.SetFileAttributesW(file_name, atributo_ocultar)

    if retorno:
        print('Arquivo foi ocultado')
    else:
        print('Arquivo não foi ocultado')
else:
    os.rename(file_name, '.'+file_name)
