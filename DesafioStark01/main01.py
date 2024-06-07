from funciones_stark01 import *
from data_stark import *
import os

bandera_rta_heroe_masculino_alto = False
bandera_rta_heroe_masculino_bajo = False
bandera_rta_heroe_femenino_alto = False
bandera_rta_heroe_femenino_bajo = False

color_ojos_determinado = False
color_pelos_determinado = False
inteligencia_determinada = False


while True:

    match(menu_stark_01()):
        case "1":
            nombre_masculino(lista_personajes)

        case "2":
            nombre_femenino(lista_personajes)

        case "3":
            heroe_masculino_mas_alto = determinar_mas_alto_masc(lista_personajes)
            bandera_rta_heroe_masculino_alto = True
            print("Se Determino quien es el Masculino mas alto.")

        case "4":
            heroe_femenina_mas_alta = determinar_mas_alto_fem(lista_personajes)
            bandera_rta_heroe_femenino_alto = True
            print("Se Determino quien es la Femenina mas alta.")

        case "5":
            heroe_masculino_mas_bajo = determinar_mas_bajo_masc(lista_personajes)
            bandera_rta_heroe_masculino_bajo = True
            print("Se Determino quien es el Masculino mas bajo.")

        case "6":
            heroe_femenina_mas_baja = determinar_mas_baja_fem(lista_personajes)
            bandera_rta_heroe_femenino_bajo = True
            print("Se Determino quien es la Femenina mas baja.")

        case "7":
            altura_promedio_masculino(lista_personajes)

        case "8":
            altura_promedio_femenino(lista_personajes)

        case "9":
            if bandera_rta_heroe_femenino_alto and bandera_rta_heroe_femenino_bajo and bandera_rta_heroe_masculino_alto and bandera_rta_heroe_masculino_bajo:
                informar_altos_bajos_fems_masc(heroe_masculino_mas_alto , heroe_masculino_mas_bajo , heroe_femenina_mas_alta , heroe_femenina_mas_baja)
            else:
                print("Para Mostrar quienes son los mas altos y los mas bajos antes debes determinarlos (opcion 3(alto),4(alta),5(bajo),6(baja))")
        
        case "10":
            determinar_cant_color_ojos(lista_personajes)
            color_ojos_determinado = True
            print("Se ha determinado la cantidad de colores de ojos")

        case "11":
            determinar_cant_color_pelos(lista_personajes)
            color_pelos_determinado = True
            print("Se ha determinado la cantidad de colores de pelos")

        case "12":
            determinar_cant_inteligencias(lista_personajes)
            inteligencia_determinada = True
            print("Se ha determinado la cantidad de inteligencias")

        case "13":
            if color_ojos_determinado:
                listar_color_ojos(lista_personajes)
            else:
                print("Para listar por color de ojos primero debes determinarlo (opcion 10)")

        case "14":
            if color_pelos_determinado:
                listar_color_pelo(lista_personajes)
            else:
                print("Para listar por color de pelos primero debes determinarlo (opcion 11)")


        case "15":
            if inteligencia_determinada:
                listar_inteligencia(lista_personajes)
            else:
                print("Para listar por inteligencias primero debes determinarlo (opcion 12)")

        case "16":
            if salida_menu() == True:
                break

        case _:
            print("Ingrese una opcion correcta.")

    os.system("Pause")