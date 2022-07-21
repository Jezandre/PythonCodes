import os

caminho_procura = input('Digite o caminho: ')
termo_procura = input('Digite o que está procurando: ')

conta = 0


def formata_tamanho(tamanho):
    base = 1024
    kilo = base
    mega = base ** 2
    giga = base ** 3
    tera = base ** 4
    peta = base ** 5
    if tamanho < kilo:
        texto = 'B'
    elif tamanho < mega:
        tamanho /= kilo
        texto = 'K'
    elif tamanho < giga:
        tamanho /= mega
        texto = 'M'
    elif tamanho < tera:
        tamanho /= giga
        texto = 'G'
    elif tamanho < peta:
        tamanho /= tera
        texto = 'T'
    else:
        tamanho /= peta
        texto /= 'P'

    tamanho = round(tamanho,2)
    return f'{tamanho}{texto}'



for raiz, diretorios, arquivos in os.walk(caminho_procura):
    for arquivo in arquivos:
        if termo_procura in arquivo:
            try:
                conta += 1
                caminho_completo = os.path.join(raiz, arquivo)
                nome_arquivo, ext_arquivo = os.path.splitext(arquivo)
                tamanho = os.path.getsize(caminho_completo)

                print()
                print('Encontrei o ', arquivo)
                print('Nome: ', nome_arquivo)
                print('Extensão', ext_arquivo)
                print('Caminho:', caminho_completo)
                print(f'Tamanho: ', formata_tamanho(tamanho))
            except PermissionError as e:
                print('Sem permissões')
            except FileNotFoundError as e:
                print('Arquivo não encontrado')
            except Exception as e:
                print('Erro desconhecido: ', e)
print()
print(f'{conta} arquivos encontrados')
