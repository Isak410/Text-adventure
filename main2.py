#globale variabler
penger = 100



def Inngang():
    print("du våkner opp i et rom og du ser tre dører foran deg, en blå, en rød og en grønn")
    asking = True
    while asking == True:
        førstedør = input("A = Rød dør, B = Blå dør, C = Grønn dør")
        if førstedør == "A":
            Rød1()
        if førstedør == "B":
            Blå1()
        if førstedør == "C":
            Grønn1()
        else:
            print("Du har skrevet feil")



def Rød1():
    global penger
    print("når du har gått igjennom den røde døren ser du en vareautomat")
    print("du blir plutselig veldig tørst, og du bestemmer deg for å kjøpe deg noe godt å drikke")
    vareautomat = input("A = Cola 55kr , B = Sprite 25kr , C = Fanta 20kr ->")
    if vareautomat == "A":
        global penger
        penger -= 55
        print("du har", penger, "kroner igjen")
        Cola()
    if vareautomat == "B":
        penger -= 25
        print("du har", penger, "kroner igjen")
        Sprite()
    if vareautomat == "C":
        penger -= 20
        print("du har", penger, "kroner igjen")
        Fanta()

def Blå1():
    print("du prøver å åpne den blåe døren, men den rører seg ikke")
    print("du bestemmer deg for å prøve en annen dør")
    retry = input("A = Rød dør, B = Grønn dør")
    if retry == "A":
        Rød1()
    if retry == "B":
        Grønn1()

def Grønn1():
    print("når du åpner den grønne døren står det en lav mann med langt grått sjegg")
    print("du aner ikke hva du skal gjøre, så du bestemmer deg for å stille han et spørsmål")
    spørsmål1 = input("A = hvor er jeg?, B = hvem er du?")
    if spørsmål1 == "A":
        print("han svarer med at du er i en drøm, og at alt du trenger å gjøre for å våkne er å drikke den svarte eliksir")
        svarteeliksir = input("A = Rød dør, B = Blå dør")
        if svarteeliksir == "A":
            Rød1()
        if svarteeliksir == "B":
            Blå1()
    if spørsmål1 == "B":
        print("Han svarer med 'jeg er drømmemannen'")
        print("'Jeg er her for å lede deg gjennom drømmen din' sier han")
        print("du skjønner ingenting, og bestemmer deg for å velge en annen dør")
        svarteeliksir = input("A = Rød dør, B = Blå dør")
        if svarteeliksir == "A":
            Rød1()
        if svarteeliksir == "B":
            Blå1()



def Cola():
    print("du tar en slurk av colaen, og du besvimer og våkner opp hjemme i sengen din")
    Goodend()

def Fanta():
    print("Når du trykker på fantaen skjer det ingen ting")
    print("du bestemmer deg for å velge en annen drikke")
    fantaretry = input("A = Cola, B = Sprite")
    if fantaretry == "A":
        Cola()
    if fantaretry == "B":
        Sprite()

def Sprite():
    print("du drakk litt av spriten, og du detter på bakken og dør")
    End()



def End():
    print("du døde")
    end = input("A = prøv på nytt, B = Avslutt spill")
    if end == "A":
        Inngang()
    if end == "B":
        exit

def Goodend():
    print("gratulerer, du klarte spillet")
    goodend = input("A = Spill på nytt, B = Avslutt spill")
    if goodend == "A":
        Inngang()
    if goodend == "B":
        exit





Inngang()


















