import simpy
import random

class SistemaColas:
    def __init__(self, env):
        self.env = env
        self.servidor = simpy.Resource(env, capacity=1)
        self.tiempo_total_espera = 0
        self.clientes_atendidos = 0

    def llegada_cliente(self):
        with self.servidor.request() as req:
            yield req

            tiempo_espera = random.expovariate(1.0 / 2)  # Distribución exponencial con tasa 2
            yield self.env.timeout(tiempo_espera)
            self.tiempo_total_espera += tiempo_espera
            self.clientes_atendidos += 1

def ejecutar_simulacion():
    env = simpy.Environment()
    sistema = SistemaColas(env)
    env.process(sistema.llegada_cliente())

    env.run(until=10)  # Tiempo de simulación

    tiempo_promedio_espera = sistema.tiempo_total_espera / sistema.clientes_atendidos
    print("Tiempo promedio de espera:", tiempo_promedio_espera)

ejecutar_simulacion()
