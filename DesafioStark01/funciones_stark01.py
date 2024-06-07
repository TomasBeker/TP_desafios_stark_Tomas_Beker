from data_stark import *
import os

def menu_stark_01()->str:
  """Menu principal del programa.

  Returns:
      str: retorna la opcion elegida.
    """
  import os

  while True:
    os.system("cls")
    print("*********                MENU DE OPCIONES                 *********")
    print("-------------------------------------------------------------------")
    print("1. Nombre de los SuperHéroes Masculinos.")
    print("2. Nombre de los SuperHéroes Femeninos.")
    print("3. Determinar cuál es el superhéroe más alto de género M.")
    print("4. Determinar cuál es el superhéroe más alto de género F.")
    print("5. Determinar cuál es el superhéroe más bajo de género M.")
    print("6. Determinar cuál es el superhéroe más bajo de género F.")
    print("7. Determinar la altura promedio de los superhéroes de género M.")
    print("8. Determinar la altura promedio de los superhéroes de género F.")
    print("9. Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (ítems 3 a 6).")
    print("10. Determinar cuántos superhéroes tienen cada tipo de color de ojos.")
    print("11. Determinar cuántos superhéroes tienen cada tipo de color de pelo.")
    print("12. Determinar cuántos superhéroes tienen cada tipo de inteligencia")
    print("13. Listar todos los superhéroes agrupados por color de ojos.")
    print("14. Listar todos los superhéroes agrupados por color de pelo.")
    print("15. Listar todos los superhéroes agrupados por tipo de inteligencia.")
    print("16. Salir.")

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

#Punto A 01.
def nombre_masculino(lista):
  """nombre_masculino: recorre toda la lista y printea los nombres de los heroes Masculinos.

    Args:
        lista (list): lista de personajes.
    """
  for item in lista:
    if item["genero"] == "M":
      print(item["nombre"])

#Punto B 01.
def nombre_femenino(lista):
  """nombre_femenino: recorre toda la lista y printea los nombres de las heroes Femeninos.

    Args:
        lista (list): lista de personajes.
    """      
  for item in lista:
    if item["genero"] == "F":
      print(item["nombre"])

  
#Punto C 01.
def determinar_mas_alto_masc(lista)->str:
  """determinar_mas_alto_masc: Recorre la lista para determinar que masculino es el mas alto de la lista. 

    Args:
        lista (list): lista de personajes.

    Returns:
        str: Persona masculina mas alta.
    """
  altura_mas_alta_m = None
  persona_mas_alta_m = None
  bandera_altura_max_m = True

  for item in lista:
    if item["genero"] == "M":
      if bandera_altura_max_m or float(item["altura"]) > altura_mas_alta_m:
        bandera_altura_max_m = False
        altura_mas_alta_m = float(item["altura"])
        persona_mas_alta_m = item["nombre"]

  for item in lista:
    if item["genero"] == "M":
      if float(item["altura"]) > altura_mas_alta_m:
        persona_mas_alta_m = item["nombre"] 

  
  return persona_mas_alta_m

#Punto D 01.
def determinar_mas_alto_fem(lista)->str:
  """determinar_mas_alto_fem: Recorre la lista para determinar que femenina es la mas alta de la lista. 

    Args:
        lista (list): lista de personajes.

    Returns:
        str: Persona femenina mas alta.
    """
  altura_mas_alta_f = None
  persona_mas_alta_f = None
  bandera_altura_max_f = True

  for item in lista:
    if item["genero"] == "F":
      if bandera_altura_max_f or float(item["altura"]) > altura_mas_alta_f:
        bandera_altura_max_f = False
        altura_mas_alta_f = float(item["altura"])
        persona_mas_alta_f = item["nombre"]
    


  return persona_mas_alta_f
  
    
    

#Punto E 01.
def determinar_mas_bajo_masc(lista)->str:
  """determinar_mas_bajo_masc: Recorre la lista para determinar que Masculino es el mas bajo de la lista.

    Args:
        lista (list): lista de personajes.

    Returns:
        str: Persona Masculina mas baja.
    """

  altura_mas_baja_m = None
  persona_mas_baja_m = None
  bandera_altura_min_m = True

  for item in lista:
    if item["genero"] == "M":
      if bandera_altura_min_m or float(item["altura"]) < altura_mas_baja_m:
        bandera_altura_min_m = False
        altura_mas_baja_m = float(item["altura"])
        persona_mas_baja_m = item["nombre"]

  
  return persona_mas_baja_m

#Punto F 01.
def determinar_mas_baja_fem(lista)->str:
  """determinar_mas_baja_fem: Recorre la lista para determinar que Femenina es la mas baja de la lista.

    Args:
        lista (list): lista de personajes.

    Returns:
        str: Persona Femenina mas baja.
    """
  altura_mas_baja_f = None
  persona_mas_baja_f = None
  bandera_altura_min_f = True

  for item in lista:
    if item["genero"] == "F":
      if bandera_altura_min_f or float(item["altura"]) < altura_mas_baja_f:
        bandera_altura_min_f = False
        altura_mas_baja_f = float(item["altura"])
        persona_mas_baja_f = item["nombre"]

  
  return persona_mas_baja_f
    

#Punto G 01.
def altura_promedio_masculino(lista):
  """altura_promedio_masculino: Recorre la lista de personajes filtra a los masculinos para saber cual es el promedio
  de alturas entre los masculinos, pero no lo muestra.

    Args:
        lista (list): Lista de personajes.
    """
  contador_masculino = 0
  acumulador_alturas = 0
  for item in lista:
    if item["genero"] == "M":
      contador_masculino += 1
      
      acumulador_alturas = float(item["altura"]) + acumulador_alturas 
  
  promedio_altura_masculina = acumulador_alturas / contador_masculino

  #print(f"El promedio de altura masculina es: {promedio_altura_masculina}")
  print("Se determino el promedio de altura masculina.")

#Punto H 01.
def altura_promedio_femenino(lista):
  """altura_promedio_femenino: Recorre la lista de personajes filtra a las femeninas para saber cual es el promedio 
  de alturas entre las femeninas, pero no lo muestra.

    Args:
        lista (list): Lista de personajes.
    """
  contador_fememino = 0
  acumulador_alturas = 0
  for item in lista:
    if item["genero"] == "F":
      contador_fememino += 1
      acumulador_alturas = float(item["altura"]) + acumulador_alturas 
  
  promedio_altura_femenina = acumulador_alturas / contador_fememino

  #print(f"El promedio de altura femenina es: {promedio_altura_femenina}")
  print("Se determino el promedio de altura femenino.")


#Punto I 01.
def informar_altos_bajos_fems_masc(alto, bajo, alta, baja):
  """informar_altos_bajos_fems_masc: Printea al masculino mas alto y al mas bajo, tambien printea a la feme
    nina mas alta y la mas baja.

    Args:
        alto (str): Masculino mas alto.
        bajo (str): Masculino mas bajo.
        alta (str): Femenina mas alta.
        baja (str): Femenina mas baja.
    """
  print(f"El mas alto es: {alto}")
  print(f"El mas bajo es: {bajo}")
  print(f"La mas alta es: {alta}")
  print(f"La mas baja es: {baja}")

#Punto J 01.
def determinar_cant_color_ojos(lista):
  """determinar_cant_color_ojos: Con contadores y recorriendo la lista determina la cantidad de color de ojos de los heroes.

    Args:
        lista (list): Lista de personajes.
    """
  contador_blue = 0
  contador_red = 0
  contador_yellow = 0
  contador_yellow_iris = 0
  contador_green = 0
  contador_silver = 0
  contador_hazel = 0
  contador_brown = 0

  for item in lista:
    
    item["color_ojos"] = item["color_ojos"].lower()
    match(item["color_ojos"]):
      case "blue":
        contador_blue += 1
      case "red":
        contador_red += 1
      case "yellow":
        contador_yellow += 1
      case "yellow (without irises)":
        contador_yellow_iris += 1
      case "green":
        contador_green += 1
      case "silver":
        contador_silver += 1
      case "hazel":
        contador_hazel += 1
      case "brown":
        contador_brown += 1 

#Punto K 01.
def determinar_cant_color_pelos(lista): 
  """determinar_cant_color_pelos: Con contadores y recorriendo la lista determina la cantidad de color de pelos de los heroes.

    Args:
        lista (list): Lista de personajes.
    """
  contador_yellow = 0
  contador_brown = 0
  contador_black = 0
  contador_auburn = 0
  contador_red_orange = 0
  contador_white = 0
  contador_blond = 0
  contador_green = 0
  contador_red = 0
  contador_brown_white = 0 
  contador_pelados = 0

  for item in lista:
    
    item["color_pelo"] = item["color_pelo"].lower()
    match(item["color_pelo"]):
      case "yellow":
        contador_yellow += 1
      case "brown":
        contador_brown += 1 
      case "black":
        contador_black += 1
      case "auburn":
        contador_auburn += 1
      case "red / orange":
        contador_red_orange += 1
      case "white":
        contador_white += 1
      case "blond":
        contador_blond += 1
      case "green":
        contador_green += 1
      case "red":
        contador_red += 1
      case "brown / white":
        contador_brown_white += 1
      case _:
        contador_pelados += 1

#Punto L 01.
def determinar_cant_inteligencias(lista):
  """determinar_cant_inteligencias: Con contadores y recorriendo la lista determina la cantidad de inteligencias de los heroes.

    Args:
        lista (list): Lista de personajes.
    """
  contador_good = 0
  contador_average = 0
  contador_sin_inteligencia = 0
  contador_high = 0

  for item in lista:

    if item["inteligencia"] == "":
      item["inteligencia"] = item["inteligencia"].replace("", "No tiene")

    item["inteligencia"] = item["inteligencia"].lower()
    match(item["inteligencia"]):

      case "good":
        contador_good += 1
      case "average":
        contador_average += 1
      case "high":
        contador_high += 1
      case "no tiene":
        contador_sin_inteligencia += 1


def esta_en_lista(lista,key)->bool:
  """esta_en_lista: Verifica si un elemento está presente en una lista.

    Args:
        lista (list): lista de personajes.
        key (str): La clave de valor deseada.

    Returns:
        bool: True si el elemento está en la lista, False en caso contrario.
    """
  esta = False

  for elemento in lista:
      if elemento == key:
          esta = True
          break
  return esta


#Punto N 01.
def listar_color_pelo(lista):
  """listar_color_pelo: Printea una lista de personas agrupadas por el color de pelo.

    Args:
        lista (list): Lista de personajes.
    """
  lista_nueva = []
  colores = []

  for item in lista:
    lista_nueva.append(item)

  for item in lista_nueva:
    if not esta_en_lista(colores, item["color_pelo"]):
      colores.append(item["color_pelo"])

  for color in colores:
    print("color: " + color)
    for item in lista_nueva:
      if item["color_pelo"] == color:
        print(item["nombre"], item["color_pelo"])
  
    print("------------------------------------------")


#Punto M 01. 
def listar_color_ojos(lista):
  """listar_color_ojos: Printea una lista de personas agrupadas por el color de ojos.

    Args:
        lista (list): Lista de personajes.
    """
  lista_nueva = []
  colores = []

  for item in lista:
    lista_nueva.append(item)

  for item in lista_nueva:
    if not esta_en_lista(colores, item["color_ojos"]):
      colores.append(item["color_ojos"])

  for color in colores:
    print("color: " + color)
    for item in lista_nueva:
      if item["color_ojos"] == color:
        
        print(item["nombre"], item["color_ojos"])
  
    print("------------------------------------------")

def listar_inteligencia(lista):
  """listar_inteligencia: Printea una lista de personas agrupadas por inteligencia. 

    Args:
        lista (list): Lista de personajes.
    """
  lista_nueva = []
  inteligencias = []

  for item in lista:
    lista_nueva.append(item)


  for item in lista_nueva:
    if not esta_en_lista(inteligencias, item["inteligencia"]):
      inteligencias.append(item["inteligencia"])

  for inteligencia in inteligencias:
    print("inteligencia: " + inteligencia)
    for item in lista_nueva:
      if item["inteligencia"] == inteligencia:
        print(item["nombre"], item["inteligencia"])
  
    print("------------------------------------------")
