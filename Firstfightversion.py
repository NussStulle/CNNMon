import random

#Festlegung des Indexes für

sortindex = 0

# Definition der Pokemon-Klasse

class Pokemon:
        def __init__(self, name, hp, speed, dp):
            self.name = name   #Name des Mons
            self.hp = hp        #Die Gesundheitspunkte
            self.speed = speed   #Angriffs-Geschwindigkeit
            self.dp = dp        #Verteidigungspunkte

# Erzeugung Test-Mons als Liste

pokelist = [
Pokemon("Nussasam", 100, 140, 20),
Pokemon("Stullkacku", 120, 120, 35),
Pokemon("Dumbidor", 60, 70, 25),
Pokemon("Strongitor", 200, 50, 50),
Pokemon("Nomitatos", 100, 100, 25)
]

#Random Auswahl der Mons je Spieler

tlpm = random.choice(pokelist)
tlpm2 = random.choice(pokelist)

print("Gewählte Pokemon:")
print("Pokemon mit Random-Antriff: " + tlpm.name)
print("Pokemon mit besten Antriff: " + tlpm2.name)

#Definiton der Kampf-Klasse

class Attack:
    def __init__(self, name, ap, acc, pp):
        self.name = name                #Name des Angriffes
        self.ap = ap                    #Angriffswert
        self.acc = acc                  #Genauigkeit
        self.pp = pp                    #Anzahl der Ausführungen
        self.avdmg = self.ap * (self.acc / 100)

#Erzeugung Test-Attacken und einfügen in Zwei Listen, damit die PP sich nicht  beeinflussen.

poneattlist = [
Attack("Dumbhit", 30, 50, 5),
Attack("Stronghit", 50, 60, 5),
Attack("Aimhit", 40, 90, 5),
Attack("Randompunch", 60, 20, 5)
]

ptwoattlist = [
Attack("Dumbhit", 30, 50, 5),
Attack("Stronghit", 50, 60, 5),
Attack("Aimhit", 40, 90, 5),
Attack("Randompunch", 60, 20, 5)
]


#Sortierung der Angriffe nach Durchschnittlichen Schaden

ptwoattlist.sort(key=lambda Attack: Attack.avdmg, reverse=True)

bestatt = ptwoattlist[sortindex]



# Definition eines Standartkampfes

def fightresult(def_hp : int , att_ap : int, def_dp : int, att_acc : int) -> int:
     hit : int
     rndresult : int
     rndresult = random.randint(1,100)
     print(" ")
     print("Würfelwert: ", rndresult)
     hit = (100 - att_acc) - rndresult
     if hit > 0:
         def_hp = def_hp
         print("Daneben")
     elif def_dp > att_ap:
         def_hp = def_hp
         print("Geblockt")
     else:
        def_hp = def_hp - (att_ap - def_dp)
        print("Treffer")
     return def_hp


# Kampfsimulation mit Bevorzogung des Schnelleren Mons

if tlpm.speed > tlpm2.speed:
    print("Random-Angriff beginnt")
    while tlpm.hp > 0 and tlpm2.hp > 0:
        rdmatt = random.choice(poneattlist)
        while rdmatt.pp == 0:
            rdmatt = random.choice(poneattlist)
        tlpm.hp = fightresult(tlpm.hp, rdmatt.ap, tlpm.dp, rdmatt.acc)
        rdmatt.pp = rdmatt.pp - 1
        print("Ramdom-Angriff mit: " + rdmatt.name + " Angriffswert: ", rdmatt.ap, "Angriffsgenauigkeit: ", rdmatt.acc, "Rest-PP: ", rdmatt.pp)
        print("HP: " + tlpm.name, tlpm.hp)
        if tlpm.hp > 0:
            bestatt = ptwoattlist[sortindex]
            tlpm2.hp = fightresult(tlpm2.hp, bestatt.ap, tlpm2.dp, bestatt.acc)
            if bestatt.pp == 0:
                sortindex = sortindex + 1
                bestatt = ptwoattlist[sortindex]
            bestatt.pp = bestatt.pp - 1
            print("Bester Angriff mit: " + bestatt.name + " Angriffswert: ", bestatt.ap, "Angriffsgenauigkeit: ", bestatt.acc, "Rest-PP: ", bestatt.pp)
            print("HP: " + tlpm2.name, tlpm2.hp)

elif tlpm2.speed > tlpm.speed:
    print("Bester Angriff beginnt")
    while tlpm.hp > 0 and tlpm2.hp > 0:
        bestatt = ptwoattlist[sortindex]
        tlpm2.hp = fightresult(tlpm2.hp, bestatt.ap, tlpm2.dp, bestatt.acc)
        if bestatt.pp == 0:
            sortindex = sortindex + 1
            bestatt = ptwoattlist[sortindex]
        bestatt.pp = bestatt.pp - 1
        print("Bester Angriff mit: " + bestatt.name + " Angriffswert: ", bestatt.ap, "Angriffsgenauigkeit: ", bestatt.acc, "Rest-PP: ", bestatt.pp)
        print("HP: " + tlpm2.name, tlpm2.hp)
        if tlpm2.hp > 0:
             rdmatt = random.choice(poneattlist)
             while rdmatt.pp == 0:
                 rdmatt = random.choice(poneattlist)
             tlpm.hp = fightresult(tlpm.hp, rdmatt.ap, tlpm.dp, rdmatt.acc)
             rdmatt.pp = rdmatt.pp - 1
             print("Random-Angriff mit: " + rdmatt.name + " Angriffswert: ", rdmatt.ap, "Angriffsgenauigkeit: ", rdmatt.acc, "Rest-PP: ", rdmatt.pp)
             print("HP: " + tlpm.name, tlpm.hp)
else:
    print("Random-Angriff beginnt")
    while tlpm.hp > 0 and tlpm2.hp > 0:
        rdmatt = random.choice(poneattlist)
        while rdmatt.pp == 0:
            rdmatt = random.choice(poneattlist)
        tlpm.hp = fightresult(tlpm.hp, rdmatt.ap, tlpm.dp, rdmatt.acc)
        rdmatt.pp = rdmatt.pp - 1
        print("Random-Angriff mit: " + rdmatt.name + " Angriffswert: ", rdmatt.ap, "Angriffsgenauigkeit: ", rdmatt.acc, "Rest-PP: ", rdmatt.pp)
        print("HP: " + tlpm.name, tlpm.hp)
        if tlpm.hp > 0:
            bestatt = ptwoattlist[sortindex]
            tlpm2.hp = fightresult(tlpm2.hp, bestatt.ap, tlpm2.dp, bestatt.acc)
            if bestatt.pp == 0:
                sortindex = sortindex + 1
                bestatt = ptwoattlist[sortindex]
            bestatt.pp = bestatt.pp - 1
            print("Bester Angriff mit: " + bestatt.name + " Angriffswert: ", bestatt.ap, "Angriffsgenauigkeit: ", bestatt.acc, "Rest-PP: ", bestatt.pp)
            print("HP: " + tlpm2.name, tlpm2.hp)

# Ausgabe wer gewonnen hat

if tlpm.hp <= 0:
    print(" ")
    print( "Bester Angriff hat mit " + tlpm2.name + " gewonnen")
else:
    print(" ")
    print( "Random-Angriff hat mit " + tlpm.name + " gewonnen")
