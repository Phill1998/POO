# quadrado

class Quadrado:
    def __init__(self, lado):
        self.__lado = lado

    @property
    def area(self):
        area = self.__lado*self.__lado
        return area

    @property
    def perimetro(self):
        perimetro = self.__lado*4
        return perimetro
    

calc = Quadrado(4)
print(calc.area)
print(calc.perimetro)



print ('----' * 10)


# retangulo

class Retangulo:
    def __init__(self, base, altura):
        self.__base = base
        self.__altura = altura

    @property
    def area(self):
        area = self.__base * self.__altura
        return area
    
    @property
    def perimetro(self):
        perimetro = (2*(self.__base*self.__altura))
        return perimetro
    
ret = Retangulo(5,2)
print (ret.area)
print (ret.perimetro)


print ('----' * 10)


# circulo


from math import pi

class Circulo:
    def __init__(self, raio):
        self.__raio=raio
    
    @property
    def peri(self):
        peri = 2* pi * self.__raio
        return peri

    @property
    def diam(self):
        diam = (2*self.__raio) 
        return diam
    

circ =Circulo(2)
print(circ.peri)
print(circ.diam)
print('---' * 8)


# meu triangulo cabuloso


class Triangulo():
    def __init__(self, base, altura, lado_a=5, lado_b=3, lado_c=5, angulo_ab=90, angulo_ac=40, angulo_bc=70):
    
        self.__base = base 
        self.__altura = altura
        self.__lado_a = lado_a
        self.__lado_b = lado_b
        self.__lado_c = lado_c
        self.__angulo_ab = angulo_ab
        self.__angulo_ac = angulo_ac
        self.__angulo_bc = angulo_bc 

    @property
    def base(self):
        return self.__base
    
    @property
    def altura(self):
        return self.__altura
    
    @property
    def lado_a(self):
        return self.__lado_a

    @property
    def lado_b(self):
        return self.__lado_b
    
    @property
    def lado_c(self):
        return self.__lado_c

    @property
    def angulo_ab(self):
        return self.__angulo_ab
    
    @property
    def angulo_ac(self):
        return self.__angulo_ac
    
    @property
    def angulo_bc(self):
        return self.__angulo_bc

    @property 
    def area(self):
         return (self.__base * self.__altura) / 2
 
    @property
    def perimetro(self):
        return self.__lado_a + self.lado_b + self.__lado_c

    @property
    def tipo_triangulo(self):
        if self.__lado_a == self.lado_b and self.lado_b == self.__lado_c:
            return 'triangulo equilatero'
        elif self.__lado_a == self.lado_b or self.lado_a == self.__lado_c:  
            return 'triangulo isóceles'
        else:
            return 'triangulo escaleno'
        



t = Triangulo(5,3, 2, 7, 4)
print(t.tipo_triangulo)