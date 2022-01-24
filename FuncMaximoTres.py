def maximo(n1, n2, n3):
    max = n1
    if n1 <= n2:
        max = n2
    if n2 <= n3:
        max = n3
    return max
