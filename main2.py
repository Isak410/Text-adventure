#globale variabler
penger = 100
nøkkelrød = 0
nøkkelblå = 0




def Inngang():
    global penger
    print("du våkner opp i et rom og du ser tre dører foran deg, en blå, en rød og en grønn")
    print("På hver dør står det hva det koster å åpne den")
    Inngang1()
    
def Inngang1():
        print("rød dør har et nøkkelhull, den blåe koster koster 25, og den grønne koster 15kr")
        en()
    
def en():
    global penger, nøkkelblå, nøkkelrød
    asking = True
    while asking == True:
        Inngang2()


def Inngang2():
    global penger, nøkkelblå, nøkkelrød
    asking = True
    while asking == True:
        førstedør = input("A = Rød dør, B = Blå dør, C = Grønn dør -> ")
        if førstedør == "A":
            if nøkkelrød == 1:
                nøkkelrød -= 1
                Rød1()
            elif nøkkelrød == 0:
                print("du har ikke riktig nøkkel")
                en()    

        elif førstedør == "B":
            if nøkkelblå == 1:
                print("du åpner den blåe døren, og du finner en rød nøkkel inni")
                nøkkelblå -= 1
                nøkkelrød += 1
                en()
            elif nøkkelblå == 0:
                print("du har ikke riktig nøkkel")    
                en()        
        elif førstedør == "C":
            penger -= 15
            print("du har nå", penger, "kroner igjen")
            print("inni rommet fant du en blå nøkkel")
            nøkkelblå += 1
            en()

            print("du har", penger, "kroner igjen")
            Grønn1()
        else:
            print("Du har skrevet feil")



def Rød1():
    global penger
    print("når du har gått igjennom den røde døren ser du en vareautomat")
    print("du blir plutselig veldig tørst, og du bestemmer deg for å kjøpe deg noe godt å drikke")
    vareautomat = input("A = Cola 55kr , B = Sprite 25kr , C = Fanta 20kr -> ")
    if vareautomat == "A":
        penger -= 55
        if penger < 1:
            Blakk()
        else:
            print("du har", penger, "kroner igjen")
            Cola()
    if vareautomat == "B":
        penger -= 25
        if penger < 1:
            Blakk()
        else:
            print("du har", penger, "kroner igjen")
            Sprite()
    if vareautomat == "C":
        Fanta()

def Blå1():
    print("du prøver å åpne den blåe døren, men den rører seg ikke")
    print("du bestemmer deg for å prøve en annen dør")
    en()

def Grønn1():
    print("når du åpner den grønne døren står det en lav mann med langt grått sjegg")
    print("du aner ikke hva du skal gjøre, så du bestemmer deg for å stille han et spørsmål")
    spørsmål1 = input("A = hvor er jeg?, B = hvem er du? -> ")
    if spørsmål1 == "A":
        print("han svarer med at du er i en drøm, og at alt du trenger å gjøre for å våkne er å drikke den svarte eliksir")
        en()
    if spørsmål1 == "B":
        print("Han svarer med 'jeg er drømmemannen'")
        print("'Jeg er her for å lede deg gjennom drømmen din' sier han")
        print("du skjønner ingenting, og bestemmer deg for å velge en annen dør")
        en()



def Cola():
    print("du tar en slurk av colaen, og du besvimer og våkner opp hjemme i sengen din")
    Goodend()

def Fanta():
    print("Når du trykker på fantaen skjer det ingen ting")
    print("du bestemmer deg for å velge en annen drikke")
    fantaretry = input("A = Cola, B = Sprite -> ")
    if fantaretry == "A":
        Cola()
    if fantaretry == "B":
        Sprite()

def Sprite():
    print("du drakk litt av spriten, og du detter på bakken og dør")
    Enddead()


def Blakk():
    print("du er tom for penger")
    End()





def Endblakk():
    print("du gikk tom for penger")
    End()

def Enddead():
    print("du døde")
    End()
    
def End():
    global penger, nøkkelblå, nøkkelrød
    end = input("A = prøv på nytt, B = Avslutt spill -> ")
    if end == "A":
        penger = 100
        nøkkelblå = 0
        nøkkelrød = 0
        Inngang()
    if end == "B":
        exit()

def Goodend():
    print("gratulerer, du klarte spillet")
    goodend = input("A = Spill på nytt, B = Avslutt spill -> ")
    if goodend == "A":
        Inngang()
    if goodend == "B":
        exit()





Inngang()


















