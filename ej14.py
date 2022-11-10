#!/usr/bin/env python3
"""
Autor : Juan Pablo Londoño <10745793@iespenyagolosa.es>
Fecha   : 10/11/22
Propósito: Cambiar las vocales por una vocal
"""

frase = 'tengo una hormiguita en la barriga'
vocal = input('Dime un a vocal: ')
VOCALES = 'aeiou'
frase_nueva = []

for i in range(len(frase)):
    if frase[i] in VOCALES:
        frase_nueva.append(vocal)
    else:
        frase_nueva.append(frase[i])


print(f'La frase ahora es: {frase_nueva}')