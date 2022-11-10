#!/usr/bin/env python3
"""
Autor : Juan Pablo Londoño <10745793@iespenyagolosa.es>
Fecha   : 9/11/22
Propósito: 
"""

num = int(input('Dime un número: '))
factorial = 1

for i in range(1, num+1):
    factorial *= i

print(f'El factorial de {num} es: {factorial}')
