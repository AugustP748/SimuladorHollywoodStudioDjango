from .GeneradorService import Generadores
import pandas as pd
import copy
import math

class Simulador:
    def __init__(self):
        self.vrr: int = 0
        self.tevrr: float = 0
        self.vmf: int = 0
        self.tevmf: float = 0
        self.teh: float = 0
        self.ted: float = 0
        self.tuple: tuple = ()
        self.atractions:dict = dict()
        self.general_table:list=[]
        self.generate = Generadores()
        self.new_u_value: float = self.generate.congruencial_multiplicativo(1317, 5631, 547)

    
    def simular(self):
        # for de dias
        for d in range(30):
            #for de horas
            for h in range(8):
                tuple+=(d+1,)
                tuple+=(h+1,)
                u: float = next(self.new_u_value)
                cvh: int = math.trunc(227*(227-226)*u) #cantidad de visitantes en la hora x
                tuple+=(cvh,)
                for _ in range(cvh):
                    """for de visitantes"""
                    u = next(self.new_u_value)
                    if u <= 0.65:
                        vrr+=1 #cantidad de visitantes que visitan atarcción RR en la hora
                        u = next(self.new_u_value)
                        teminrr=-190*math.log10(u) #TE en minutos en atraccion RR
                        #print(teminrr)
                        tevrr+=teminrr #TE total de visitantes en atracción RR
                    else:
                        vmf+=1 #cantidad de visitantes que visitan atarcción MF en la hora
                        u = next(self.new_u_value)
                        teminmf=-85*math.log10(u) #TE en minutos en atraccion MF
                        tevmf+=teminmf #TE total de visitantes en atracción MF
                self.atractions["RR"] = float("{:.2f}".format(tevrr/vrr))
                self.atractions["MF"] = float("{:.2f}".format(tevmf/vmf))
                
                tuple+=(copy.copy(self.atractions),)
                #print(teh/cvh) # promedio tiempo de espera de la hora
                vrr=0
                vmf=0
                tevmf=0
                tevrr=0
                self.general_table.append(copy.copy(tuple))
                tuple=()
                self.atractions.clear()
                
        #print(tem/cvd) # promedio tiempo de espera mensual   
        
        df = pd.DataFrame(self.general_table)
        df = df.rename(columns={0: "día", 1: "hora", 2: "visitantes", 3: "atracciones"})
        df = df.set_index(["día", "hora", "visitantes"])
        #print(df.loc[df.index.get_level_values("día") == 30])
        return df
    
        