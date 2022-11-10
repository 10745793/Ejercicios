#!/usr/bin/env python3
"""
Autor : Juan Pablo Londoño <10745793@iespenyagolosa.es>
Fecha   : 7/11/22
Propósito: Calcular números consecutivos
"""
n=int(input("Dime un número"))

if n>0:
    for i in range (0,n+1):
        print(i,end=", ")
else:
    for i in range (0,n-1,-1):
        print(i,end=", ")

print()