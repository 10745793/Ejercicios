#!/usr/bin/env python3
"""
Autor : Juan Pablo Londoño <10745793@iespenyagolosa.es>
Fecha   : 25/10/22
Propósito: Conversión de grados Celsius a Fahrenheit
"""

print('Convertidor de grados Celsius a Fahrenheit')
gradosC = float(input('Escribe una temperatura en grados Celsius: '))
gradosF = 1.8*gradosC + 32
print(f'{gradosC} ºC son {gradosF} ºF')