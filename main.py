import random

# Definition der Pokemon-Klasse

class Pokemon:
        def __init__(self, name, hp, speed, dp):
            self.name = name
            self.hp = hp
            self.speed = speed
            self.dp = dp

# Erzeugung Test-Mons
nussasam = Pokemon("Nussasam", 100, 140, 20)
stullkacku = Pokemon("Stullkacku", 120, 120, 15)

#Definiton der Kampf-Klasse

class Attack:
    def __init__(self, name, ap, acc):
        self.name = name
        self.ap = ap
        self.acc = acc

#Erzeugung Test-Attacke
dumbhit = Attack("Dumbhit", 30, 50)


# Definition eines Standartkampfes, mit Acc.

def fightresult(def_hp : int , att_ap : int, def_dp : int, att_acc : int) -> int:
     hit : int
     rndresult : int
     rndresult = random.randint(1,100)
     print("Randomwert zum Test")
     print(rndresult)
     hit = rndresult - att_acc
     if hit < 0:
         def_hp = def_hp
     else:
         def_hp = def_hp - (att_ap - def_dp)
     return def_hp

# Kampfsimulation

if stullkacku.speed > nussasam.speed:
    while nussasam.hp > 0 and stullkacku.hp > 0:
        nussasam.hp = fightresult(nussasam.hp, dumbhit.ap, nussasam.dp, dumbhit.acc)
        print("HP " + nussasam.name)
        print(nussasam.hp)
        stullkacku.hp = fightresult(stullkacku.hp, dumbhit.ap, stullkacku.dp, dumbhit.acc)
        print("HP " + stullkacku.name)
        print(stullkacku.hp)
elif nussasam.speed > stullkacku.speed:
    while stullkacku.hp > 0 and nussasam.hp > 0:
        stullkacku.hp = fightresult(stullkacku.hp, dumbhit.ap, stullkacku.dp, dumbhit.acc)
        print("HP " + stullkacku.name)
        print(stullkacku.hp)
        nussasam.hp = fightresult(nussasam.hp, dumbhit.ap, nussasam.dp, dumbhit.acc)
        print("HP " + nussasam.name)
        print(nussasam.hp)
else:
    while nussasam.hp > 0 and stullkacku.hp > 0:
        nussasam.hp = fightresult(nussasam.hp, dumbhit.ap, nussasam.dp, dumbhit.acc)
        print("HP " + nussasam.name)
        print(nussasam.hp)
        stullkacku.hp = fightresult(stullkacku.hp, dumbhit.ap, stullkacku.dp, dumbhit.acc)
        print("HP " + stullkacku.name)
        print(stullkacku.hp)

if nussasam.hp == 0:
    print( stullkacku.name + " hat gewonnen")
else:
    print( nussasam.name + " hat gewonnen")
