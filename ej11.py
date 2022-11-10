#!/usr/bin/env python3
"""
Autor : Juan Pablo Londoño <10745793@iespenyagolosa.es>
Fecha   : 9/11/22
Propósito: Calcular mínimo, máximo i media de los números introducidos
"""

numeros = int(input('¿Cuántos valores vas a introducir?: '))
minimo = 0
maximo = 0
suma = 0
media = 0
for i in range (1, numeros+1):
    num = int(input(f'Dime el número {i}: '))
    suma += num
    if num > maximo:
        maximo = num
media = suma / numeros
print(f'La número más pequeño de los introducidos es: {minimo}')
print(f'La número más grande de los introducidos es: {maximo}')
print(f'La media de los números introducidos es: {media}')
