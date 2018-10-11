#-------------------------------------------------------------------------------
# Name: Python Manipulação de matrizes (lista de lista) aplicado a jogo

# Purpose:
#
# Author:      7569223
#
# Created:     11/10/2018
# Copyright:   (c) 7569223 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import random

#Dimensões M x N do campo, t qntd de tiros
m = input ("linhas:")
n = input ("Colunas:")
t = input ("numero de tiros:")
m,n,t = int(m),int(n),int(t)



#leitura do campo (0 = areavazia; 1 = unidade)
C = []
for i in range (m):
    l = [int(x) for x in input().split()]
    C.append(l)


#leitura dos tiros (linha x coluna)
Ts = []
for i in range(t):
    T = [int (x) for x in input().split()]
    Ts.append(T)

#area preenchida
P = []
for i in range (m):
    for j in range(n):
        num = C[i][j]
        if num == 1:
            l = [i,j]
            P.append (l)

tam1 = len(Ts)
tam2 = len(P)


#contabilização da área atingida P[i][j] c relação aos disparos Ts[i][j])
cont = 0
i = 0
while i < tam1:
    if Ts[i][0] == P[i][0]:
        if Ts[i][1] == P[i][1]:
            cont += 1
    i += 1

print (Ts)
print (P)


#se cont > = tamanho do vetor (P), todos elementos eliminados
if cont >= tam2:
    print ("S")
else:
    print ("N")























