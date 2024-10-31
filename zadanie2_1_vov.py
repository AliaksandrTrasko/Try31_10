# policz liczbe elementow w liscie
def oblicz_liczbe_elementow(lista):
    l=0
    for i in lista:
        l+=1
    return l

"""# znajdz minimum w liscie za pomoca petli for
# i operatora warunkowe if"""
def minimum_w_liscie(lista):
    
    minimum = lista[0]
    for i in lista:
        if i<minimum:
            minimum=i
        
    return minimum
    
# anlogicznie maksimum
def maksimum_w_liscie(lista):
    
    maksimum = lista[0]
    for i in lista:
        if i>maksimum:
            maksimum=i
        
    return maksimum
    
"""# oblicz srednia za pomoca petli for
# wynik zaokrąglij do 2 miejsca po przecinku"""
def oblicz_srednia(lista):
    dlugsc=0
    summ=0
    for i in lista:
        summ+=i
        dlugsc+=1
    return round((summ/dlugsc), 2)

"""# importuj biblioteke statistics i za jej pomoca zaimplementuj 
# funkcje srednia_import
# wynik zaokrąglij do 2 miejsca po przecinku"""
import statistics
def oblicz_srednia_import(lista):
    return round(statistics.mean(lista), 2)
    
"""# za pomoca zaimplementowanej wyzej funkcji srednia
# oblicz srednia z podanego zakresu listy
# przyjmij, ze poczatek jest wlacznie, a końiec rozłącznie"""
def oblicz_srednia_zakresu(lista, poczatek, koniec):
    return oblicz_srednia_import(lista[poczatek:koniec])
    
"""# zwroc ocene studenta ze sredniej ocen z listy 
# progi:
# srednia < 3 --> 2
# srednia >= 3 i < 3.25 --> 3
# srednia >= 3.25 i < 3.75 --> 3.5
# srednia >= 3.75 i < 4.25 --> 4 
# itd
# wykorzystaj wczesniej zaimplementowa funckje srednia
# wykorzystaj operator warunkowy if, elif, else"""
def zwroc_ocene(lista_ocen):
    srednia=oblicz_srednia_import(lista_ocen)
    if srednia<3:
        return 2
    elif srednia>=3 and srednia<3.25:
        return 3
    elif srednia>=3.25 and srednia<3.75:
        return 3.5
    elif srednia>=3.75 and srednia<4.25:
        return 4
    elif srednia>=4.25 and srednia<4.75:
        return 4.5
    else:
        return 5

"""# oblicz ocene studenta z listy, ale tylko pod warunkiem,
# jesli przynajmniej polowa ocen z listy jest pozytywna 
# (przynajmniej 3), jesli nie ocena wynosi 2 
# mozesz wykorzystac funkcje ocena"""
def zwroc_ocene_warunek(lista_ocen):
    pozytywne_ocene=[]
    for i in lista_ocen:
        if i>=3:
            pozytywne_ocene.append(i)
    if len(pozytywne_ocene)>=len(lista_ocen)/2:
        return(zwroc_ocene(lista_ocen))
    else:
        return 2
        
"""# oblicz srednia wazona studenta
# lista ocen sklada sie z list, przy czym 
# zagnizdzona lista zawiera informacje o wadze oceny i samej ocenie
# wynik zaokraglij do drugiego miejsca po przecinku
# przykładowy input: [[4, 5], [1, 2], [2, 3.5]]"""
def oblicz_srednia_wazona(lista_ocen):
    summa_ocen=0
    iloczyn_ocen_i_wadz=0
    for i in lista_ocen:
        iloczyn_ocen_i_wadz+=i[0]*i[1]
        summa_ocen+=i[0]
    return round(iloczyn_ocen_i_wadz/summa_ocen, 2)
    
"""# na podstawie sredniej wskaz ocene
# podpowiedz: przeniesz progi z funkcji ocena 
# do funkcji ponizej, a w funkcji ocena korzystaj z 
# funkcji ponizej
# jesli mozesz unikac dublowania kodu - unikaj"""
def zwroc_ocene_ze_sredniej(srednia):
    if srednia<3:
        return 2
    elif srednia>=3 and srednia<3.25:
        return 3
    elif srednia>=3.25 and srednia<3.75:
        return 3.5
    elif srednia>=3.75 and srednia<4.25:
        return 4
    elif srednia>=4.25 and srednia<4.75:
        return 4.5
    else:
        return 5
        

'''
na podstawie listy, ktorej struktura przedstawia sie nastepujaco:
[precent_frekwencji, udzial_w_debacie, ocena_z_testu, aktywnosc_prawda_falsz, [oceny_z_zadan, ...]]
np. [0.5, True, 4.5, False, [2, 3.5, 5, 5]]
zaimplementuj funkcje, ktora zwroci ocene studentowi 
warunki dla ocen są następujące:
- jeśli precent_frekwencji < 0.4 wystaw 2, inaczej oblicz ocene podstawową
- do wyliczenia oceny podstawowej ze wzoru
    jeśli aktywnosc_prawda_falsz == True wzór wygląda następująco:
        (ocena_z_testu + średnia z oceny_z_zadan + 0.1)/2
    jeśli aktywnosc_prawda_falsz == False wzór wygląda następująco:
        (ocena_z_testu + średnia z oceny_z_zadan)/2
    użyj funkcji zwroc_ocene
- za udzial_w_debacie == True podnieś ocene o pół w górę
UWAGA! Pamiętaj, że na studiach występują następujące oceny: 2, 3, 3.5, 4, 4.5, 5
'''
def zwroc_ocene_z_skomplikowanych_warunkow_zaliczenia(lista):
    ocena=0
    if lista[0]<0.4:
        ocena=2
    else:
        if lista[3]==True:
            ocena=(lista[2]+oblicz_srednia_import(lista[4])+0.1)/2
        else:
            ocena=(lista[2]+oblicz_srednia_import(lista[4]))/2
        ocena=zwroc_ocene_ze_sredniej(ocena)
    if lista[1]==True:
        ocena+=0.5
        ocena=zwroc_ocene_ze_sredniej(ocena)
    return ocena


# STREFA SKRYPTU
if __name__ == '__main__':
    pass
    # student = [0.5, True, 4.5, False, [2, 3.5, 5, 5]]

    # ocena = zwroc_ocene_z_skomplikowanych_warunkow_zaliczenia(student)
    # print(ocena)