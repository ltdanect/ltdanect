#-------------------------------------------------------------------------------
# Name:        CAIXA ELETRONICO PYTHON
# Created:     17/11/2018
# Copyright:   (c) 7569223 2018
# EDITOR:     PYSCRIPTER

#para os valores comuns (ex.2,5,20,25,40,50,100,400,440,etc.)
#e combinações (2,5,10,20,50,100)

#-------------------------------------------------------------------------------

def caixa_eletronico(valor):
    d = {}
    valor = int (valor)

    nota100 = int  (valor / 100)
    val= valor % 100
    nota50 = int ( val / 50)
    val = val % 50
    nota20 = int( val / 20)
    val = val % 20
    nota10 = int( val / 10)
    val = val % 10
    nota5 = int ( val / 5)
    val = val % 5
    nota2 = int (val / 2)

    if valor % 10 == 1:
        if valor < 100:
            if valor == 11:
                nota10 -= 1
                nota5 += 1
                nota2 += 3

            elif valor == 21:
                nota20 -= 1
                nota10 += 1
                nota5 += 1
                nota2 += 3

            elif valor == 31:
                nota10 -= 1
                nota5 += 1
                nota2 += 3
            elif valor == 41:
                nota20 -= 1
                nota10 += 1
                nota5 += 1
                nota2 += 3

            elif valor == 51:
                nota50 -= 1
                nota20 += 2
                nota5 += 1
                nota2 += 3
            elif valor == 61:
                nota10 -= 1
                nota5 += 1
                nota2 += 3
            elif valor == 71:
                nota20 -= 1
                nota10 += 1
                nota5 += 1
                nota2 += 3

            elif valor == 81:
                nota10 -= 1
                nota5 += 1
                nota2 += 3

            elif valor == 91:
                nota20 -= 1
                nota10 += 1
                nota5 += 1
                nota2 += 3

        else:
            if valor % 100 < 10:
                nota100 -= 1
                nota50 += 1
                nota20 += 2
                nota5 += 1
                nota2 += 3
            else:
                 if valor % 100 == 11:
                    nota10 -= 1
                    nota5 += 1
                    nota2 += 3

                 elif valor % 100  == 21:
                    nota20 -= 1
                    nota10 += 1
                    nota5 += 1
                    nota2 += 3

                 elif valor % 100  == 31:
                    nota10 -= 1
                    nota5 += 1
                    nota2 += 3
                 elif valor % 100  == 41:
                     nota20 -= 1
                     nota10 += 1
                     nota5 += 1
                     nota2 += 3

                 elif valor % 100  == 51:
                     nota50 -= 1
                     nota20 += 2
                     nota5 += 1
                     nota2 += 3
                 elif valor % 100  == 61:
                     nota10 -= 1
                     nota5 += 1
                     nota2 += 3
                 elif valor % 100  == 71:
                     nota20 -= 1
                     nota10 += 1
                     nota5 += 1
                     nota2 += 3

                 elif valor % 100   == 81:
                     nota10 -= 1
                     nota5 += 1
                     nota2 += 3

                 elif valor% 100  == 91:
                     nota20 -= 1
                     nota10 += 1
                     nota5 += 1
                     nota2 += 3



    if valor % 10 == 3:
        if valor < 100:

            if valor == 13:
                nota10 -= 1
                nota5 += 1
                nota2 += 3

            elif valor == 23:
                nota20 -= 1
                nota10 += 1
                nota5 += 1
                nota2 += 3

            elif valor == 33:
                nota10 -= 1
                nota5 += 1
                nota2 += 3
            elif valor == 43:
                nota20 -= 1
                nota10 += 1
                nota5 += 1
                nota2 += 3

            elif valor == 53:
                nota50 -= 1
                nota20 += 2
                nota5 += 1
                nota2 += 3
            elif valor == 63:
                nota10 -= 1
                nota5 += 1
                nota2 += 3
            elif valor == 73:
                nota20 -= 1
                nota10 += 1
                nota5 += 1
                nota2 += 3

            elif valor == 83:
                nota10 -= 1
                nota5 += 1
                nota2 += 3

            elif valor == 93:
                nota20 -= 1
                nota10 += 1
                nota5 += 1
                nota2 += 3

        else:
            if valor % 100 < 10:
                nota100 -= 1
                nota50 += 1
                nota20 += 2
                nota5 += 1
                nota2 += 3
            else:
                 if valor % 100 == 13:
                    nota10 -= 1
                    nota5 += 1
                    nota2 += 3

                 elif valor % 100  == 23:
                    nota20 -= 1
                    nota10 += 1
                    nota5 += 1
                    nota2 += 3

                 elif valor % 100  == 33:
                    nota10 -= 1
                    nota5 += 1
                    nota2 += 3
                 elif valor % 100  == 43:
                     nota20 -= 1
                     nota10 += 1
                     nota5 += 1
                     nota2 += 3

                 elif valor % 100  == 53:
                     nota50 -= 1
                     nota20 += 2
                     nota5 += 1
                     nota2 += 3
                 elif valor % 100  == 63:
                     nota10 -= 1
                     nota5 += 1
                     nota2 += 3
                 elif valor % 100  == 73:
                     nota20 -= 1
                     nota10 += 1
                     nota5 += 1
                     nota2 += 3

                 elif valor % 100   == 83:
                     nota10 -= 1
                     nota5 += 1
                     nota2 += 3

                 elif valor% 100  == 93:
                     nota20 -= 1
                     nota10 += 1
                     nota5 += 1
                     nota2 += 3


    if valor == 6:
        nota5 -= 1
        nota2 += 3

    if valor == 8:
        nota5 -= 1
        nota2 += 3



    if valor % 10 == 6:
        nota5 -= 1
        nota2 += 3

    if valor % 10 == 8:
        nota5 -= 1
        nota2 += 3

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
