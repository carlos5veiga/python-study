largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))
contLarg = contAlt = 1
while contAlt <= altura:
    while contLarg <= largura:
        print("#", end="")
        contLarg = contLarg + 1
    print()
    contLarg = 1
    contAlt = contAlt + 1
