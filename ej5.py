#!/usr/bin/env python3
"""
Autor : Juan Pablo Londoño <10745793@iespenyagolosa.es>
Fecha   : 31/10/22
Propósito: Cálculo de área
"""

print('Elige una figura geométrica: ')
print('a) Triángulo')
print('b) Círculo')
figura = input('Qué figura quieres calcular (escribe T o C)? ').upper()
if figura == 'T':
    base = float(input('Escribe la base: '))
    altura = float(input('Escribe la altura: '))
    area = base*altura/2
    print(f'Un triángulo de base {base} y altura {altura} tiene un área de {area}')    
elif figura == 'C':
    radio = float(input('Escribe el radio: '))
    area = 3.14*radio**2
    print(f'Un círculo de radio {radio} tiene un área de {area}')