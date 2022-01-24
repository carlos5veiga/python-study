num = int(input("Digite um número inteiro: "))
digito = num%10
num = num // 10
adjacentes = False

while ((num>=1) and (not(adjacentes))):
    if (digito == num%10):
        adjacentes = True
    else:
        digito = num%10
        num = num // 10
    
    
if (adjacentes):
    print("sim")
else:
    print("não")
