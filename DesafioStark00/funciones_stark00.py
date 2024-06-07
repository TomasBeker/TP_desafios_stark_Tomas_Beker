from data_stark import *
import os


#Punto B.
def nombre_heroe():
  """nombre_heroe: es una funcion que recorre la lista y printea el nombre de cada heroe.
  """  
  for super_heroe in lista_personajes:
    print(super_heroe["nombre"])

#Punto C.
def nombre_altura_heroes():
  """nombre_altura_heroe: es una funcion que recorre la lista y printea el nombre de cada heroe y su altura.
  """

  for super_heroe in lista_personajes:
    print(f"{super_heroe['nombre']} y su altura es {super_heroe['altura']}")

#Punto D.
def heroe_altura_maxima()->str:
  """heroe_altura_maxima: Recorre la lista y busca al heroe mas alto

  Returns:
      str: retorna el nombre del heroe mas alto
  """

  bandera_altura_maxima = True
  altura_mas_alta = None

  for super_heroe in lista_personajes:
    if (bandera_altura_maxima or float(super_heroe["altura"]) > altura_mas_alta):
      bandera_altura_maxima = False
      altura_mas_alta = float(super_heroe["altura"])
      super_heroe_alto = super_heroe["nombre"]

  for super_heroe in lista_personajes:
    if float(super_heroe["altura"]) == altura_mas_alta:
      super_heroe_alto = super_heroe["nombre"]
  
  return super_heroe_alto

#Punto E.
def heroe_altura_minima()->str:
  """heroe_altura_minima: Recorre la lista y busca al heroe mas bajo

  Returns:
      str: retorna el nombre del heroe mas bajo
  """

  altura_mas_baja = None
  bandera_altura_minima = True

  for super_heroe in lista_personajes:
    if bandera_altura_minima or float(super_heroe["altura"]) < altura_mas_baja:
      bandera_altura_minima = False
      altura_mas_baja = float(super_heroe["altura"])
      super_heroe_bajo = super_heroe["nombre"]

  for super_heroe in lista_personajes:
    if float(super_heroe["altura"]) == altura_mas_baja:
      super_heroe_bajo = super_heroe["nombre"]

  return super_heroe_bajo

#Punto F.
def promedio_de_alturas()->float:
  """promedio_de_alturas: Recorre la lista con un acumulador de alturas para promediar las alturas.
   
  Returns:
      float: retorna el promedio de las alturas.
  """

  acumulador_altura = 0
  for super_heroe in lista_personajes:
    acumulador_altura = acumulador_altura + float(super_heroe["altura"])
  
  promedio_alturas = acumulador_altura / len(lista_personajes)

  return promedio_alturas


#Punto H.
def heroe_peso_maximo_minimo():
  """heroe_peso_maximo_minimo: Informa cual es el Nombre del superhéroe asociado a la altura mas baja y la mas alta
  """

  bandera_peso_maximo = True
  peso_mas_pesado = None

  bandera_peso_minimo = True
  peso_mas_liviano = None

  for super_heroe in lista_personajes:
    if (bandera_peso_maximo or float(super_heroe["peso"]) > peso_mas_pesado):
      bandera_peso_maximo = False
      peso_mas_pesado = float(super_heroe["peso"])
      super_heroe_pesado = super_heroe["nombre"]

  for super_heroe in lista_personajes:
    if float(super_heroe["peso"]) == peso_mas_pesado:
      super_heroe_pesado = super_heroe["nombre"]

  for super_heroe in lista_personajes:
    if bandera_peso_minimo or float(super_heroe["peso"]) < peso_mas_liviano:
      bandera_peso_minimo = False
      peso_mas_liviano = float(super_heroe["peso"])
      super_heroe_liviano = super_heroe["nombre"]

  for super_heroe in lista_personajes:
    if float(super_heroe["peso"]) == peso_mas_liviano:
      super_heroe_liviano = super_heroe["nombre"]
  
  print(f"El SuperHéroe mas pesado es: {super_heroe_pesado} y el SuperHéroe mas liviano es: {super_heroe_liviano}")


#Punto J.
def menu_stark_00():
  """Menu principal del programa.

  Returns:
      str: retorna la opcion elegida.
    """
  import os

  while True:
    os.system("cls")
    print("*********                MENU DE OPCIONES                 *********")
    print("-------------------------------------------------------------------")
    print("1. Nombre de los SuperHéroes.")
    print("2. Nombre y altura de los SuperHéroes.")
    print("3. Determinar cual es el SuperHéroes mas alto.")
    print("4. Determinar cual es el SuperHéroes mas bajo.")
    print("5. Determinar la altura promedio de los SuperHéroes.")
    print("6. Informar cual es el Nombre del SuperHéroe mas bajo y mas alto.")
    print("7. Informar cual es el SuperHéroe más pesado y el mas liviano.")
    print("8. Salir.")

    opcion = input("Ingrese opcion: ")
    
    return opcion



def salida_menu()->bool:
  """salida_menu

  Returns:
      bool: Retorna la opcion que elija el usuario
            s = True    Con lo que saldriamos del programa.
            n = False   Con lo que permaneceriamos dentro del programa.

  """
  salida = input("Desea salir?(s o n): ")   
  if salida.lower() == "s":
    return True
  else:
    return False