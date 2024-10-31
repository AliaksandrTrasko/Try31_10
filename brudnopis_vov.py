#16.10.24 lab
"""

n=1
while n<4:
    print(n)
    n+=1
print('koniec')
#=
for i in [1,2,3]:
    print(i)
#=
for i in range(1,4):
    print(i)

for i in range(5):
    print(i)
#output: 0,1,2,3,4

l=[1, 2, 3, 4]
d=len(l)
for i in range(d):
    print (l[i])



from funkcje import* 

result(4)

print(pole_kwadratu(4))
assert (pole_kwadratu(4) == 16)
"""

#Zadanie 2.1
from zadanie2_1 import oblicz_liczbe_elementow
from zadanie2_1 import minimum_w_liscie
from zadanie2_1 import maksimum_w_liscie
from zadanie2_1 import oblicz_srednia
from zadanie2_1 import oblicz_srednia_import
from zadanie2_1 import oblicz_srednia_zakresu
from zadanie2_1 import zwroc_ocene
from zadanie2_1 import zwroc_ocene_warunek
from zadanie2_1 import oblicz_srednia_wazona
from zadanie2_1 import zwroc_ocene_ze_sredniej
from zadanie2_1 import zwroc_ocene_z_skomplikowanych_warunkow_zaliczenia

lista=[2, 2, 1, 5,]
test=[2, 5, 2.56, 3756, -1]
lista_2=[[4, 5], [1, 2], [2, 3.5]]
lista_3=[0.5, True, 5, False, [4, 5, 5, 5]]
print(oblicz_liczbe_elementow(lista))
print(minimum_w_liscie(lista))
print(maksimum_w_liscie(lista))
print(oblicz_srednia(test))
print(oblicz_srednia_import(lista))
print(oblicz_srednia_zakresu(lista, 1, 3))
print(zwroc_ocene(lista))
print(zwroc_ocene_warunek(lista))
print(oblicz_srednia_wazona(lista_2))
print(zwroc_ocene_ze_sredniej(oblicz_srednia_import(lista)))
print(zwroc_ocene_z_skomplikowanych_warunkow_zaliczenia(lista_3))



#Zadanie 2.0
"""
a= ['a', 'b', 'c','d','e', 'f', 'g', 'h', 'i', 'j']
print(len(a))
print(a[3], a[7])
print(a[-1], a[-8])
print(a[1:5])
print(a[2::3])

a.append('k')
a.append('l')
a.append('m')
a.append('n')
a.pop(2)
a.pop(8)

b=a
b.pop(0) 
print(a)

print(b)

a= ['a', 'b', 'c','d','e', 'f', 'g', 'h', 'i', 'j']
c=a.copy()
c.pop(0)
print(a)
print(c)

i=1
while i<11:
    print(i, end=' ')
    i+=1
print('')
for i in range (1, 11, 1):
    print(i, end=' ')
print('')

i=2
while i<11:
    print(i, end=' ')
    i+=2
print('')
for i in range (2, 11, 2):
    print(i, end=' ')
print('')

import math
print ('%.5f' % math.pi)

lista_zagniezdzona=[1, 2, 3, 4]
lista=['a', lista_zagniezdzona, 'b']
print (lista[1][1])
"""

#09.10.24 lab
"""
#moja_lista= ['a', 'b', 'c','d']
#print (moja_lista[1])

#moja_tabela= [[1,2,3],
#              [4,5,6],
#              [7,8,9]]
#print (moja_tabela[1][0])

#moja_lista= ['a', 'b', 'c','d','e', 'f']
#print ("-----start-----")
#print (moja_lista[3:])

#moja_lista= ['a', 'b', 'c','d','e', 'f']
#print ("-----start-----")
#print (moja_lista[:-2])

#moja_lista= ['a', 'b', 'c','d','e', 'f']
#print ("-----start-----")
#print (moja_lista[0:7:2])

#moja_lista= ['a', 'b', 'c','d','e', 'f']
#print ("-----start-----")
#print (moja_lista[::-2])

#moja_lista= ['a', 'b', 'c','d','e', 'f']
#print ("-----start-----")
#print (moja_lista[0:3])

#moja_lista= ['a', 'b', 'c','d','e', 'f']
#moja_lista.append('g')
#print (moja_lista[::])
#moja_lista.pop(1)
#print (moja_lista[::])
#dlugosc=len(moja_lista)
#print ("moja lista ma {dlugosc} elementow")

#from funkcje import dlugosc_listy
    
#moja_lista= ['a', 'b', 'c','d','e', 'f']
#print (f"moja funkcja ma {dlugosc_listy(moja_lista)} elementow")

#python brudnopis.py
"""
