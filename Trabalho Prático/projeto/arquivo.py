def lerArquivo(name, name2):
    try:
        estado = []
        arquivo = open(name, 'r')
        for i in arquivo:
            linha = i.split()
            temp = []
            for j in range(len(linha)):
                temp.append( int(linha[j]) )
            estado.append(temp)
        estado2 = []
        arquivo = open(name2, 'r')
        for i in arquivo:
            linha = i.split()
            temp = []
            for j in range(len(linha)):
                temp.append( int(linha[j]) )
            estado2.append(temp)
    except ValueError:
        print('Erro ao tentar manipular arquivo {}'.format(ValueError))
    finally:
        arquivo.close()
    return str(estado), str(estado2)