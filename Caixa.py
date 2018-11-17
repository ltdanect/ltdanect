#-------------------------------------------------------------------------------
# Name:        CAIXA ELETRONICO PYTHON
# Purpose:
# Created:     17/11/2018
# Copyright:   (c) 7569223 2018
# EDITOR:     PYSCRIPTER

#para os valores comuns (ex.2,5,20,25,40,50,100,400,440,etc.)
#e combinações (2,5,10,20,50,100)

#-------------------------------------------------------------------------------

def caixa_eletronico(valor):
    d = {}
    nota2 = 0
    nota5 = 0


    nota100 = int (valor / 100)
    val = valor % 100
    nota50 = int(val / 50)
    val = val % 50
    nota20 = int(val / 20)
    val = val % 20
    nota10 = int(val / 10)

    if valor % 10 == 1 and valor != 1:
        nota10 -= 1
        nota2 += 3
        nota5 += 1
    if valor % 10 == 2:
        nota2 += 1
    if valor % 10 == 3 and valor != 3:
        nota10 -= 1
        nota2 += 4
        nota5 += 1

    if valor % 100 == 1 and valor != 1:
        nota100 -= 1
        nota50 += 1
        nota20 += 2

    if valor % 100 == 3 and valor != 3:
        nota100 -= 1
        nota50 += 1
        nota20 += 2
    if valor % 10 == 4:
        nota2 += 2
    if valor % 10 == 5:
        nota5 += 1
    if valor % 10 == 6:
        nota2 += 3
    if valor % 10 == 7:
        nota2 += 1
        nota5 += 1
    if valor % 10 == 8:
        nota2 += 4
    if valor % 10 == 9:
        nota2 += 2
        nota5 += 1
    if valor % 10 == 10:
        nota10 += 1
    if nota100 > 0:
        d[100] = nota100
    if nota50 > 0:
        d[50] = nota50
    if nota20 > 0:
        d[20] = nota20
    if nota10 > 0:
        d[10] = nota10
    if nota5 > 0:
        d[5] = nota5

    if nota2 > 0:
        d[2] = nota2

    return d


valor = int (input())
d = caixa_eletronico(valor)
print (d)
