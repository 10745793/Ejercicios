#!/usr/bin/env python3
"""
Autor : Juan Pablo Londoño <10745793@iespenyagolosa.es>
Fecha   : 10/11/22
Propósito: Dibujar un rectángulo
"""

anchura = int(input('Anchura del rectángulo: '))
altura = int(input('Anltura del rectángulo: '))

for i in range(altura):
    for j in range(anchura):
        print('*', end = '')
    print()