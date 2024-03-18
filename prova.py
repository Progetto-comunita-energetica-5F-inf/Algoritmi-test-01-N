import time
batteria = 1000
def countdown(batteria):
    timer = int(input('quante ore vuoi calcolare: '))
    consumo = 6
    consumoTot = 0
    while timer:
        consumoTot += consumo
        print(timer)
        time.sleep(1)
        timer -= 1
        
    print('Hai consumato:')
    print(consumoTot)
    batteria-=consumoTot
    print(batteria)
countdown(batteria)