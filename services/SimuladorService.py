from GeneradorService import *
import copy
import math

if __name__ == '__main__':
    vrr: int = 0
    tevrr: float = 0
    vmf: int = 0
    tevmf: float = 0
    teh: float = 0
    ted: float = 0
    tem: float = 0
    cvd: float = 0
    tiempo_de_espera_mes: dict = dict()
    te_promedio_hora:dict = dict()
    generate = Generadores()
    new_u_value: float = generate.congruencial_multiplicativo(1317, 5631, 547)
    # for de dias
    for d in range(30):
        #for de horas
        for h in range(8):
            
            u: float = next(new_u_value)
            cvh: int = math.trunc(227*(227-226)*u) #cantidad de visitantes en la hora x
            cvd+=cvh #cantidad de visitantes diarios = suma de cant. visit. en las 8hs del día
            #print(cvh)
            
            for _ in range(cvh):
                """for de visitantes"""
                u = next(new_u_value)
                if u <= 0.65:
                    vrr+=1 #cantidad de visitantes que visitan atarcción RR en la hora
                    u = next(new_u_value)
                    teminrr=-190*math.log10(u) #TE en minutos en atraccion RR
                    #print(teminrr)
                    tevrr+=teminrr #TE total de visitantes en atracción RR
                else:
                    vmf+=1 #cantidad de visitantes que visitan atarcción MF en la hora
                    u = next(new_u_value)
                    teminmf=-85*math.log10(u) #TE en minutos en atraccion MF
                    tevmf+=teminmf #TE total de visitantes en atracción MF
                
            teh = teh + tevrr + tevmf #tiempo de espera total en la hora
            ted+=teh # tiempo de espera del dia es suma de TE total por cada hora
            #print(teh/cvh) # promedio tiempo de espera de la hora
            te_promedio_hora[h+1] = float("{:.3f}".format(teh/cvh))
            teh=0 # reiniciamos TE de la hora para la siguiente hora
            tevmf=0
            tevrr=0
            
        tiempo_de_espera_mes[d+1] = copy.copy(te_promedio_hora)
        te_promedio_hora.clear()  
        tem+=ted
        ted=0
    #print(tem/cvd) # promedio tiempo de espera mensual   
      

    #print(tiempo_de_espera_mes)
    for valor_externo in tiempo_de_espera_mes.values():
            print(valor_externo)
        