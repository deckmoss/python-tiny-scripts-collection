articles = {
    123010 : "Entchen",
    123020 : "Tisch",
    123030 : "Lampe",
    123040 : "Vase",
    123050 : "Stuhl",
    123060 : "Bilderrahmen",
    123070 : "Poster",
}

vis=""

customers = [
        { "name": "Gemm", "nachname": "Simpson", "artikelnummern": [123010, 123020] },
        { "name": "Layton", "nachname": "Ballard", "artikelnummern": [123020, 123070] },
        { "name": "Nathaniel", "nachname": "Ochoa", "artikelnummern": [123050, 123060] },
        { "name": "Tyrone", "nachname": "Simpson", "artikelnummern": [123030, 123040] },
        { "name": "Jenson", "nachname": "Gonzales", "artikelnummern": [123060, 123070] },
]

# def returnArticle(articles):
#     return lambda articles : 

print("\nAufgabe 1)")

def print_customer_article_hierarchy(kunden: list, artikel: list) -> None:
    # Vervollständige die Funktion, um folgende Ausgabe mittels des Beispielaufrufs zu generieren: 
    # > Gemm Simpson:
    # >     123010 Entchen
    # >     123020 Tisch
    # > 
    # > Layton Ballard:
    # >     123020 Tisch
    # >     123070 Poster
    # > 
    # > Nathaniel Ochoa:
    # >     123050 Stuhl
    # >     123060 Bilderrahmen
    # > 
    # > Tyrone Simpson:
    # >     123030 Lampe
    # >     123040 Vase
    # > 
    # > Jenson Gonzales:
    # >     123060 Bilderrahmen
    # >     123070 Poster
    # >

    # Anfang Lösung:
    vis=""
    for customer in kunden:
        vis+="{} {}:".format(customer["name"],customer["nachname"])
        for code in customer["artikelnummern"]:
            vis+=f"{'\n':<4}{str(code)+" "+artikel[code]}"
        vis+="\n"*2
    print(vis)
    # Ende Lösung

# Beispielaufruf:
print_customer_article_hierarchy(customers, articles)


print("\nAufgabe 2)")

def print_customer_article_flat(kunden: list, artikel: list) -> None:
    # Vervollständige die Funktion, um folgende Ausgabe mittels des Beispielaufrufs zu generieren: # Vervollständige die Funktion, um folgende Ausgabe mittels des Beispielaufrufs zu generieren: 
    # > Gemm Simpson: 123010 Entchen
    # > Gemm Simpson: 123020 Tisch
    # > 
    # > Layton Ballard: 123020 Tisch
    # > Layton Ballard: 123070 Poster
    # > 
    # > Nathaniel Ochoa: 123050 Stuhl
    # > Nathaniel Ochoa: 123060 Bilderrahmen
    # > 
    # > Tyrone Simpson: 123030 Lampe
    # > Tyrone Simpson: 123040 Vase
    # > 
    # > Jenson Gonzales: 123060 Bilderrahmen
    # > Jenson Gonzales: 123070 Poster
    # >

    # Anfang Lösung:
    vis=""
    for kunde in kunden:
        for code in kunde["artikelnummern"]:
            vis+="{} {}: {} {}".format(kunde["name"],
                                       kunde["nachname"],
                                       code,
                                       artikel[code])
            vis+="\n"
        vis+="\n"    
    print(vis)
    # Ende Lösung

# Beispielaufruf:
print_customer_article_flat(customers, articles)


print("\nAufgabe 3)")

def append_customer(kunden: list, vorname: str, name: str, artikelnummern: list[int]) -> None:
    # Vervollständige die Funktion, um folgende Ausgabe mittels des Beispielaufrufs zu generieren: 
    # > Gemm Simpson:
    # >    123010 Entchen
    # >    123020 Tisch
    # > 
    # > Layton Ballard:
    # >    123020 Tisch
    # >    123070 Poster
    # > 
    # > Nathaniel Ochoa:
    # >    123050 Stuhl
    # >    123060 Bilderrahmen
    # > 
    # > Tyrone Simpson:
    # >    123030 Lampe
    # >    123040 Vase
    # > 
    # > Jenson Gonzales:
    # >    123060 Bilderrahmen
    # >    123070 Poster
    # > 
    # > Stefan Müller:
    # >    123020 Tisch
    # >    123060 Bilderrahmen
    # >

    # Anfang Lösung:
    global customers
    customers.append({ "name": vorname, "nachname": name, "artikelnummern": artikelnummern })
    # Ende Lösung

# Beispielaufruf:
append_customer(customers, "Stefan", "Müller", [123020, 123060])
print_customer_article_hierarchy(customers, articles)


print("\nAufgabe 4)")

def append_article(kunden: list, vorname: str, name: str, artikelnummer: int) -> None:
    # Vervollständige die Funktion, um folgende Ausgabe mittels des Beispielaufrufs zu generieren: 
    # > Gemm Simpson:
    # >    123010 Entchen
    # >    123020 Tisch
    # > 
    # > Layton Ballard:
    # >    123020 Tisch
    # >    123070 Poster
    # >    123050 Stuhl
    # > 
    # > Nathaniel Ochoa:
    # >    123050 Stuhl
    # >    123060 Bilderrahmen
    # > 
    # > Tyrone Simpson:
    # >    123030 Lampe
    # >    123040 Vase
    # > 
    # > Jenson Gonzales:
    # >    123060 Bilderrahmen
    # >    123070 Poster
    # > 
    # > Stefan Müller:
    # >    123020 Tisch
    # >    123060 Bilderrahmen
    # >

    # Anfang Lösung:
    global customers
    global articles
    for kunde in customers:
        if kunde["name"] == vorname and kunde["nachname"]== name:
            kunde["artikelnummern"].append(artikelnummer)
    # Ende Lösung

# Beispielaufruf:
append_article(customers, "Layton", "Ballard", 123050)
print_customer_article_hierarchy(customers, articles)


print("\nAufgabe 5)")

def delete_article(kunden: list, artikelnummer: int) -> None:
    # Vervollständige die Funktion, um folgende Ausgabe mittels des Beispielaufrufs zu generieren: 
    # > Gemm Simpson:
    # >    123010 Entchen
    # >    123020 Tisch
    # > 
    # > Layton Ballard:
    # >    123020 Tisch
    # >    123070 Poster
    # >    123050 Stuhl
    # > 
    # > Nathaniel Ochoa:
    # >    123050 Stuhl
    # > 
    # > Tyrone Simpson:
    # >    123030 Lampe
    # >    123040 Vase
    # > 
    # > Jenson Gonzales:
    # >    123070 Poster
    # > 
    # > Stefan Müller:
    # >    123020 Tisch
    # >

    # Anfang Lösung:
    global customers
    global articles
    del articles[artikelnummer]
    for kunde in customers:
        for code in kunde["artikelnummern"]:
            if code not in articles: kunde["artikelnummern"].remove(code)
    # Ende Lösung

# Beispielaufruf:
delete_article(customers, 123060)
print_customer_article_hierarchy(customers, articles)


print("\nAufgabe 6)")

def amount_article_sold(kunden: list, artikelnummer: int) -> int:
    # Vervollständige die Funktion, um folgende Ausgabe mittels des Beispielaufrufs zu generieren: 
    # > Artikelnummer '123020' 3x verkauft
    # > Artikelnummer '123070' 2x verkauft
    
    # Anfang Lösung:
    def article_counter(kunden: list):
        return lambda artikelnummer : (1 for kunde in kunden if artikelnummer in kunde["artikelnummern"])
    return sum(*[article_counter(kunden)(artikelnummer)])
    # Ende Lösung


# Beispielaufruf:
print(f"Artikelnummer '123020' {amount_article_sold(customers, 123020)}x verkauft")
print(f"Artikelnummer '123070' {amount_article_sold(customers, 123070)}x verkauft")

print("\nAufgabe 7)")

def print_article_sold(kunden: list, artikelnummern: list) -> int:
    # Vervollständige die Funktion, um folgende Ausgabe mittels des Beispielaufrufs zu generieren: 
    # > Artikelnummer '123010' 1x verkauft
    # > Artikelnummer '123020' 3x verkauft
    # > Artikelnummer '123030' 1x verkauft
    # > Artikelnummer '123040' 1x verkauft
    # > Artikelnummer '123050' 2x verkauft
    # > Artikelnummer '123060' 0x verkauft
    # > Artikelnummer '123070' 2x verkauft

    # Anfang Lösung
    vis=""
    for code in artikelnummern:
        vis+= "Artikelnummer '{}' {}x verkauft\n".format(code,amount_article_sold(customers, code))
    print(vis)
    # Ende Lösung

# Beispielaufruf:
print_article_sold(customers, articles)



print("\nAufgabe 8)")

def print_article_customer_hierarchy(kunden: list, artikelnummern: list) -> None:
    # Vervollständige die Funktion, um folgende Ausgabe mittels des Beispielaufrufs zu generieren: 
    # > 123010 Entchen:
    # >    Gemm Simpson
    # > 
    # > 123020 Tisch:
    # >    Gemm Simpson
    # >    Layton Ballard
    # >    Stefan Müller
    # > 
    # > 123030 Lampe:
    # >    Tyrone Simpson
    # > 
    # > 123040 Vase:
    # >    Tyrone Simpson
    # > 
    # > 123050 Stuhl:
    # >    Layton Ballard
    # >    Nathaniel Ochoa
    # > 
    # > 123070 Vase:
    # >    Layton Ballard
    # >    Jenson Gonzales
    # >

    # Anfang Lösung:
    # Alternative 1:
    vis =""
    for code,subject in articles.items():
        vis+= f"\n{code} {subject}:" \
              +"".join((f"\n{'':>4}" 
                        +customer["name"] 
                        +" " 
                        +customer["nachname"]  
                        for customer in customers  
                        if code in customer["artikelnummern"])) \
              +"\n"
    print(vis)
    # Alternative 2:
    # artikelnummern_gesamt = set()
    # for kunde in kunden:
    #     artikelnummern_gesamt.update(kunde['artikelnummern'])

    # Alternative 3:
    #artikelnummern_gesamt = {artikelnummer for kunde in kunden for artikelnummer in kunde['artikelnummern']}
    #print(artikelnummern_gesamt)
   # Ende Lösung

# Beispielaufruf:
print_article_customer_hierarchy(customers, articles)
