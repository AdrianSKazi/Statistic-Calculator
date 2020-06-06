import math

###DESCRIPTIVE SSTATISTICS###
#Srednia Arytmetyczna
def Mean(xi,ni):
    c = 0
    n = 0
    for i in range(len(xi)):
        c += xi[i]*ni[i]
        n += ni[i]
    srednia = c/n
    return print('Mean = ',srednia)

#Odchylenie Standardowe
def StandardDeviation(xi,ni):
    # srednia arytmetyczna
    c = 0
    n = 0
    for i in range(len(xi)):
        c += xi[i] * ni[i]
        n += ni[i]
    srednia = c / n

    #wariancja
    licznik = []
    for i in range(len(xi)):
        licznik.append(math.pow(xi[i] - srednia, 2) * ni[i])
    wariancja = sum(licznik) / sum(ni)

    #odchylenie standardowe
    odchylenie = math.sqrt(wariancja)
    print('Standard Deviation = ', odchylenie)

#Wariancja
def Variance(xi,ni):
    # srednia arytmetyczna
    c = 0
    n = 0
    for i in range(len(xi)):
        c += xi[i] * ni[i]
        n += ni[i]
    srednia = c / n

    licznik = []
    for i in range(len(xi)):
        licznik.append(math.pow(xi[i] - srednia, 2) * ni[i])
    wariancja = sum(licznik) / sum(ni)
    return print('Variance = ',wariancja)

#Wariancja nieobciążona
def VarianceUnbiased(xi,ni):
    #srednia
    c = 0
    n = 0
    for i in range(len(xi)):
        c += xi[i] * ni[i]
        n += ni[i]
    srednia = c / n

    licznik = []
    for i in range(len(xi)):
        licznik.append(math.pow(xi[i]-srednia,2))
    wariancja = sum(licznik) / (sum(ni)-1)
    return wariancja

#Wariancja Resztowa
def RemainderVariance(xi,yi,ni):
    # Linia regresji
    sredniaX = sum(xi) / len(xi)
    sredniaY = sum(yi) / len(yi)

    a1LicznikTab = []
    for i in range(len(xi)):
        a1LicznikTab.append((xi[i] - sredniaX) * (yi[i] - sredniaY) * ni[i])
    a1Licznik = sum(a1LicznikTab)

    a1MianownikTab = []
    for i in range(len(xi)):
        a1MianownikTab.append(math.pow(xi[i] - sredniaX, 2) * ni[i])
    a1Mianownik = sum(a1MianownikTab)

    a1 = a1Licznik / a1Mianownik
    a0 = sredniaY - a1 * sredniaX

    # wartosci oczekiwane
    yiExpectedTab = []
    for i in range(len(xi)):
        yiExpectedTab.append(a0 + a1 * xi[i])

    # Wariancja resztowa z prostą jako regresja
    SSquareNiLicznikTab = []
    for i in range(len(xi)):
        SSquareNiLicznikTab.append(math.pow(yi[i] - yiExpectedTab[i], 2) * ni[i])
    SSquareNiLicznik = sum(SSquareNiLicznikTab)

    wariancjaResztowa = SSquareNiLicznik / (sum(ni) - 2)
    return print('Remainder Variance = ',wariancjaResztowa)

#Odchylenie przeciętne
def AverageDeviation(xi,ni):
    # srednia
    c = 0
    n = 0
    for i in range(len(xi)):
        c += xi[i] * ni[i]
        n += ni[i]
    srednia = c / n

    licznik = 0

    for i in range(len(xi)):
        licznik += (abs(xi[i] - srednia) * ni[i])
    odchylenieprzecietne = licznik / sum(ni)
    print('Average Deviation = ', odchylenieprzecietne)

#Odchylenie ćwiartkowe
def QuartileDeviation(xi,ni):
    tab = []

    for i in range(len(xi)):
        for j in range(ni[i]):
            tab.append(xi[i])
    tab.sort()
    q3 = tab[int((3/4 * len(tab))+1)]
    q1 = tab[int((1/4 * len(tab))+1)]

    q = (q3-q1)/2

    # return print('Quartile Deviation = ',q)
    return print('Quartile Deviation = ',q)

#Współczynnik zmienności
def CoefficientOfVariation(xi,ni):
    # srednia arytmetyczna
    c = 0
    n = 0
    for i in range(len(xi)):
        c += xi[i] * ni[i]
        n += ni[i]
    srednia = c / n

    # wariancja
    licznik = []
    for i in range(len(xi)):
        licznik.append(math.pow(xi[i] - srednia, 2) * ni[i])
    wariancja = sum(licznik) / sum(ni)

    # odchylenie standardowe
    odchylenie = math.sqrt(wariancja)

    return print('Coefficient of Variation = ',round(odchylenie/srednia*100,2),'%')

#Współczynnik koncentracji Lorentza
def LorentzConcentrationIndex(xi, ni):
    # suma ni
    suma_ni = sum(ni)

    # xi * ni
    xini = []
    for i in range(len(xi)):
        xini.append(xi[i] * ni[i])
    suma_xini = sum(xini)

    # procent ni
    ni_proc = []
    for i in range(len(ni)):
        ni_proc.append((ni[i] / suma_ni) * 100)

    # procent xi * ni
    xini_proc = []
    for i in range(len(ni)):
        xini_proc.append((xini[i] / suma_xini) * 100)

    # skumulowany procent ni
    ni_proc_cumm = []
    ni_proc_cumm.append(ni_proc[0])
    for i in range(1, len(ni)):
        ni_proc_cumm.append(ni_proc[i] + ni_proc_cumm[i - 1])

    # skumulowany procent xi * ni
    xini_proc_cumm = []
    xini_proc_cumm.append(xini_proc[0])
    for i in range(1, len(ni)):
        xini_proc_cumm.append(xini_proc[i] + xini_proc_cumm[i - 1])
    pole = 5000
    p1 = 1 / 2 * ni_proc_cumm[0] * xini_proc_cumm[0]

    # łączna powierzchnia pozostałych pól
    pola = [p1]
    for i in range(len(ni) - 1):
        pola.append(1 / 2 * (xini_proc_cumm[i] + xini_proc_cumm[i + 1]) * (ni_proc_cumm[i + 1] - ni_proc_cumm[i]))

    # wskaźnik Lorenza
    k = (pole - sum(pola)) / pole

    return print('Lorentz Concentration Index = ',round(k, 3))

#Moment Centralny Trzeciego Rzędu
def ThirdCentralMoment(xi,ni):
    #srednia
    c = 0
    n = 0
    for i in range(len(xi)):
        c += xi[i] * ni[i]
        n += ni[i]
    srednia = c / n

    #licznik
    tab = []
    for i in range(len(xi)):
        tab.append(math.pow((xi[i]-srednia),3)*ni[i])
    m3_licznik = sum(tab)

    #moment centralny 3-ego rzędu
    m3 = m3_licznik / sum(ni)

    if m3 > 0:
        a = ('Right-hand asymmetry')
    elif m3 == 0:
        a = ('Ideal symmetry')
    else:
        a = ('Left-hand asymmetry')

    return print('Third Central Moment = ', round(m3,3),'\n'+'Asymmetry: ',a)

#MomentStandaryzowanyTrzeciegoRzędu
def StandarizedThirdCentralMoment(xi,ni):
    ###MOMENT CENTRALNY 3-EGO RZĘDU
    # srednia
    c = 0
    n = 0
    for i in range(len(xi)):
        c += xi[i] * ni[i]
        n += ni[i]
    srednia = c / n

    # licznik
    tab = []
    for i in range(len(xi)):
        tab.append(math.pow((xi[i] - srednia), 3) * ni[i])
    m3_licznik = sum(tab)

    # moment centralny 3-ego rzędu
    m3 = m3_licznik / sum(ni)

    ###S^3
    # wariancja
    licznik = []
    for i in range(len(xi)):
        licznik.append(math.pow(xi[i] - srednia, 2) * ni[i])
    wariancja = sum(licznik) / sum(ni)

    # odchylenie standardowe
    odchylenie = math.sqrt(wariancja)

    #S^3
    S3 = math.pow(odchylenie,3)

    As = m3/S3

    return print('Standarized Third Central Moment = ',As)

#Moment Centralny Czwartego Rzędu
def FourthCentralMoment(xi,ni):
    #srednia
    c = 0
    n = 0
    for i in range(len(xi)):
        c += xi[i] * ni[i]
        n += ni[i]
    srednia = c / n

    #licznik
    tab = []
    for i in range(len(xi)):
        tab.append(math.pow((xi[i]-srednia),4)*ni[i])
    m4_licznik = sum(tab)

    #moment centralny 4-ego rzędu
    m4 = m4_licznik / sum(ni)

    return print('Fourth Central Moment = ', round(m4,3))

#MomentStandaryzowanyCzwartegoRzędu
def StandarizedFourthCentralMoment(xi,ni):
    ###MOMENT CENTRALNY 4-EGO RZĘDU
    # srednia
    c = 0
    n = 0
    for i in range(len(xi)):
        c += xi[i] * ni[i]
        n += ni[i]
    srednia = c / n

    # licznik
    tab = []
    for i in range(len(xi)):
        tab.append(math.pow((xi[i] - srednia), 4) * ni[i])
    m4_licznik = sum(tab)

    # moment centralny 4-ego rzędu
    m4 = m4_licznik / sum(ni)

    ###S^4
    # wariancja
    licznik = []
    for i in range(len(xi)):
        licznik.append(math.pow(xi[i] - srednia, 2) * ni[i])
    wariancja = sum(licznik) / sum(ni)

    # odchylenie standardowe
    odchylenie = math.sqrt(wariancja)

    #S^4
    S4 = math.pow(odchylenie,4)

    #A4
    a4 = m4/S4

    if a4>3:
        a = ('Values are more focused than in normal distribution')
    elif a4==3:
        a = ('Values are equally focused as in normal distribution')
    else:
        a = ('Values are less focused than in normal distribution')
    return print('Standarized Fourth Central Moment = ',round(a4,3),'\n'+'Interpretation: ',a)
