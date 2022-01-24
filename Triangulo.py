class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


    def perimetro(self):
        return self.a + self.b + self.c

    def tipo_lado(self):
        self.tipo=''
        if self.a == self.b and self.a == self.c:
            self.tipo='equilátero'
        elif self.a == self.b or self.a == self.c or self.b == self.c:
            self.tipo='isóceles'
        else:
            self.tipo='escaleno'
        return self.tipo

    def retangulo(self):
        if ((self.a**2==self.b**2 + self.c**2) or
            (self.b**2==self.a**2 + self.c**2) or
            (self.c**2==self.a**2 + self.b**2)):
            return True
        else:
            return False

    def semelhantes(self, triangulo):
        lista1 = [self.a, self.b, self.c]
        lista1.sort()
        lista2 = [triangulo.a, triangulo.b, triangulo.c]
        lista2.sort()
        r0 = lista1[0] / lista2[0]
        r1 = lista1[1] / lista2[1]
        r2 = lista1[2] / lista2[2]
        if r0 == r1 and r0 == r2:
            return True
        else:
            return False

    
