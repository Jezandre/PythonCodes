#!/usr/bin/env python3
import sys

argumentos = sys.argv
qtd_argumentos = len(argumentos)

if qtd_argumentos <= 1:
    print('faltando argumentos')
    print('-a', 'Para listar todos os arquivos nesta pasta', sep='\t')
    print('-d', 'Para listar todos os diretórios nesta pasta', sep='\t')
    sys.exit()

so_arquivos = False
if '-a' in argumentos:
    so_arquivos =True


so_diretorios = False
if '-d' in argumentos:
    so_diretorios = True

# for arquivo in os.listdir('.'):
#     if '-a'