kunden = [
        {"name": "Gemm", "nachname": "Simpson", "bundesland": "Bayern", "jahr_eintritt": 2010, "jahr_austritt": 2016},
        {"name": "Layton", "nachname": "Ballard", "bundesland": "NRW", "jahr_eintritt": 2014, "jahr_austritt": 2018},
        {"name": "Nathaniel", "nachname": "Ochoa", "bundesland": "Hamburg", "jahr_eintritt": 2016, "jahr_austritt": 2026},
        {"name": "Tyrone", "nachname": "Simpson",  "bundesland": "NRW", "jahr_eintritt": 2020, "jahr_austritt": 2030},
        {"name": "Jenson", "nachname": "Gonzales", "bundesland": "Sachsen", "jahr_eintritt": 2018, "jahr_austritt": 2028}
    ]


print("Aufgabe 1)")

def print_kunde(kunde):
    # Vervollständige die Funktion, um folgende Ausgabe mittels des Beispielaufrufs zu generieren: 
    # > Nathaniel Ochoa aus Hamburg eingetreten im Jahr 2016, ausgetreten im Jahr 2026
    
    # # Anfang Lösung:
    # print(f"{kunde['name']} {kunde['nachname']} aus "
    #      +f"{kunde['bundesland']} eingetreten im Jahr " 
    #      +f"{kunde['jahr_eintritt']}, ausgetreten im Jahr "
    #      +f"{kunde['jahr_austritt']}")
    # # Ende Lösung

    # Anfang Lösung:
    ausgabestring = ("{} {} aus {} eingetreten im Jahr {}, ausgetreten im Jahr {}")
    print(ausgabestring.format(kunde["name"], 
                               kunde["nachname"],
                               kunde["bundesland"],
                               kunde["jahr_eintritt"],
                               kunde["jahr_austritt"]))
    # Ende Lösung


# Beispielaufruf
print_kunde(kunden[2])


print("\nAufgabe 2)")

def print_kunden(kunden):
    # Vervollständige die Funktion, um folgende Ausgabe mittels des Beispielaufrufs zu generieren: 
    # > Gemm Simpson aus Bayern eingetreten im Jahr 2010, ausgetreten im Jahr 2016
    # > Layton Ballard aus NRW eingetreten im Jahr 2014, ausgetreten im Jahr 2018
    # > Nathaniel Ochoa aus Hamburg eingetreten im Jahr 2016, ausgetreten im Jahr 2026
    # > Tyrone Simpson aus NRW eingetreten im Jahr 2020, ausgetreten im Jahr 2030
    # > Jenson Gonzales aus Sachsen eingetreten im Jahr 2018, ausgetreten im Jahr 2028

    # Anfang Lösung:
    for kunde in kunden:
        print_kunde(kunde)
    # Ende Lösung

# Beispielaufruf
print_kunden(kunden)


print("\nAufgabe 3)")

def print_kunde_suche_name(kunden, nachname):
    # Vervollständige die Funktion, um folgende Ausgabe mittels des Beispielaufrufs zu generieren: 
    # > Gemm Simpson aus Bayern eingetreten im Jahr 2010, ausgetreten im Jahr 2016
    # > Tyrone Simpson aus NRW eingetreten im Jahr 2020, ausgetreten im Jahr 2030
    # Hinweis: Groß- und Kleinschreibung soll beachtet werden

    # Anfang Lösung:
    print_kunden(kunde for kunde in kunden 
                    if nachname == kunde['nachname'])
    # Ende Lösung

# Beispielaufruf
print_kunde_suche_name(kunden, "Simpson")


print("\nAufgabe 4)")

def print_kunde_suche_name_ci(kunden, nachname):
    # Vervollständige die Funktion, um folgende Ausgabe mittels des Beispielaufrufs zu generieren: 
    # > Gemm Simpson aus Bayern eingetreten im Jahr 2010, ausgetreten im Jahr 2016
    # > Tyrone Simpson aus NRW eingetreten im Jahr 2020, ausgetreten im Jahr 2030
    # Hinweis: ci steht für case insensitive, d.h. Groß- und Kleinschreibung wird nicht beachtet

    # Anfang Lösung:
    print_kunden(kunde for kunde in kunden 
                    if nachname.lower() == kunde['nachname'].lower())
    # Ende Lösung

# Beispielaufruf
print_kunde_suche_name_ci(kunden, "simPsoN")


print("\nAufgabe 5)")

def print_kunde_suche_jahr(kunden, jahr):
    # Vervollständige die Funktion so, dass sie alle Personen listet, die zum übergebenen Zeitpunkt Kunde waren
    # Mit Beispielaufruf zu generierende Ausgabe:
    # > Gemm Simpson aus Bayern eingetreten im Jahr 2010, ausgetreten im Jahr 2016
    # > Layton Ballard aus NRW eingetreten im Jahr 2014, ausgetreten im Jahr 2018
    # > Nathaniel Ochoa aus Hamburg eingetreten im Jahr 2016, ausgetreten im Jahr 2026

    # Anfang Lösung:
    print_kunden(kunde for kunde in kunden 
                    if kunde['jahr_eintritt'] <= jahr <= kunde['jahr_austritt'])
    # Ende Lösung

# Beispielaufruf
print_kunde_suche_jahr(kunden, 2016)


print("\nAufgabe 6)")

def print_kunde_suche_jahr_bereich(kunden, jahr_start, jahr_ende):
    # Vervollständige die Funktion so, dass sie alle Personen listet, die in der übergebenen Zeitspanne Kunde waren
    # Mit Beispielaufruf zu generierende Ausgabe:
    # > Nathaniel Ochoa aus Hamburg eingetreten im Jahr 2016, ausgetreten im Jahr 2026
    # > Tyrone Simpson aus NRW eingetreten im Jahr 2020, ausgetreten im Jahr 2030
    # > Jenson Gonzales aus Sachsen eingetreten im Jahr 2018, ausgetreten im Jahr 2028

    # Anfang Lösung:
    print_kunden(kunde for kunde in kunden 
            if kunde['jahr_eintritt'] <= jahr_start <= jahr_ende <= kunde['jahr_austritt'])
    # Ende Lösung

# Beispielaufruf
print_kunde_suche_jahr_bereich(kunden, 2022, 2024)


print("\nAufgabe 7)")

def print_kunde_vis(kunde):
    # Vervollständige die Funktion:
    # Sie soll den Eintritt und Austritt einer Person visualisieren in der Zeitspanne von 2000-2040.
    # Mit Beispielaufruf zu generierende Ausgabe:
    # > ______________-----______________________ | Layton Ballard
    # Ein Minuszeichen steht für ein Jahr Kunde sein
    # Ein Unterstrich steht für ein Jahr kein Kunde sein

    # Anfang Lösung:
    zeitspanne = "".join("-" if kunde['jahr_eintritt'] <= jahr <= kunde['jahr_austritt'] else "_"\
                         for jahr in range(2000,2040+1))\
                 + f" | {kunde['name']+" "+kunde['nachname']}"
    print(zeitspanne)
    # Ende Lösung

# Beispielaufruf
print_kunde_vis(kunden[1])


print("\nAufgabe 8)")

def print_kunden_vis(kunden):
    # Vervollständige die Funktion, um folgende Ausgabe zu generieren:
    # > 2000      2010      2020      2030   2040
    # > V^^^^^^^^^V^^^^^^^^^V^^^^^^^^^V^^^^^^^^^V
    # > __________-------________________________ | Gemm Simpson
    # > ______________-----______________________ | Layton Ballard
    # > ________________-----------______________ | Nathaniel Ochoa
    # > ____________________-----------__________ | Tyrone Simpson
    # > __________________-----------____________ | Jenson Gonzales

    # Anfang Lösung:
    vis ="".join(f"{"20{}0".format(str(jahr)):<10}" for jahr in range(0,4+1))
    vis ="".join(f'{vis[:34]+vis[37:]:>46}'+"\nV"+(f"{'':^>9}"+"V")*4)
    print(vis) 
    for kunde in kunden:
        print_kunde_vis(kunde)
    # Ende Lösung

# Beispielaufruf
print_kunden_vis(kunden)


print("\nAufgabe 9)")

def austreten_zum_jahr(kunden, jahr):
    # Vervollständige die Funktion, so dass keine Person über den übergeben Zeitpunkt hinaus Kunde ist.

    # Anfang Lösung:
    for kunde in kunden:
        if kunde['jahr_austritt'] > jahr: kunde['jahr_austritt'] = jahr
    
    return kunden
    # Ende Lösung

# Beispielaufruf
kunden = austreten_zum_jahr(kunden, 2026)

# Erwartete Visualisierung des Beispielaufrufs:
# > 2000      2010      2020      2030   2040
# > V^^^^^^^^^V^^^^^^^^^V^^^^^^^^^V^^^^^^^^^V
# > __________-------________________________ | Gemm Simpson
# > ______________-----______________________ | Layton Ballard
# > ________________-----------______________ | Nathaniel Ochoa
# > ____________________-------______________ | Tyrone Simpson
# > __________________---------______________ | Jenson Gonzales
print_kunden_vis(kunden)


print("\nAufgabe 10)")

def laufzeit_beschraenken_auf_max_jahre(kunden, jahre):
    # Vervollständige die Funktion so, dass keine Person länger als die übergebene Laufzeit Kunde ist.
    
    # Anfang Lösung:
    jahre_max = lambda kunde,jahre : kunde['jahr_eintritt']+jahre \
                                     if kunde['jahr_austritt']\
                                     - kunde['jahr_eintritt'] > jahre \
                                     else kunde['jahr_austritt']
    
    for kunde in kunden:
        kunde['jahr_austritt'] = jahre_max(kunde,jahre-1)
    # Ende Lösung

# Beispielaufruf
laufzeit_beschraenken_auf_max_jahre(kunden, 5)

# Erwartete Visualisierung des Beispielaufrufs:
# > 2000      2010      2020      2030   2040
# > V^^^^^^^^^V^^^^^^^^^V^^^^^^^^^V^^^^^^^^^V
# > __________-----__________________________ | Gemm Simpson
# > ______________-----______________________ | Layton Ballard
# > ________________-----____________________ | Nathaniel Ochoa
# > ____________________-----________________ | Tyrone Simpson
# > __________________-----__________________ | Jenson Gonzales
print_kunden_vis(kunden)
