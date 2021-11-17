def main():

    alive = True
    svar = ""
    hp = 100
    level = 1
    potion = 1

    while alive:
        svar = input("Vad vill du göra [d], [i], [s], [h] -->")
        if hp == 0:
            alive = False

        if svar == "i":
            print(f" Du har {potion} Healing Pottor")

        if svar == "s":
            print(f"HP:{hp}")
            print(f"Level:{level}")

        if svar == "h":
            if potion == 0:
                print("Du har inga pottor kvar")
            else:
                print("Du har tar en Healing Potta")
                potion = potion - 1
                hp = hp + 10


main()
