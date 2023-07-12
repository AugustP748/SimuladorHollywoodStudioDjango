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
    
    