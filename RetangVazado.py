largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))
contLarg = contAlt = 1
while contAlt <= altura:
    while contLarg <= largura:
        if contAlt == 1 or contAlt == altura:
            print("#", end="")
        else:
            if contLarg == 1 or contLarg == largura:
                print("#", end="")
            else:
                print(" ", end="")
        contLarg = contLarg + 1
    print()
    contLarg = 1
    contAlt = contAlt + 1
