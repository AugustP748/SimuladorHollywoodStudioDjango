import math

class Generadores:
    def __init__(self):
        ...
    
    def lehmer(self,semilla, a, m):
        # no working
        while True:
            semilla = (a * semilla) % m
            yield self.__valorU(semilla, m)
    
    def congruencial_mixto(self,semilla, a, c, m):
        while True:
            semilla = (a * semilla + c) % m
            yield self.__valorU(semilla, m)
            
    def congruencial_multiplicativo(self,semilla:int, a:int, m:int) -> float:
        """this module generate random pseudonumber using congruential multi
        parameters:
            - semilla: integer
             - a: constant a is integer too
             - m: module m is integer"""
        while True:
            semilla = (a * semilla) % m
            yield self.__valorU(semilla, m)

    def __valorU(self,semilla,m):
        u = semilla / m
        return float("{:.3f}".format(u))
    
if __name__ == '__main__':
    
    semilla_inicial = 1237
    constante_a = 4309
    constante_c = 2311
    modulo_m = 6031
    
    # multiplicativo
    semilla_inicial2 = 1317
    constante_a2 = 5631
    modulo_m2 = 547
    
    #lehmer
    semilla_inicial3 = 4122
    constante_a3 = 48271
    modulo_m3 = 2**31 - 1


    
    g = Generadores()
    r = g.congruencial_mixto(semilla_inicial,constante_a,constante_c,modulo_m)
    r2 = g.congruencial_multiplicativo(semilla_inicial2,constante_a2,modulo_m2)
    r3 = g.lehmer(semilla_inicial3,constante_a3,modulo_m3)
    print("resultado mix")
    print(next(r3))
    print(next(r3))
    