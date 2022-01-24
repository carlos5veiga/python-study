def bhaskara(a, b, c):
    import math
    delta = ((b**2) - (4*a*c))
    if (delta < 0):
        print("esta equação não possui raízes reais")
    else:
        if (delta == 0):
            print("a raiz desta equação é", ((-b)/(2*a)))
        else:
            raiz1 = ((-b-(math.sqrt(delta)))/(2*a))
            raiz2 = ((-b+(math.sqrt(delta)))/(2*a))
            if (raiz1 < raiz2):
                print("como raízes da equação são", raiz1, "e", raiz2)
            else:
                print("como raízes da equação são", raiz2, "e", raiz1)
