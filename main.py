import os

#      TODO sprawdzenie czy haslo nie posiada liczb
#      TODO uniemozliwic wprowadzania liter ktore juz wczesniej juz sie uzylo
# MAIN
gra = True
zycia = 10

haslo = input('Wpisz haslo do zgadniecia:').lower()
hasloTemp = ([litery for litery in haslo])
hasloDoZgadniecia = (['_' for litery in haslo])
uzyteLitery= set()
zleLitery=[]



def zgadniecie():
    global zycia
    global uzyteLitery


    dlugoscPrzedPobraniemLitery = len(uzyteLitery)
    czyJestLiterka = False
    zgadula = input('Zgadnij literke: ')
    if zgadula.isalpha() == True:
        uzyteLitery.add(zgadula)
        dlugoscPoPobraniuLitery = len(uzyteLitery)
        if dlugoscPoPobraniuLitery != dlugoscPrzedPobraniemLitery:
            if len(zgadula) == 1:
                index = 0
                while index < len(haslo):
                    index = haslo.find(zgadula, index)
                    if index == -1:
                        break
                    czyJestLiterka = True
                    hasloDoZgadniecia[index] = zgadula
                    index += 1

            if (czyJestLiterka == False):
                zycia -= 1
                zleLitery.append(zgadula)

def czy_wygrana():
    global gra
    if zycia == 0:
        print('Przegrales')
        gra = False
    if hasloDoZgadniecia == hasloTemp:
        print('Gratuluje nie powiesiles sie!')
        gra = False


while gra == True:
    print('Ilosc zyc: ', zycia)
    print('Nieprawidlowe litery: ', zleLitery)
    if len(uzyteLitery) > 0:
        print('Uzyte litery: ', uzyteLitery)
    else:
        print('Uzyte litery: ')
    print('Haslo do zgadniecia: ', hasloDoZgadniecia)
    zgadniecie()
    print(hasloTemp)
    print(hasloDoZgadniecia)
    os.system('cls')
    czy_wygrana()
