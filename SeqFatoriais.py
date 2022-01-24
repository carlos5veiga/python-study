cont = 0
while cont >= 0:
    fatorial = 1
    cont = int(input("Digite um número: "))
    if cont >= 0:
        num=1
        while num <= cont:
            fatorial = fatorial*num
            num = num+1
        print("O fatorial de", cont, "é", fatorial)
        print()
    
