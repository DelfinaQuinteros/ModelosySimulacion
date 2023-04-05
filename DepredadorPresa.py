import numpy as np


def get_variacion_presas(presas, predadores, tasa_natalidad_lieb, tasa_mortandad_lieb, dt):
    return ((tasa_natalidad_lieb * presas) - (tasa_mortandad_lieb * presas * predadores)) * dt


def get_variacion_predadores(presas, predadores, tasa_mortandad_zorr, tasa_natalidad_zorr, dt):
    return ((tasa_natalidad_zorr * presas * predadores) - (tasa_mortandad_zorr * predadores)) * dt


def simulacion(dt, tiempo_inicial, presas_iniciales, predadores_iniciales, tasa_natalidad_lieb, tasa_mortandad_lieb,
               tasa_mortandad_zorr, tasa_natalidad_zorr, cant_muestras):
    presas_arr = [presas_iniciales]
    predadores_arr = [predadores_iniciales]
    tiempo_arr = [tiempo_inicial]

    tiempo = tiempo_inicial
    presas = presas_iniciales
    predadores = predadores_iniciales

    for i in range(cant_muestras - 1):
        tiempo = tiempo + dt
        presas += get_variacion_presas(presas, predadores, tasa_natalidad_lieb, tasa_mortandad_lieb, dt)
        predadores += get_variacion_predadores(presas, predadores, tasa_mortandad_zorr, tasa_natalidad_zorr, dt)

        presas_arr.append(presas)
        predadores_arr.append(predadores)
        tiempo_arr.append(tiempo)

    return np.array(presas_arr), np.array(predadores_arr), np.array(tiempo_arr)

