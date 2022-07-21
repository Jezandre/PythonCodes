from time import sleep
from threading import Thread
from threading import Lock


"""# print('Hello')
#
# for i in range(10):
#     print(i)
#     sleep(.5)
#
# print('World!')

class MeuThread(Thread):
    def __init__(self, texto, tempo):
        self.texto = texto
        self.tempo = tempo
        super().__init__()
    def run(self):
        sleep(self.tempo)
        print(self.texto)

t1 = MeuThread('Thread 1', 5)
t1.start()

t2 = MeuThread('Thread 2', 3)
t2.start()

t3 = MeuThread('Thread 3', 2)
t3.start()

for i in range(20):
    print(i)
    sleep(.5)"""

"""def vai_demorar(texto, tempo):
    sleep(tempo)
    print(texto)

t1 = Thread(target=vai_demorar, args=('Olá Mundo!0',2))
t1.start()

t2 = Thread(target=vai_demorar, args=('Olá Mundo!1',5))
t2.start()

t3 = Thread(target=vai_demorar, args=('Olá Mundo!2',1))
t3.start()

for i in range(20):
    print(i)
    sleep(.5)"""

"""def vai_demorar(texto, tempo):
    sleep(tempo)
    print(texto)

t1 = Thread(target=vai_demorar, args=('Olá Mundo!,10')
t1.start()
t1.join()

while t1.is_alive():
    print('Eperando a Thread')
    sleep(2)

print('tHREAD ACABOU')"""

class Ingressos:
    def __init__(self, estoque):
        self.estoque = estoque
        self.lock = Lock()

    def comprar(self, quantidade):
        self.lock.acquire()

        if self.estoque < quantidade:
            print('Não temos ingressos suficientes')
            self.lock.release()
            return

        sleep(1)

        self.estoque -= quantidade
        print(f'Você comprou {quantidade} ingressos. '
              f'Ainda temos {self.estoque}')
        self.lock.release()

if __name__ == '__main__':
    ingressos = Ingressos(10)

    threads =[]
    for i in range(20):
        t = Thread(target=ingressos.comprar, args=(i,))
        threads.append(t)

    for t in threads:
        t.start()

    executando = True
    while executando:
        executando = False

        for t in threads:
            if t.is_alive():
                executando = True
                break


    print(ingressos)

