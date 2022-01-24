def ordenada(lista):
    for i in range(len(lista)-1):
        for j in range(i+1,len(lista)):
            if lista[i]>lista[j]:
                return False
    return True
