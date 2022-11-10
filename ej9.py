#!/usr/bin/env python3
"""
Autor : Juan Pablo Londoño Arbeláez <10745793@iespenyagolosa.es>
Fecha   : 3/11/2022
Propósito: Escribir una lista de números pares
"""

num1=int(input('dime el numero 1: '))
num2=int(input('dime el numero 2: '))
for i in range(num1,num2):
    if i%2==0:
        print(i,end=', ')