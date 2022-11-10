#!/usr/bin/env python3
"""
Autor : Juan Pablo Londoño <10745793@iespenyagolosa.es>
Fecha   : 25/10/22
Propósito: Conversión de segundos a minutos
"""

print('Convertidor de segundos a minutos')
segundos = int(input('Escribe una cantidad de segundos: '))
minutos = segundos // 60
segundos_restantes = segundos % 60
print(f'{segundos} segundos son {minutos} minutos y {segundos_restantes} segundos')