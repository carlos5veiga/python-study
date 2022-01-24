

def fatorial(num):
    fatorial = 1
    cont = 0

    while cont<num:
        cont = cont + 1
        fatorial = fatorial * cont

    return (fatorial)
       
def binomial(n, k):
    return ((fatorial(n)//(fatorial(k)*fatorial(n-k))))


