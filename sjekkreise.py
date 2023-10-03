"""
Definer en funksjon sjekk_reise(reise) som tar inn en nøstet liste reise, hvor hvert element i
denne lista igjen er en liste med to elementer av datatype str (et par av reiseopprinnelse og
reisemål). Funksjonen skal returnere True dersom reise er en gyldig reiserute, og False ellers.
Reiseruten er gyldig når hvert reisemål (andre element i en indre liste) er likt reiseopprinnelsen
(første element) i den etterfølgende indre listen. Du kan anta at alle elementene i den ytre listen er
en indre liste av lengde 2.
"""
def sjekk_reise(reise):
    for i in range(len(reise) - 1):
        if reise[i][1] != reise[i + 1][0]:
            return False
    return True


"""
Et land har følgende regler for reisekarantene:
Dersom en person er vaksinert, trenger personen ikke å gå i karantene (0 dager i karantene)
Dersom en uvaksinert person har vært i et land som har fargekode rød eller oransje, skal
peresonen 10 dager i karantene.
Dersom en uvaksinert person har vært i et land som har fargekode grønn, skal personen 3 dager i
karantene.
Skriv en funksjon karantene(vaksinert, farge) som returner antall dager (datatype int) en person
må i karantene i henhold til reglene over, hvor parameteren vaksinert er enten True eller False
(datatype bool) og parameteren farge er enten "roed", "oransje" eller "groenn" (datatype str).
Altså skal for eksempel kallet karantene(True, "roed") returnere 0, mens kallet karantene(False,
"oransje") skal returnere 10.
"""
def karantene(vaksinert, farge):
    if vaksinert:
        return 0
    elif farge == "rød" or farge == "oransje":
        return 10
    return 3

"""
Skriv en funksjon tell_grader(fag, bsc, msc) som tar inn tre parametre av datatypen tekst (str) og
sjekker om en Bsc-grad og/eller en Msc-grad er innen et bestemt fag. Dersom parameteren fag
har samme verdi som både parametrene bsc og msc, skal funksjonen returnere 2. Dersom
parameteren fag har samme verdi som én av parametrene bsc eller msc skal funksjonen
returnere 1. Dersom parameteren fag hverken er lik verdien til parametrene bsc eller msc, skal
funksjonen returnere 0.
For eksempel skal kallet tell_grader("informatikk", "informatikk", "informatikk") returnere 2, mens
kallet tell_grader("historie", "informatikk", "informatikk") skal returnere 0.

""" 
def tell_grader(fag, bsc, msc):
    if (fag == bsc) and (fag == msc):
        return 2
    elif (fag != bsc) or (fag != msc):
        return 0
    return 1

"""
Skriv en funksjon fjern_vokaler(setning, vokal_liste) som tar inn to parametre - en setning
(datatype str) og en liste med vokaler (datatype list, hvor hvert element er en str av lengde 1).
Funksjonen skal returnere en kopi av teksten setning hvor alle vokaler fra vokal_liste er fjernet fra
teksten. Du kan anta at både setning og vokal_liste kun inneholder små bokstaver.
For eksempel skal kallet fjern_vokaler("ha det fint", ["a", "e", "i", "o", "u"]) returnere teksten "h dt
fnt".

"""
def fjern_vokaler(setning, vokal_liste):
    ny_setning = ""
    for vokal in setning:
        if vokal not in vokal_liste:
            ny_setning += vokal
    return ny_setning

"""
Skriv en funksjon summer_rabatt(vareliste, forpris, nypris) som tar som argument en liste med
varenavn (vareliste) , en ordbok med varenavn som nøkler og deres førpris som verdier
(forpris), samt en en ordbok med varenavn som nøkler og deres nypris som verdier (nypris).
Funksjonen skal regne ut hvor mye rabatt en kunde har fått i sum dersom kunden har kjøpt
varene i vareliste (én av hvert element i lista). Rabatten for en gitt vare er forskjellen mellom
førpris og nypris for det gitte varenavnet, hvor disse prisene ligger i hver sin ordbok forpris og
nypris. Du kan anta at alle varenavn i vareliste finnes som nøkler i både ordboken forpris og
nypris, og du kan anta at nypris alltid er lavere eller lik førpris.
For eksempel skal kallet summer_rabatt(["laptop", "ryggsekk"], {"laptop":5000, "ryggsekk":900},
{"laptop":4000, "ryggsekk":600}) returnere 1300.

"""
def summer_rabatt(vareliste, forpris, nypris):
    totalrabatt = 0
    for varer in vareliste:
        if varer in forpris:
            totalrabatt += forpris[varer] - nypris[varer]
    return totalrabatt
