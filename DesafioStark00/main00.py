from data_stark import *
from funciones_stark00 import *
import os


bandera_rta_heroe_alto = False
bandera_rta_heroe_bajo = False

while True:

    match(menu_stark_00()):

        case "1":
            nombre_heroe()
        case "2":
            nombre_altura_heroes()
        case "3":
            resultado_heroe_alto = heroe_altura_maxima()
            bandera_rta_heroe_alto = True
            print("Se Determino quien es el mas alto.")
        case "4":
            resultado_heroe_bajo = heroe_altura_minima()
            bandera_rta_heroe_bajo = True
            print("Se Determino quien es el mas bajo.")
        case "5":
            promedio_de_alturas()
            print("Se Determino el promedio de la altura.")
        case "6":
            if bandera_rta_heroe_alto and bandera_rta_heroe_bajo:
                #promedio_de_alturas()
                print(f"El super heroe mas alto es: {resultado_heroe_alto} y el super heroe mas bajo es: {resultado_heroe_bajo}.")
            else:
                print("Para elegir la opcion 5 tenes que haber elegido antes la 3 y 4.")
        case "7":
            heroe_peso_maximo_minimo()
        case "8":
            if salida_menu() == True:
                break
        case _:
            print("Ingrese una opcion correcta.")

    os.system("Pause")
