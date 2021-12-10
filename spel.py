import random as rand


class player():
    def __init__(self, klass, hp, damage, level, item):
        self.klass = klass
        self.hp = hp
        self.damage = damage
        self.level = level
        self.item = item


class monster():
    def __init__(self, name, health):
        self.name = name
        self.health = health


def main():
    character = ""
    alive = True
    svar = ""
    hp = 100
    damage = 50
    level = 1
    potion = 1
    weapon = ""
    character = input("vilken klass vill du välja? [ranger], [warrior]")
    if character == "ranger":
        hp = 80
        damage = 60
        weapon = "en simpel pilbåge"
    if character == "warrior":
        hp = 100
        damage = 40
        weapon = "ett simpelt svärd"
    while alive:

        svar = input(
            "Vad vill du göra? öppna en dörr [d],öpnna inventory [i],kolla stats [s],använd healing potta [h] -->")

        if svar == "d":
            door = input(
                "Vilken dörr vill du ta vänster[l], mitten[m], höger[r] ")
            if door == "l":
                slumptal = rand.randint(1, 3)
                if slumptal == 1:
                    kistslump = rand.randint(1, 3)
                    print("Du hittar en kista")
                    if kistslump == 1:
                        if character == "warrior":
                            svardslump = rand.randint(1, 10)
                            if svardslump < 6:

                                print(
                                    "Du hittade ett vanligt svärd, din skada ökar med 5!")
                                damage = damage + 5
                                weapon = "Vanligt svärd"
                            elif svardslump < 9:

                                print(
                                    "Du hitta ett sällsynt svärd, din skada ökar med 15!")
                                damage = damage + 15
                                weapon = "Sällsynt svärd"
                            else:

                                print(
                                    "Du hittade ett mytiskt svärd, din skada ökar med 25!")
                                damage = damage + 25
                                weapon = "Mytiskt svärd"
                    elif character == "ranger":
                        bågslump = rand.randint(1, 10)
                        if bågslump < 6:

                            print(
                                "Du hittade en vanlig pilbåge, din damage ökar med 10!")
                            damage = damage + 10
                            weapon = "Vanlig pilbåge"
                        elif bågslump < 9:

                            print(
                                "du hittade en sällsynt pilbåge, din damage ökar med 20!")
                            damage = damage + 20
                            weapon = "Sällsynt pilbåge"
                        else:

                            print(
                                "Du hittade en mytisk pilbåge, din damage ökar med 40!")
                            damaga = damaga + 40
                            weapon = "Mytisk pilbåge"
                    elif kistslump == 2:

                        print("Du hittade en halväten burk ravioli")
                        svar = input("Vill du äta raviolin? Ja[ja], Nej[nej]")
                        if svar == "j":
                            raviolislump = rand.randint(1, 2)
                            if raviolislump == 1:
                                print(
                                    "Du äter raviolin och känner en konstig smak, din hp minskar med 30")
                                hp = hp - 30
                            elif raviolislump == 2:
                                print(
                                    "Du äter ravilolin, den smakar udda men du känner dig mättad, din hp ökar med 30")
                                hp = hp + 30
                    elif kistslump == 3:

                        print("Du hittade en bit utrustning")
                        klädslump = rand.randint(1, 10)
                        if klädslump < 6:

                            print(
                                "du hittade en vanlig bit utrustning, din hp ökar med 10!")
                            hp = hp + 10
                        elif klädslump < 9:

                            print(
                                "du hittade en sällsynt bit utrustning, din hp ökar med 20!")
                            hp = hp + 20
                        else:

                            print(
                                "du hittade en ett mytisk bit utrustning, din damage ökar med 40!")
                            hp = hp + 40
                elif slumptal == 2:
                    monsterslump = rand.randint(1, 3)
                    if monsterslump == 1:
                        groda = 100
                        fightstats = hp + damage
                        print(f"Du möter en groda med {groda}hp")
                        if fightstats > groda:
                            print("Du dödade grodan")
                        else:
                            hp = hp - 50
                            print("Du blev skadad för 50hp")

                    elif monsterslump == 2:
                        fightstats = hp + damage
                        stenbumling = 150
                        print(f"Du stöter på en stenjätte med {stenbumling}hp")
                        if fightstats > stenbumling:
                            print("Du slaktar stenjätten")
                        else:
                            hp = hp - 75
                            print("Du blev skadad för 75hp")
                    else:
                        fightstats = hp + damage
                        draksatan = 200
                        print(
                            f"Du stöter på en massiv drake med {draksatan}hp")
                        if fightstats > draksatan:
                            print("Du dödar draken")
                        else:
                            hp = hp - 125
                            print("Du blev skadad för 125hp")
                else:
                    print("Du gick in i en fälla, du förlorar 40 hp")
                    hp = hp - 40
            if door == "m":
                slumptal = rand.randint(1, 3)
                if slumptal == 1:
                    kistslump = rand.randint(1, 3)
                    print("Du hittar en kista")
                    if kistslump == 1:
                        if character == "warrior":
                            svardslump = rand.randint(1, 10)
                            if svardslump < 6:

                                print(
                                    "Du hittade ett vanligt svärd, din damage ökar med 5!")
                                damage = damage + 5
                                weapon = "Vanligt svärd"
                            elif svardslump < 9:

                                print(
                                    "Du hitta ett sällsynt svärd, din damage ökar med 15!")
                                damage = damage + 15
                                weapon = "Sällsynt svärd"
                            else:

                                print(
                                    "Du hittade ett mytiskt svärd, din damage ökar med 25!")
                                damage = damage + 25
                                weapon = "Mytiskt svärd"
                    elif character == "ranger":
                        bågslump = rand.randint(1, 10)
                        if bågslump < 6:

                            print(
                                "Du hittade en vanlig pilbåge, din damage ökar med 10!")
                            damage = damage + 10
                            weapon = "Vanlig pilbåge"
                        elif bågslump < 9:

                            print(
                                "du hittade en sällsynt pilbåge, din damage ökar med 20!")
                            damage = damage + 20
                            weapon = "Sällsynt pilbåge"
                        else:

                            print(
                                "Du hittade en mytisk pilbåge, din damage ökar med 40!")
                            damage = damage + 40
                            weapon = "Mytisk pilbåge"
                    elif kistslump == 2:
                        print("du hittade en halväten burk ravioli")
                        svar = input("Vill du äta raviolin? Ja[ja], Nej[nej]")
                        if svar == "j":
                            raviolislump = rand.randint(1, 2)
                        if raviolislump == 1:
                            print(
                                "Du äter raviolin och känner en konstig smak, din hp minskar med 30")
                            hp = hp - 30
                        elif raviolislump == 2:
                            print(
                                "Du äter ravilolin, den smakar udda men du känner dig mättad, din hp ökar med 30")
                            hp = hp + 30

                    elif kistslump == 3:
                        print("Du hittade en bit utrustning")
                        klädslump = rand.randint(1, 10)
                        if klädslump < 6:

                            print(
                                "du hittade en vanlig bit utrusting, din hp ökar med 10!")
                            hp = hp + 10
                        elif klädslump < 9:

                            print(
                                "du hittade en sällsynt bit utrustning, din hp ökar med 20!")
                            hp = hp + 20
                        else:

                            print(
                                "du hittade en ett mytisk bit utrustning, din hp ökar med 40!")
                            hp = hp + 40
                elif slumptal == 2:
                    monsterslump = rand.randint(1, 3)
                    if monsterslump == 1:
                        groda = 100
                        fightstats = hp + damage
                        print(f"Du möter en groda med {groda}hp")
                        if fightstats > groda:
                            print("Du dödade grodan")
                        else:
                            hp = hp - 50
                            print("Du blev skadad för 50hp")

                    elif monsterslump == 2:
                        fightstats = hp + damage
                        stenbumling = 150
                        print(f"Du stöter på en stenjätte med {stenbumling}hp")
                        if fightstats > stenbumling:
                            print("Du slaktar stenjätten")
                        else:
                            hp = hp - 75
                            print("Du blev skadad för 75hp")
                    else:
                        fightstats = hp + damage
                        draksatan = 200
                        print(
                            f"Du stöter på en massiv drake med {draksatan}hp")
                        if fightstats > draksatan:
                            print("Du dödar draken")
                        else:
                            hp = hp - 125
                            print("Du blev skadad för 125hp")
                else:
                    print("Du gick in i en fälla, du förlorar 40 HP")
                    hp = hp - 40
            if door == "r":
                slumptal = rand.randint(1, 3)
                if slumptal == 1:
                    kistslump = rand.randint(1, 3)
                    print("Du hittar en kista")
                    if kistslump == 1:
                        if character == "warrior":
                            svardslump = rand.randint(1, 10)
                            if svardslump < 6:

                                print(
                                    "Du hittade ett vanlig svärd, din damage ökar med 5!")
                                damage = damage + 5
                                weapon = "Vanligt svärd"
                            elif svardslump < 9:

                                print(
                                    "Du hitta ett sällsynt svärd, din damage ökar med 15!")
                                damage = damage + 15
                                weapon = "Sällsynt svärd"
                            else:

                                print(
                                    "Du hittade ett mytiskt svärd, din damage ökar med 25!")
                                damage = damage + 25
                                weapon = "Mytiskt svärd"
                    elif character == "ranger":
                        bågslump = rand.randint(1, 10)
                        if bågslump < 6:

                            print(
                                "Du hittade en vanlig pilbåge din, damage ökar med 10!")
                            damage = damage + 10
                            weapon = "Vanlig pilbåge"
                        elif bågslump < 9:

                            print(
                                "du hittade en sällsynt pilbåge, din damage ökar med 15!")
                            damage = damage + 15
                            weapon = "Sällsynt pilbåge"
                        else:

                            print(
                                "Du hittade en mytisk pilbåge, din damage ökar med 40!")
                            damage = damage + 40
                            weapon = "Mytisk pilbåge"
                    elif kistslump == 2:

                        print("Du hittade en halväten burk ravioli")
                        svar = input("Vill du äta raviolin? Ja[ja] Nej[nej]")

                        if svar == "ja":
                            raviolislump = rand.randint(1, 2)

                            print(raviolislump)
                            if raviolislump == 1:
                                print(
                                    "Du äter raviolin och känner en konstig smak, din hp minskar med 30")
                                hp = hp - 30
                            elif raviolislump == 2:
                                hp = hp + 30
                                print(
                                    "Du äter ravilolin, den smakar udda men du känner dig mättad, din hp ökar med 30")

                    elif kistslump == 3:

                        print("Du hittade en bit utrustning")
                        klädslump = rand.randint(1, 10)
                        if klädslump < 6:

                            print(
                                "Du hittade en vanlig bit utrustning, din hp ökar med 10!")
                            hp = hp + 10
                        elif klädslump < 9:

                            print(
                                "du hittade en sällsynt bit utrustning, din hp ökar med 20!")
                            hp = hp + 20
                        else:

                            print(
                                "du hittade en ett mytisk bit utrustning, din hp ökar med 40!")
                            hp = hp + 40
                elif slumptal == 2:
                    monsterslump = rand.randint(1, 3)
                    if monsterslump == 1:
                        groda = 100
                        fightstats = hp + damage
                        print(f"Du möter en groda med {groda}hp")
                        if fightstats > groda:
                            print("Du dödade grodan")
                        else:
                            hp = hp - 50
                            print("Du blev skadad för 50hp")

                    elif monsterslump == 2:
                        fightstats = hp + damage
                        stenbumling = 150
                        print(f"Du stöter på en stenjätte med {stenbumling}hp")
                        if fightstats > stenbumling:
                            print("Du slaktar stenjätten")
                        else:
                            hp = hp - 75
                            print("Du blev skadad för 75hp")
                    else:
                        fightstats = hp + damage
                        draksatan = 200
                        print(
                            f"Du stöter på en massiv drake med {draksatan}hp")
                        if fightstats > draksatan:
                            print("Du dödar draken")
                        else:
                            hp = hp - 125
                            print("Du blev skadad för 125hp")
                else:
                    print("Du gick in i en fälla, du förlorar 40 HP")
                    hp = hp - 40
        if hp < 0:
            alive = False
            print("Du dog")

        if svar == "i":
            print(f" Du har {potion} Healing Pottor")
            print(f" Du har {weapon}")
        if svar == "s":
            print(f"HP:{hp}")
            print(f"damage:{damage}")
            print(f"Level:{level}")
            print(f"Klass:{character}")

        if svar == "h":
            if potion == 0:
                print("Du har inga pottor kvar")
            else:
                print("Du har tar en Healing Potta")
                potion = potion - 1
                hp = hp + 60


main()
