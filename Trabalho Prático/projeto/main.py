from buscar import buscaLargura, buscaProfundidade
from arquivo import lerArquivo

estadoInicial, estadoObjetivo = lerArquivo('estadoInicial.txt', 'estadoObjetivo.txt')

opcao = int(input("Digite 1 ou 2: \n 1: Busca em Largura \n 2: Busca em Profundidade \n "))

if opcao == 1:
    buscaLargura(estadoInicial, estadoObjetivo)
elif opcao == 2:
    buscaProfundidade(estadoInicial, estadoObjetivo)
else:
    print("Opção inválida, insira o numero 1 ou 2")

