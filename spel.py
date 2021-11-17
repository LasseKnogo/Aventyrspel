import random as rand


def main():

    alive = True
    svar = ""
    HP = 100
    level = 1
    AP = 100
    potion = 1

    while alive:
        svar = input("Vad vill du göra [d], [i], [s], [h] -->")
        if HP == 0:
            alive = False

        if svar == "d":
            door = input("Vilken dörr vill du ta [l], [m], [r] ")
            if door == "l":
                slumptal = rand.randint(1, 3)
                if slumptal == 1:
                    print("Du hittar en kista")
                elif slumptal == 2:
                    print("Du hittar en läskig kille")
                else:
                    print("Du gick in i en fälla")
            if door == "m":
                slumptal = rand.randint(1, 3)
                if slumptal == 1:
                    print("Du hittar en kista")
                elif slumptal == 2:
                    print("Du hittar en läskig kille")
                else:
                    print("Du gick in i en fälla")
            if door == "r":
                slumptal = rand.randint(1, 3)
                if slumptal == 1:
                    print("Du hittar en kista")
                elif slumptal == 2:
                    print("Du hittar en läskig kille")
                else:
                    print("Du gick in i en fälla")

        if svar == "i":
            print(f" Du har {potion} Healing Pottor")

        if svar == "s":
            print(f"HP:{HP}")
            print(f"AP:{AP}")
            print(f"Level:{level}")

        if svar == "h":
            if potion == 0:
                print("Du har inga pottor kvar")
            else:
                print("Du har tar en Healing Potta")
                potion = potion - 1
                HP = HP + 10


main()
