import os
import sys
import time


# functies
def clear_terminal(): # clear logic from bagely v3
    if sys.platform.startswith('win'):
        os.system('cls')
    elif sys.platform.startswith('linux') or sys.platform.startswith('darwin'):
        os.system('clear')
    else:
        print("[ERROR] Unsupported operating system. Please clear the terminal manually.")


def aantal_kluizen_vrij():
    with open("kluizen.txt", "r") as txt:
        num_lines = sum(1 for _ in txt)

    return 12 - num_lines


def nieuwe_kluis():
    vrije_kluizen = []

    for i in range(1, 13):
        vrije_kluizen.append(i)

    with open("kluizen.txt", "r") as txt:
        for regel in txt:
            kluisnummer = int(regel.split(";")[0])

            if kluisnummer in vrije_kluizen:
                vrije_kluizen.remove(kluisnummer)

    if len(vrije_kluizen) == 0:
        return -2

    print(f"Kluisje {vrije_kluizen[0]} is vrij, voer een code in.")
    pincode = input("> ")

    if ";" in pincode:
        return -1

    if len(pincode) < 4:
        return -1

    with open("kluizen.txt", "a") as txt:
        txt.write(f"{vrije_kluizen[0]};{pincode}\n")

    return vrije_kluizen[0]


def kluis_openen():
    print("wat is je kluisjesnummer?")
    u_sel_kluisnummer = input("> ")

    print("wat is je code?")
    u_sel_code = input("> ")

    with open("kluizen.txt", "r") as txt:
        for regel in txt:
            if regel.strip() == f"{u_sel_kluisnummer};{u_sel_code}":
                return True

    return False


def kluis_teruggeven():
    print("wat is je kluisjesnummer?")
    u_sel_kluisnummer = input("> ")

    print("wat is je code?")
    u_sel_code = input("> ")

    with open("kluizen.txt", "r") as txt:
        regels = txt.readlines()

    gevonden = False

    with open("kluizen.txt", "w") as txt:
        for regel in regels:
            if regel.strip() == f"{u_sel_kluisnummer};{u_sel_code}":
                gevonden = True
            else:
                txt.write(regel)

    return gevonden


# main loop
while True:
    print("""1: Ik wil weten hoeveel kluizen nog vrij zijn
2: Ik wil een nieuwe kluis
3: Ik wil even iets uit mijn kluis halen
4: Ik geef mijn kluis terug
5: Ik wil het programma afsluiten""")

    keuze = input("> ")

    if keuze == "1":
        i = aantal_kluizen_vrij()

        if i == 0:
            print("Er zijn geen kluisjes vrij!")
        elif i == 1:
            print("Er is nog 1 kluisje vrij!")
        else:
            print(f"Er zijn nog {i} kluisjes vrij")

        time.sleep(2.5)
        clear_terminal()

    elif keuze == "2":
        if aantal_kluizen_vrij() == 0:
            print("Er zijn geen kluisjes vrij!")
        else:
            resultaat = nieuwe_kluis()

            if resultaat == -1:
                print("Ongeldige code!")

            elif resultaat == -2:
                print("Er zijn geen kluisjes vrij!")

            else:
                print(f"Combinatie opgeslagen als: {resultaat}")

        time.sleep(2.5)
        clear_terminal()

    elif keuze == "3":
        gevonden = kluis_openen()
        print(gevonden)

        time.sleep(2.5)
        clear_terminal()

    elif keuze == "4":
        gevonden = kluis_teruggeven()
        print(gevonden)

        time.sleep(2.5)
        clear_terminal()

    elif keuze == "5":
        print("Programma afgesloten.")
        break

    else:
        print(f"{keuze} is geen geldige keuze!")

        time.sleep(2.5)
        clear_terminal()