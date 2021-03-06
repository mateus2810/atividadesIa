from os import system
from time import sleep

def mover(estado):
    movimentos = []
    est = eval(estado)
    i = 0
    j = 0
    while 0 not in est[i]: i += 1
    j = est[i].index(0)

    if j > 0:
        est[i][j], est[i][j - 1] = est[i][j - 1], est[i][j]
        movimentos.append(str(est))
        est[i][j], est[i][j - 1] = est[i][j - 1], est[i][j]

    if i > 0:
        est[i][j], est[i - 1][j] = est[i - 1][j], est[i][j]
        movimentos.append(str(est))
        est[i][j], est[i - 1][j] = est[i - 1][j], est[i][j]

    if j < 2:
        est[i][j], est[i][j + 1] = est[i][j + 1], est[i][j]
        movimentos.append(str(est))
        est[i][j], est[i][j + 1] = est[i][j + 1], est[i][j]

    if i < 2:
        est[i][j], est[i + 1][j] = est[i + 1][j], est[i][j]
        movimentos.append(str(est))
        est[i][j], est[i + 1][j] = est[i + 1][j], est[i][j]

    return movimentos

def buscaLargura(inicial, final):
    nosExpandidos = 0
    fila = [[inicial]]
    while True:
        if not fila: raise Exception
        caminhoFila = fila[0]
        fila = fila[1:]
        estadoAtualNo = caminhoFila[-1]
        movimentoBuscaLargura(estadoAtualNo, nosExpandidos)
        if estadoAtualNo == final: break
        for movimento in mover(estadoAtualNo):
            fila.append(caminhoFila + [movimento])
        nosExpandidos += 1
    return caminhoFila

noExp = 0

def buscaProfundidadeLimitada(inicial, final, limite):
    profundidade = 0
    pilha = [[inicial]]
    global noExp
    while True:
        if not pilha:
            return None
        else:
            caminhoFila = pilha[-1]
            pilha = pilha[:-1]
            estadoAtualNo = caminhoFila[-1]
            movimentoProfundidade(estadoAtualNo, noExp)
            if estadoAtualNo == final: break
            if profundidade >= limite: continue
            for movimento in mover(estadoAtualNo):
                pilha.append(caminhoFila + [movimento])
            profundidade += 1
            noExp += 1
    return caminhoFila

def buscaProfundidade(inicial, final):
    limite = 0
    while True:
        caminho = buscaProfundidadeLimitada(inicial, final, limite)
        if caminho: break
        limite += 1
    return caminho

def contagemPosicaoForaLugar(estadoInicial, estadoFinal):
    estadoI = eval(estadoInicial)
    estadoF = eval(estadoFinal)
    posicaoDiferente = 0
    for i in range(0,3):
        for j in range(0,3):
            if estadoI[i][j] != estadoF[i][j]:
                posicaoDiferente += 1
    return posicaoDiferente

def buscaGulosa(estadoInicial, estadoObjetivo):
    nosExpandidos = 0
    listaNosExplorados = []
    borda = [[contagemPosicaoForaLugar(estadoInicial, estadoObjetivo), estadoInicial]]
    while borda:
        i = 0
        for j in range(1, len(borda) ):
            if (borda[i][0]) > (borda[j][0]):
                i = j
        caminho = borda[i]
        borda = borda[:i] + borda[i+1:]
        fimCaminho = caminho[-1]
        movimentoBuscaGulosa(fimCaminho, nosExpandidos)
        if fimCaminho == estadoObjetivo: break
        if fimCaminho in listaNosExplorados: continue
        for movimento in mover(fimCaminho):
            if movimento in listaNosExplorados: continue
            borda.append([contagemPosicaoForaLugar(movimento, estadoObjetivo)] + caminho[1:] + [movimento])
        listaNosExplorados.append(fimCaminho)
        nosExpandidos+=1
    return caminho


def buscaAEstrela(estadoInicial, estadoObjetivo):
    profundidade = 1
    nosExpandidos = 0
    listaNosExplorados = []
    borda = [[contagemPosicaoForaLugar(estadoInicial, estadoObjetivo), profundidade, estadoInicial]]
    while borda:
        i = 0
        for j in range(1, len(borda) ):
            if (borda[i][0]) > (borda[j][0]):
                i = j
        caminho = borda[i]
        borda = borda[:i] + borda[i+1:]
        fimCaminho = caminho[-1]
        movimentoBuscaAEstrela(fimCaminho, nosExpandidos)
        if fimCaminho == estadoObjetivo: break
        if fimCaminho in listaNosExplorados: continue
        profundidade = caminho[1] + 1
        for movimento in mover(fimCaminho):
            if movimento in listaNosExplorados: continue
            valor = contagemPosicaoForaLugar(movimento, estadoObjetivo) + profundidade
            borda.append([valor] + [profundidade] + caminho[2:] + [movimento])
        listaNosExplorados.append(fimCaminho)
        nosExpandidos+=1
    return caminho

def movimentoBuscaLargura(estado, noExpandido):
        system('cls')
        estado = eval(estado)
        print(" Busca em Largura:\n")
        print("  Nós Expandidos: %d\n" % (noExpandido))
        print('      ', estado[0][0], estado[0][1], estado[0][2])
        print('      ', estado[1][0], estado[1][1], estado[1][2])
        print('      ', estado[2][0], estado[2][1], estado[2][2])
        print("\n")
        sleep(1)

def movimentoProfundidade(estado, noExpandido):
    system('cls')
    estado = eval(estado)
    print("Busca em Profundidade Limitada:\n")
    print("  Nós Expandidos: %d\n" % (noExpandido))
    print('      ', estado[0][0], estado[0][1], estado[0][2])
    print('      ', estado[1][0], estado[1][1], estado[1][2])
    print('      ', estado[2][0], estado[2][1], estado[2][2])
    print("\n")
    sleep(1)

def movimentoBuscaGulosa(estado, noExpandido):
    system('cls')
    estado = eval(estado)
    print("Busca Gulosa:\n")
    print("  Nós Expandidos: %d\n" % (noExpandido))
    print('      ', estado[0][0], estado[0][1], estado[0][2])
    print('      ', estado[1][0], estado[1][1], estado[1][2])
    print('      ', estado[2][0], estado[2][1], estado[2][2])
    print("\n")
    sleep(1)

def movimentoBuscaAEstrela(estado, noExpandido):
    system('cls')
    estado = eval(estado)
    print("Busca A Estrela:\n")
    print("  Nós Expandidos: %d\n" % (noExpandido))
    print('      ', estado[0][0], estado[0][1], estado[0][2])
    print('      ', estado[1][0], estado[1][1], estado[1][2])
    print('      ', estado[2][0], estado[2][1], estado[2][2])
    print("\n")
    sleep(1)



