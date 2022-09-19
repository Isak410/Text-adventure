tau = 0
bandasje = 2
telefon = 1
hp = 100
hpmonster = 100 
pinner = 0



print("du er midt i skogen i en stormfull natt")
print("du ser ingenting men du hører en gren som knekker")
valg = input("a = investigere, b = løpe i motsatt retning, c = gå ned på knær å begynn å be")


if valg == "a":
    print("du går nærmere lyden, og du møter på et monster")
    print("du kommer i en slosskamp mot monsteret")
    valg1 = input("a = slåss, b = løp")

    if valg1 == "a":
        print("du begynner å slåsse, og den får inn et kraftig slag på deg")
        hp -= 50
        valg3 = input("a = slå tilbake, b = sette deg i fosterstilling")
        if valg3 == "a":
            print("du får et slag inn, men monsteret slår deg tilbake")
            hpmonster -=35
            hp -=50
            if hp < 1:
                print("du døde")

        if valg3 == "b":
            print("du setter deg i fosterstilling, og monsteret løper vekk")


    if valg1 == "b":
        print("du begynte å løpe, og telefonen din datt på bakken")
        
        valg2 = input("a = gå å plukke opp telefonen, b løpe videre")
        
        if valg2 == "a": 
            print ("du prøvde å plukke opp telefonen, og du fikk tak i den")
        if valg2 == "b":
            print ("du går fra telefonen, og den blir knust av monsteret")
            telefon -= 1





if valg == "b":
    print("Du begynner å løpe i motsatt retning")
    print("Du hører noe springe etter deg")
    print("Du ser et tau og du plukker det opp")
    tau += 1
    if tau == 1:
         print("du har nå et tau")
    Valg2 = input("a = stopp og aksepter at du ikke kommer deg hjem, b = ikke gi opp håpet og fortsett å løpe")

    if Valg2 == "a":
        print("Monsteret stoppet og står nå helt stille rett bak deg")

    if Valg2 == "b":
        print("du prøver å løpe videre, men monsteret tar deg igjen og du blir slått ned")



if valg == "c":
    print("du begynner å be og du ber helt til det blir dag og du kommer deg hjem trygt")


if hp < 1:
    print("du døde")


if telefon == 0:
    print("du prøver å nå etter telefonen for å få hjelp, når du innser at du mistet den når du slåss mot monsteret")
    print("du innser at du må prøve å finne ly før det blir mørkt i tilfelle monsteret kommer tilbake")
    valgly = input("a = prøv å finne veien ut av skogen, b = lete etter telefonen, c = begynne å lage en liten camp")

    if valgly == "a":
        print("du leter i flere timer etter utveien fra skogen, men")

    if valgly == "b":
        print("du går tilbake til der du slåss mot monsteret, og der ser du monsteret igjen")
        print("du kommer i en")

    if valgly == "c":
        print("du finner en liten plass som du bestemmer deg for å søke ly")
        print("du bygger en veldig liten hytte av noen pinner som du finner")
        print("nå som du har bygd hytten har du to valg")
        valghytte = input("a = lete etter mat, b = prøve å sove")

        if valghytte == "a":
            print("du går ut av hytten for å lete etter mat")




























