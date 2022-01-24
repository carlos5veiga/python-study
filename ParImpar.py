num = int(input("Digite um número inteiro: "))
if (num==0):
    print("O número", num, "não é ímpar nem par.")
else:
    if (num%2):
        print("O número", num, "é ímpar.")
    else:
        print("O número", num, "é par.")