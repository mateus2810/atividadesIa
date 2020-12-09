from buscar import buscaLargura, buscaProfundidade, buscaGulosa, buscaAEstrela
from arquivo import lerArquivo

estadoInicial, estadoObjetivo = lerArquivo('estadoInicial.txt', 'estadoObjetivo.txt')

opcao = int(input("Digite 1 a 4: \n 1: Busca em largura \n 2: Busca em Profundidade \n "
                  "3: Busca Gulosa \n 4: Busca A* (AEstrela) \n "))

if opcao == 1:
    buscaLargura(estadoInicial, estadoObjetivo)
elif opcao == 2:
    buscaProfundidade(estadoInicial, estadoObjetivo)
elif opcao == 3:
    buscaGulosa(estadoInicial, estadoObjetivo)
elif opcao == 4:
    buscaAEstrela(estadoInicial, estadoObjetivo)
else:
    print("Opção inválida, insira o numero 1 ou 2")
