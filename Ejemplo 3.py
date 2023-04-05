import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from DepredadorPresa import simulacion

# Caso con 700 liebres y 35 zorros
liebres = 700
zorros = 35
semanas = 600
tiempo_inicial = 1
variacion_tiempo = 1

tasa_natalidad_lieb = 0.06
tasa_mortandad_lieb = 0.002
tasa_mortandad_zorr = 0.10
tasa_natalidad_zorr = 0.0003

liebres_arr, zorros_arr, tiempo_arr = simulacion(variacion_tiempo,
                                                 tiempo_inicial,
                                                 liebres,
                                                 zorros,
                                                 tasa_natalidad_lieb=tasa_natalidad_lieb,
                                                 tasa_mortandad_lieb=tasa_mortandad_lieb,
                                                 tasa_mortandad_zorr=tasa_mortandad_zorr,
                                                 tasa_natalidad_zorr=tasa_natalidad_zorr,
                                                 cant_muestras=semanas)
# Grafica 1
plt.close()
colors = cm.rainbow(np.linspace(0, 1, 2))

plt.plot(tiempo_arr,
         liebres_arr,
         c=colors[0],
         label="Liebres")
plt.plot(tiempo_arr,
         zorros_arr,
         c=colors[1],
         label="Zorros")
plt.title('Comparando la densidad poblacional de liebres y zorros.')
plt.xlabel('Semanas')
plt.xticks(rotation='90')
plt.legend()
plt.ylabel('Densidad poblacional')

plt.show()

# Grafica 2
plt.close()
plt.plot(zorros_arr,
         liebres_arr,
         c=colors[0])
plt.title('Diagrama de fases de las poblaciones de liebres y de zorros.')
plt.xlabel('Zorros')
plt.xticks(rotation='90')
plt.ylabel('Liebres')

plt.show()
