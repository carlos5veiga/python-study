def ordena(lista):
    fim = len(lista)
    for i in range(fim-1):
        menor_indx = i
        for j in range(i+1,fim):
            if lista[j]<lista[menor_indx]:
                menor_indx = j
        lista[i], lista[menor_indx] = lista[menor_indx], lista[i]
    return lista



lista1 = [0, 3, 6, 2, -4, -2, 0, 3]
lista2 = [0, 3, 3, 2, -4, -2, -1, 3, 8, 10]
lista3 = [0, 3, 3, 2, -4, -2, -1, 3, 8, 10, -100]
lista4 = [0, 3, 200, 50, -4, -2, -112, 3, 8, 10, -100]

ordena(lista1)
ordena(lista2)
ordena(lista3)
ordena(lista4)
