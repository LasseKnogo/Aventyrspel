import random as rand


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
                    print("Du hittar en kista")
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
                    print("Du hittar en kista")
                    kistslump = rand.randint(1, 3)
                    if kistslump == 1:
                        print("Du hittade ett vapen")
                        svardslump = rand.randint(1, 10)
                        if svardslump < 6:

                            print("Du hittade ett vanlig svärd")
                        elif svardslump < 9:

                            print("Du hitta ett sällsynt svärd")
                        else:

                            print("Du hittade ett mytiskt svärd")

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
                    print("Du hittar en kista")
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

        if svar == "h":
            if potion == 0:
                print("Du har inga pottor kvar")
            else:
                print("Du har tar en Healing Potta")
                potion = potion - 1
                hp = hp + 60


main()
