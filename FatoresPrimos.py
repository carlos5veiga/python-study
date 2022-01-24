def primo(num):
    quantDivisoes = 0
    cont = num
    while ((cont!=0) and (quantDivisoes<3)):
        if (num%cont==0):
            quantDivisoes = quantDivisoes + 1
        cont = cont - 1
    if (quantDivisoes==0):
        print("O zero não vale")
    else:
        if (quantDivisoes<=2):
            return True
        else:
            return False


num = int(input("Informe um número inteiro maior que 1: "))
if num > 1:
    print(num, "=", end=" ")
    fator = num
    cont = 2
    resto = 0
    while fator>1:
        while resto == 0:
            if primo(cont):
                if fator%cont == 0:
                    print(cont, end=" ")
                    fator = fator//cont
                    resto = 0
                    if fator != 1:
                        print("* ", end=" ")
                else:
                    resto = 1
            else:
                resto = 1
        cont = cont+1
        resto = 0
