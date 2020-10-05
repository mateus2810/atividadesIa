#Atividade 8
def somarLista(numList):
    if len(numList) == 1:
        return numList[0]
    else:
        return numList[0] + somarLista(numList[1:])

print(somarLista([1,3,5,7,10]))