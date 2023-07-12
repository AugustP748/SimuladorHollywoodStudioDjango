from GeneradorService import *
import pandas as pd
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
    tuple: tuple = ()
    atractions:dict = dict()
    general_table:list=[]
    generate = Generadores()
    new_u_value: float = generate.congruencial_multiplicativo(1317, 5631, 547)
    # for de dias
    for d in range(30):
        #for de horas
        for h in range(8):
            tuple+=(d+1,)
            tuple+=(h+1,)
            u: float = next(new_u_value)
            cvh: int = math.trunc(227*(227-226)*u) #cantidad de visitantes en la hora x
            cvd+=cvh #cantidad de visitantes diarios = suma de cant. visit. en las 8hs del día
            tuple+=(cvh,)
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
            atractions["RR"] = float("{:.2f}".format(tevrr/vrr))
            atractions["MF"] = float("{:.2f}".format(tevmf/vmf))
            
            tuple+=(copy.copy(atractions),)
            #print(teh/cvh) # promedio tiempo de espera de la hora
            vrr=0
            vmf=0
            tevmf=0
            tevrr=0
            general_table.append(copy.copy(tuple))
            tuple=()
            atractions.clear()
            
            #te_table = [(1,1,{"RR":45.6,"MF":78.9}),(1,2,{"RR":57.8,"MF":33.7}),(1,3,{"RR":22.1,"MF":71.4}),(2,1,{"RR":98.3,"MF":83.2}),(2,2,{"RR":67.8,"MF":34.7}),(2,3,{"RR":41.1,"MF":56.9})]


        tem+=ted
        ted=0
    #print(tem/cvd) # promedio tiempo de espera mensual   
    
    df = pd.DataFrame(general_table)
    #print(df.loc[0:4, [1,3,6]])
    # Renombrar las columnas
    df = df.rename(columns={0: "día", 1: "hora", 2: "visitantes", 3: "atracciones"})

    # Establecer el índice
    df = df.set_index(["día", "hora", "visitantes"])
    print(df.loc[df.index.get_level_values("día") == 30])
    print()
    #print(df.describe())
    #print()
    #print(df.describe().loc['mean']) #tiempos de espera promedio de cada día
    #print()
    #print(df.describe().loc['mean'].mean()) #tiempo de espera promedio en el mes
    
    
    

    #print(tiempo_de_espera_mes)
    #for valor_externo in tiempo_de_espera_mes.values():
    #        print(valor_externo)
        