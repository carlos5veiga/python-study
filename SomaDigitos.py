num = int(input("Digite um número inteiro: "))
soma = 0
digito = 0
maiorQueDez = True

while maiorQueDez:
    digito = num % 10
    soma = soma + digito
    if num >= 10:
        num = num // 10
    else:
        maiorQueDez = False
        
print(soma)