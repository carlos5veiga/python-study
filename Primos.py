num = int(input("Digite um número inteiro: "))
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
        print("primo")
    else:
        print("não primo")
