"""
Pilhas e filas
Pilha (stack) - LIFO -last in, first out.
    Exemplo: Pilha de livros que são adicionados um sobre o outro
Fila(queue) - FIFO first in, First out.
    Exemplo: uma fila de banco ( ou qualquer fila da vida real)
Filas podem ter efeitos colaterais em desempenho, ,porque a cada item
alterado, todos os ídices  serão modificados.
"""
"""Pilha"""

# livros = list()
# livros.append('Livro 1') #1
# livros.append('Livro 2') #2
# livros.append('Livro 3') #3
# livros.append('Livro 4') #4
# livros.append('Livro 5') #5
# livro_removido = livros.pop()
# livro_removido = livros.pop()
# livro_removido = livros.pop()
# livro_removido = livros.pop()
# livro_removido = livros.pop()
#
# print(livros, livro_removido)

from collections import deque

fila = deque(maxlen=5)

fila.append('Jezandre')
fila.append('Thais')
fila.append('Tiago')
fila.append('Felipe')
fila.append('José')
fila.append('João')
fila.append('João')
fila.append('João')
fila.append('João')



print(fila)
