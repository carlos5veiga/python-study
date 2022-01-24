def ePrimo(k):
    quantDivisoes = 0
    cont = k
    while ((cont!=0) and (quantDivisoes<3)):
        if (k%cont==0):
            quantDivisoes = quantDivisoes + 1
        cont = cont - 1
    if (quantDivisoes<=2):
        return True
    else:
        return False





def maior_primo(n):
    if n<2:
        return 0
    cont = primo = 2
    while cont <= n:
        if ePrimo(cont):
            primo = cont
        cont = cont + 1
    return primo
        
