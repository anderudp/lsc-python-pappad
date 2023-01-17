# Fő változók
player_hp = 100  # Játékos életereje
items = []  # Begyűjtött tárgyak
visited_rooms = []  # Meglátogatott szobák
game_won = False

# Szobákhoz kapcsolódó globális változók
solution = 3254
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
decoder_used = False

# Előkészületek
print("Szobaválasztáskor 0-t megadva beléphetsz a menübe.")
print("Felébredsz egy mély álomból. Félhomály van, de látsz magad körül. Mintátlan betonfalak vesznek körbe. ", end="")

# Szobaválasztás
while player_hp > 0 and not game_won:
    print()
    current_room = input("Melyik szobába lépsz be?\n")

    # Menü
    if current_room == "0":
        print(f"Életerőd: {player_hp}")
        print(f"Begyűjtött tárgyak: {', '.join(items)}")

    # 1-es szoba
    elif current_room == "1":
        if current_room in visited_rooms:
            print("Bekapcsolod a lámpádat, és megvizsgálod a kőoltárt. A bevésett minta: OOOEENKX")
        else:
            player_choice = input("Kinyitod az 1-es ajtót, és teljes sötétség fogad. Belépsz a szobába? (i/n)")
            if player_choice == "n":
                print("Becsukod az ajtót, és visszatérsz az előszobába.")
            elif player_choice == "i":
                if "flashlight" in items:
                    print("""Bekapcsolod a zseblámpád, és megvizsgálod a szobát. Nedves, mohafödte kőfalak vesznek körbe. 
                    Egy bányában ragadtál talán? Előtted omladozó, töredezett márványoszlopok, és azok törmeléke fekszik. 
                    Egy ókori szentély elemeiként azonosítod őket. Középen megpillantasz egy kőoltárt. 
                    Az alábbi minta van belemetszve: OOOEENKX""")
                    visited_rooms.append(current_room)
                else:
                    print("Belépsz a szobába. Sötét van, a levegő hideg és nyirkos. "
                          "Megpróbálsz egy kapcsolót keresni.\nMegbotlasz valami keményben, és bevered a térded. "
                          "Veszítesz 10 életerőt.")
                    player_hp -= 10
            else: # Ez nincs rajta a döntési fán
                print("Nem tudtál rendesen válaszolni egy igen-nem kérdésre. Veszítesz 5 életerőt.")
                player_hp -= 5
            if player_hp > 0:
                print("Becsukod az ajtót, és visszatérsz az előszobába.")

    # 2-es szoba
    elif current_room == "2":
        if current_room in visited_rooms:
            print("A Caesar-masina megállt az MMMCCLICV kódon. Vajon mit jelenthet?")
        else:
            if not decoder_used:
                print("A szobában egy bizarr márványszobrot pillantasz meg. Julius Caesar melllszobra vicsorít rád, fogai helyén nyolc darab nyolc-szegmenses kijelzővel. "
                      "\nBal füléből egy 25 állapotú tekerőgomb lóg ki. A szobor aljazatánál egy billentyűzetet helyeztek el. ")
                decoder_used = True
            keep_using_decoder = True
            while keep_using_decoder:
                user_text = input("Milyen szöveget akarsz beütni?\n")
                user_shift = int(input("Mennyit adsz meg a tekerőgombon?\n"))
                result = ""
                for letter in user_text:
                    letter_alphabet_index = alphabet.find(letter.upper())
                    result += alphabet[letter_alphabet_index-user_shift]
                if result == "MMMCCLIV":
                    print("A masina csilingel egyet, és nem reagál a további bevitelre. A kapott kód: MMMCCLIV")
                    visited_rooms.append(current_room)
                    keep_using_decoder = False
                    print("Becsukod az ajtót, és visszatérsz az előszobába.")
                else:
                    print(f"A kapott kód: {result}. ", end="")
                    player_choice = input(" Megpróbálsz mást beírni? (i/n)")
                    if player_choice == "n":
                        print("Becsukod az ajtót, és visszatérsz az előszobába.")
                        keep_using_decoder = False
                    elif player_choice != "i":
                        print("Nem tudtál rendesen válaszolni egy igen-nem kérdésre. Veszítesz 5 életerőt.")
                        player_hp -= 5
                        if player_hp > 0:
                            print("Becsukod az ajtót, és visszatérsz az előszobába.")
                            keep_using_decoder = False