#Mi tercer programa dia 3
#CarReel
#Fecha: 14/02/2024


#Analizador de texto
lista1 = input("Inserta un texto extenso: ")
lista2 = []

#Convertir el texto a minusculas
lista1 = lista1.lower()

#Añadimos 3 letras a una lista
print("CANTIDAD DE LETRAS")
lista2.append(input("Ingresa la primera letra: ").lower())
lista2.append(input("Ingresa la segunda letra: ").lower())
lista2.append(input("Ingresa la tercera letra: ").lower())

print("\n")
#Problemas
"""1-Que cantidad de letras aparecen el texto extenso escrito por el usuario?"""
cantidad_letras1 = lista1.count(lista2[0])
cantidad_letras2 = lista1.count(lista2[1])
cantidad_letras3 = lista1.count(lista2[2])
print(f"Solucion 1: Hemos encontrado la letra {lista2[0]} repetidas {cantidad_letras1} veces")
print(f"Solucion 1: Hemos encontrado la letra {lista2[1]} repetidas {cantidad_letras2} veces")
print(f"Solucion 1: Hemos encontrado la letra {lista2[2]} repetidas {cantidad_letras3} veces")

"""2-Cuantas palabras aparecen en el texto extenso"""
print("CANTIDAD DE PALABRAS")
palabras = lista1.split()
print(f"Solucion 2: La cantidad total de palabras en el texto son:{len(palabras)}")

"""3-Debes indicar la primera letra del texto extenso y la ultima
letra del texto extenso)"""
print(f"Solucion 3: La primera letra del texto extenso es : {lista1[0]} y la letra de fin es:{lista1[-1]}")

"""4-Invertir el orden del texto"""
print("TEXTO INVERTIDO")
palabras.reverse()
#Metodo join permite unir
lista1_invertido = ' '.join(palabras)
print(f"Solucion 4: La inversion del texto extenso se muestra asi: {lista1_invertido}")

"""5-Existe la palabra python en el texto extenso"""
print("BUSCANDO LA PALABRA PYTHON")
buscar_python = 'python' in lista1
dict = {True:"si","False":"no"}
print(f"Solucion 5: La palabra python se encuentra dentro del texto? {dict[buscar_python]}")
