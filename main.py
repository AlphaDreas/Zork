location = [
[" ", " ", " "],
[" ", " ", " "],
[" ", " ", " "]
]


Player1 = input("What is player X's name? ")
Player2 = input("What is player O's name? ")

U1Q = "It is currently " + Player1 + "'s turn"
U2Q = "It is currently " + Player2 + "'s turn"


turn = 1
while turn <= 9:
  if turn%2 == 1:
    print(U1Q)
    answer1 = int(input("What row would you like to mark? "))
    answer2 = int(input("What column would you like to mark? "))
    if location[answer1-1][answer2-1] == "X":
      print(Player1 + " that spot has already been taken")
      U1Q = "Please pick again"
    elif location[answer1-1][answer2-1] == "O":
      print(Player1 + " that spot has already been taken")
      U1Q = "Please pick again"
    else: 
        location[answer1-1][answer2-1] = 'X'
        print(location[0][0] + '|' + location[0][1] + '|' + location[0][2])
        print("-----")
        print(location[1][0] + '|' + location[1][1] + '|' + location[1][2])
        print("-----")
        print(location[2][0] + '|' + location[2][1] + '|' + location[2][2])
        turn += 1
        U1Q = "It is currently " + Player1 + "'s turn"
        if location[0][0] == "X" and location[0][1] == "X" and location[0][2] == "X":
          print(Player1 + " won the game!")
          turn = 10
        elif location[1][0] == "X" and location[1][1] == "X" and location[1][2] == "X":
          print(Player1 + " won the game!")
          turn = 10 
        elif location[2][0] == "X" and location[2][1] == "X" and location[2][2] == "X":
          print(Player1 + " won the game!")
          turn = 10
        elif location[0][0] == "X" and location[1][0] == "X" and location[2][0] == "X":
          print(Player1 + " won the game!")
          turn = 10
        elif location[0][1] == "X" and location[1][1] == "X" and location[2][1] == "X":
          print(Player1 + " won the game!")
          turn = 10
        elif location[0][2] == "X" and location[1][2] == "X" and location[2][2] == "X":
          print(Player1 + " won the game!")
          turn = 10
        elif location[0][0] == "X" and location[1][1] == "X" and location[2][2] == "X":
          print(Player1 + " won the game!")
          turn = 10
        elif location[0][2] == "X" and location[1][1] == "X" and location[2][0] == "X":
          print(Player1 + " won the game!")
          turn = 10
        elif turn == 10:
          print("The Game ended in a tie!")
          
          
          
  else:
    print(U2Q)
    answer1 = int(input("What row would you like to mark? "))
    answer2 = int(input("What column would you like to mark? "))
    if location[answer1-1][answer2-1] == "X":
      print(Player2 + " that spot has already been taken")
      U2Q = "Please pick again"
    elif location[answer1-1][answer2-1] == "O":
      print(Player2 + " that spot has already been taken")
      U2Q = "Please pick again"
    else:
        location[answer1-1][answer2-1] = 'O'
        print(location[0][0] + '|' + location[0][1] + '|' + location[0][2])
        print("-----")
        print(location[1][0] + '|' + location[1][1] + '|' + location[1][2])
        print("-----")
        print(location[2][0] + '|' + location[2][1] + '|' + location[2][2])
        turn += 1
        U2Q = "It is currently " + Player2 + "'s turn"
        if location[0][0] == "O" and location[0][1] == "O" and location[0][2] == "O":
          print(Player2 + " won the game!")
        elif location[1][0] == "O" and location[1][1] == "O" and location[1][2] == "O":
          print(Player2 + " won the game!")
          turn = 10 
        elif location[2][0] == "O" and location[2][1] == "O" and location[2][2] == "O":
          print(Player2 + " won the game!")
          turn = 10
        elif location[0][0] == "O" and location[1][0] == "O" and location[2][0] == "O":
          print(Player2 + " won the game!")
          turn = 10
        elif location[0][1] == "O" and location[1][1] == "O" and location[2][1] == "O":
          print(Player2 + " won the game!")
          turn = 10
        elif location[0][2] == "O" and location[1][2] == "O" and location[2][2] == "O":
          print(Player2 + " won the game!")
          turn = 10
        elif location[0][0] == "O" and location[1][1] == "O" and location[2][2] == "O":
          print(Player2 + " won the game!")
          turn = 10
        elif location[0][2] == "O" and location[1][1] == "O" and location[2][0] == "O":
          print(Player2 + " won the game!")
          turn = 10
        elif turn == 10:
          print("The Game ended in a tie!")