
board = ["  ", "1", "2", "3",
         "1 ", "-", "-", "-",
         "2 ", "-", "-", "-",
         "3 ", "-", "-", "-"]
player_1_turn = True
have_winner = False
while not have_winner:
    # Játéktér kiírása
    for i in range(0, 13, 4):
        print(board[i] + '|' + board[i + 1] + "|" + board[i + 2] + "|" + board[i + 3] + "|")
    if player_1_turn:
        print("Az első játékos jön.")
    else:
        print("A második játékos jön.")
    new_place = False
    while not new_place:
        # Hely bekérése, ellenőrzése
        row = column = 10
        while not 1 <= row <= 3:
            row = int(input("Add meg a sor számát:\n"))
        while not 1 <= column <= 3:
            column = int(input("Add meg az oszlop számát:\n"))
        if board[4 * row + column] == "-":
            new_place = True
    # Játékos szimbólumának lerakása
    if player_1_turn:
        board[4 * row + column] = "o"
    else:
        board[4 * row + column] = "x"
    # Sorok ellenőrzése
    if board[5] == board[6] == board[7] != "-":
        if player_1_turn:
            print("Első játékos nyert!")
        else:
            print("Második játékos nyert!")
        have_winner = True

    if board[9] == board[10] == board[11] != "-":
        if player_1_turn:
            print("Első játékos nyert!")
        else:
            print("Második játékos nyert!")
        have_winner = True

    if board[13] == board[14] == board[15] != "-":
        if player_1_turn:
            print("Első játékos nyert!")
        else:
            print("Második játékos nyert!")
        have_winner = True

    # Oszlopok ellenőrzése
    if board[5] == board[9] == board[13] != "-":
        if player_1_turn:
            print("Első játékos nyert!")
        else:
            print("Második játékos nyert!")
        have_winner = True

    if board[6] == board[10] == board[14] != "-":
        if player_1_turn:
            print("Első játékos nyert!")
        else:
            print("Második játékos nyert!")
        have_winner = True

    if board[7] == board[11] == board[15] != "-":
        if player_1_turn:
            print("Első játékos nyert!")
        else:
            print("Második játékos nyert!")
        have_winner = True

    # Átlók ellenőrzése
    if board[5] == board[10] == board[15] != "-":
        if player_1_turn:
            print("Első játékos nyert!")
        else:
            print("Második játékos nyert!")
        have_winner = True

    if board[7] == board[10] == board[13] != "-":
        if player_1_turn:
            print("Első játékos nyert!")
        else:
            print("Második játékos nyert!")
        have_winner = True

    # Döntetlen
    if not have_winner and "-" not in board:
        have_winner = True
        print("Döntetlen.")

    # Játékosváltás
    if not have_winner:
        if player_1_turn:
            player_1_turn = False
        else:
            player_1_turn = True

for i in range(0, 13, 4):
    print(board[i] + '|' + board[i + 1] + "|" + board[i + 2] + "|" + board[i + 3] + "|")