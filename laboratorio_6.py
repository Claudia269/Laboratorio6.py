# -*- coding: utf-8 -*-
"""Laboratorio 6.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/14ymn2Mqrm2pi64_jwiDDl5grGl1RP0oN
"""

##Programa 1

# Paso 1: Elegir el tipo de té
tipo_te = input("1. Escoge el tipo de té (ejemplo: té negro, té verde, té blanco, té de hierbas): ")
cantidad_tazas = int(input("   ¿Cuántas tazas deseas preparar? "))

# Validación de la cantidad de té por taza
cantidad_te = int(input("   Ingresa la cantidad de té (en cucharaditas o bolsitas) por taza: "))
if cantidad_te > 1:
    print("   Nota: Usa solo una cucharadita o bolsita de té por cada taza.")
    confirmacion = input("   Escribe 'sí' para confirmar que entendiste y deseas continuar: ")
    while confirmacion != "si":
        confirmacion = input("   Por favor, escribe 'sí' para continuar: ")
print("   La cantidad de té es correcta.\n")

# Paso 2: Calentar el agua a la temperatura adecuada
if tipo_te == "té verde" or tipo_te == "té blanco":
    print("\n2. Calienta el agua a 70-80 °C (evita hervir completamente).")
else:
    print("\n2. Calienta el agua a 90-100 °C. Puedes llevarla a hervir.")

# Paso 3: Colocar el té en la taza o tetera
print("\n3. Coloca el té en la taza o tetera.")
if tipo_te == "té suelto":
    print("   Usa un infusor o colador de té para el té suelto.")
else:
    print("   Si usas una bolsita, simplemente colócala en la taza.")

# Paso 4: Verter el agua caliente
print("\n4. Vierte el agua caliente sobre el té en la taza o tetera.")

# Paso 5: Dejar reposar el té por el tiempo recomendado
if tipo_te == "té verde":
    print("\n5. Deja reposar el té durante 2-3 minutos.")
elif tipo_te == "té negro":
    print("\n5. Deja reposar el té durante 3-5 minutos.")
elif tipo_te == "té de hierbas":
    print("\n5. Deja reposar el té durante 5-7 minutos.")
else:
    print("\n5. Deja reposar el té durante 3-5 minutos (tiempo estándar).")

# Paso 6: Retirar el té
print("\n6. Retira el té.")
if tipo_te == "té suelto":
    print("   Retira el infusor o colador.")
else:
    print("   Retira la bolsita y exprímela suavemente.")

# Paso 7: Personalizar el té (opcional)
personalizar = input("\n7. ¿Deseas personalizar el té con azúcar, miel, leche, limón, etc.? (sí/no): ")
if personalizar == "si":
    print("   Puedes agregar tus ingredientes favoritos al gusto.")

# Paso 8: Disfrutar el té
print("\n8. ¡Disfruta tu té! Si prefieres que se enfríe un poco, espera unos minutos antes de probarlo.")

## Programa 2
# Mensaje de informacion Programa que calcula el promedio de notas
print("Programa que cálcula el promedio de notas.")

# Pedir al usuario la cantidad de notas
cantidad_notas = int(input("¿Cuántas notas deseas promediar? "))

# Crear una lista para almacenar las notas
notas = []

# Pedir al usuario cada nota y validar que sea positiva
for i in range(cantidad_notas):
    while True:  # Ciclo para validar la nota
        nota = float(input(f"Ingrese la nota {i + 1}: "))
        if nota >= 0:
            notas.append(nota)
            break  # Sale del ciclo si la nota es válida
        else:
            print("Debe ser un dato positivo. Intente de nuevo.")

# Calcular el promedio
promedio = sum(notas) / cantidad_notas

# Mostrar el promedio
print(f"El promedio de las notas es: {promedio}")

##Programa 3
print("Programa que calcula si un número es par o impar.")

continuar = 's'

while continuar == 's':
    numero = int(input("Ingresa un número: "))

    if numero % 2 == 0:
        print(f"{numero} es par")
    else:
        print(f"{numero} es impar")

    continuar = input("¿Deseas validar otro número? (s/n): ")

    # Comprueba si el usuario ha ingresado s o n
    if continuar != 's' and continuar != 'n':
        print("Entrada inválida. Por favor ingresa 's' o 'n'.")
        continuar = input("¿Deseas validar otro número? (s/n): ")

## Programa 4
print("Programa que inprime los números del 1 al 5", end=" ")
print("y valida si es par o impar.")
for numero in range(1, 6):  # Bucle del 1 al 5
    if numero % 2 == 0:
        print(f"{numero} es par")
    else:
        print(f"{numero} es impar")

## Programa 5
# temp_celsius = 0.0  #Creación de la variable

# print("Hola, este programa convierte grados celsius a grados Fahrenheit") #Avisamos el objetivo del programa

dato_usuario = input("Ingrese los grados en celsius en números: ") #Solicitamos al usuario los grados en celsius

temp_celsius = float(dato_usuario) #Validación de la información

grados_Fahrenheit = (temp_celsius * 9/5) + 32 #Aplicamos la formula de conversión de grados

print('Los grados Fahrenheit son: ', grados_Fahrenheit) #Imprimimos el resultado

## Programa 6
print("")
print("Este programa cuenta el número de vocales que se encuentran", end= " ")
print("en el texto ingresado ")
texto = input("Ingresa una cadena de texto: ")
vocales = "aeiouAEIOU"  # Definir las vocales minusculas y mayusculas
contador_vocales = 0

for letra in texto:
    if letra in vocales:
        contador_vocales += 1

print(f"La cadena '{texto}' tiene {contador_vocales} vocales.")

##Programa 7

continuar = 's'
print("Programa que calcual el promedio de un número.")
while continuar == 's':
    numero = int(input("Ingresa un número: "))

    # Validación de entrada
    if numero <= 0:
        print("El número debe ser positivo. Inténtalo de nuevo.")
        continue  # Volver al principio del bucle

    factorial = 1
    contador = 1

    while contador <= numero:
        factorial *= contador
        contador += 1

    print(f"El factorial de {numero} es {factorial}")

    continuar = input("¿Deseas calcular el factorial de otro número? (s/n): ")