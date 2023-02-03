import random

# Definition der Pokemon-Klasse

sortindex = 0

class Pokemon:
        def __init__(self, name, hp, speed, dp):
            self.name = name
            self.hp = hp
            self.speed = speed
            self.dp = dp

# Erzeugung Test-Mons und einfügen in Randomliste

pokelist = [
Pokemon("Nussasam", 100, 140, 20),
Pokemon("Stullkacku", 120, 120, 35),
Pokemon("Dumbidor", 60, 70, 25),
Pokemon("Strongitor", 200, 50, 50),
Pokemon("Nomitatos", 100, 100, 25)
]

tlpm = random.choice(pokelist)
tlpm2 = random.choice(pokelist)

print("Gewählte Pokemon:")
print("Pokemon mit Random-Antriff: " + tlpm.name)
print("Pokemon mit besten Antriff: " + tlpm2.name)

#Definiton der Kampf-Klasse

class Attack:
    def __init__(self, name, ap, acc, pp):
        self.name = name
        self.ap = ap
        self.acc = acc
        self.pp = pp
        self.avdmg = self.ap * (self.acc / 100)

#Erzeugung Test-Attacken und einfügen in Randomliste

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




ptwoattlist.sort(key=lambda Attack: Attack.avdmg, reverse=True)

bestatt = ptwoattlist[sortindex]






# Definition eines Standartkampfes, mit Acc.

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


# Kampfsimulation

# Randomisierte Auswahl der Pokemons

# Randomisierte Auswahl der Attacken

# Sortierung der Attacken nach Avdmg für die Greedy-KI

# Umzuschreiben des Codes die Änderungen nötig

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

if tlpm.hp <= 0:
    print(" ")
    print( "Bester Angriff hat mit " + tlpm2.name + " gewonnen")
else:
    print(" ")
    print( "Random-Angriff hat mit " + tlpm.name + " gewonnen")
