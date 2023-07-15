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
        self.tuple_item: tuple = ()
        self.general_table:list=[]
        self.generate = Generadores()
        self.new_u_value: float = self.generate.congruencial_multiplicativo(1317, 5631, 547)

    
    def simular(self):
        # for de dias
        for d in range(30):
            #for de horas
            for h in range(8):
                self.tuple_item+=(d+1,)
                self.tuple_item+=(h+1,)
                u: float = next(self.new_u_value)
                cvh: int = math.trunc(227*(227-226)*u) #cantidad de visitantes en la hora x
                self.tuple_item+=(cvh,)
                for _ in range(cvh):
                    """for de visitantes"""
                    u = next(self.new_u_value)
                    if u <= 0.65:
                        self.vrr+=1 #cantidad de visitantes que visitan atarcción RR en la hora
                        u = next(self.new_u_value)
                        teminrr=-190*math.log10(u) #TE en minutos en atraccion RR
                        #print(teminrr)
                        self.tevrr+=teminrr #TE total de visitantes en atracción RR
                    else:
                        self.vmf+=1 #cantidad de visitantes que visitan atarcción MF en la hora
                        u = next(self.new_u_value)
                        teminmf=-85*math.log10(u) #TE en minutos en atraccion MF
                        self.tevmf+=teminmf #TE total de visitantes en atracción MF
                
                self.tuple_item+=(float("{:.2f}".format(self.tevrr/self.vrr)),)
                self.tuple_item+=(float("{:.2f}".format(self.tevmf/self.vmf)),)
                #print(teh/cvh) # promedio tiempo de espera de la hora
                self.vrr=0
                self.vmf=0
                self.tevmf=0
                self.tevrr=0
                self.general_table.append(copy.copy(self.tuple_item))
                self.tuple_item=()

                
        #print(tem/cvd) # promedio tiempo de espera mensual   
        
        df = pd.DataFrame(self.general_table)
        df = df.rename(columns={0: "dia", 1: "hora", 2: "visitantes", 3:"RR", 4:"MF"})
        return df.loc[df["dia"] == 1].to_dict(orient="records")
        
        