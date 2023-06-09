import requests
import time
import random
print('Inicializando simulação de subsistema de monitoramento (Ctrl^C p/ Sair): ')
while True:
    try:
        data = {'current': 4.5+random.random(), 'voltage': 220+random.random()*10}
        requests.post('http://localhost:5000/', json=data,)
        print(
            f"At {time.ctime()} - Current: { data['current']} A, Voltage: { data['voltage']} V")
        time.sleep(5)
    except KeyError:
        break
    except:
        print('Erro de conexão, lembre de inicializar o sistema.')
        break
print('Finalizando simulação.')
