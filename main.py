floor0 = ['nothing', 'sword', 'monster', 'stairs up', 'sword']
floor1 = ['stairs down', 'monster', 'stairs up', 'monster', 'sword']
floor2 = ['magic stone', 'stairs down', 'sword', 'boss monster', 'prize']
dungeon = [floor0, floor1, floor2]
items = []
user_room = 0
user_floor = 0
game_over = False
win = False
can_retreat = False

while game_over == False:
  command = input("Type in a command ")
  
  
  if command == "left":
    if dungeon[user_floor][user_room] == "monster" or dungeon[user_floor][user_room] == "boss monster":
      print("Use the commands 'fight' or 'retreat.")
      can_retreat = True
    else:
      if user_room - 1 >= 0:
        user_room = user_room - 1
      else:
        print("Can't go left anymore.")
           
  
  elif command == "right":
    if dungeon[user_floor][user_room] == "monster" or dungeon[user_floor][user_room] == "boss monster":
      break
    else:
      if user_room < 4:
        user_room = user_room + 1
      else:
        print("Can't go right anymore.")
      
  elif command == "up":
    if user_floor == 0 and user_room == 3:
      user_floor = user_floor + 1 
      user_room = 0
      print("You found stairs that go up.")
    elif user_floor == 1 and user_room == 2:
      user_floor = user_floor + 1 
      user_room = 1
      print("You found stairs that go up.")
    else:
      print("No stairs, can't go up.")

  elif command == "down":
    if user_floor == 1 and user_room == 0:
      user_floor = user_floor - 1
      user_room = 3
      print("You found stairs that go down.")
    elif user_floor == 2 and user_room == 1:
      user_floor = user_floor - 1 
      user_room = 2
    else:
      print("No stairs, can't go down.")
  elif command == "exit":
    break
  
  elif command == "retreat":
    if can_retreat == True:
      if user_floor == 0 or user_floor == 2:
        user_room = user_room - 1
        can_retreat = False
      else:
        user_room = user_room - 1
        can_retreat = False
    else:
      print("Nothing to retreat from.")
  
  elif command == "grab":
    if len(items) < 3:
      if dungeon[user_floor][user_room] == "sword":
        items.append("sword")
        print("You got a sword!")
        dungeon[user_floor][user_room] = "nothing"
      elif user_floor == 2 and user_room == 0:
        items.append("magic stones")
        print("You got magic stones!")
        dungeon[user_floor][user_room] = "nothing"
      elif dungeon[user_floor][user_room] == "prize":
        items.append("prize")
        print("You got the prize!")
        dungeon[user_floor][user_room] = "nothing"
        game_over = True
        win = True
      else:
        print("nothing")
    elif len(items) >= 3:
      print("You are holding the max amount of items.")
      
    
  
  elif command == "fight":
    if dungeon[user_floor][user_room] == "monster":
      if "sword" in items:
        print("You defeated the monster but you lost your sword")
        items.remove("sword")
        dungeon[user_floor][user_room] = "nothing"
      else: 
        print("You can't fight a monster without a sword.")
    elif dungeon[user_floor][user_room] == "boss monster":
      if "sword" in items and "magic stones" in items:
        print("You’ve slayed the boss monster with the sword and magic stone")
        dungeon[user_floor][user_room] = "nothing"
        items.remove("sword")
        items.remove("magic stones")
      else:
        print("You need a sword and magic stones to fight the boss monster")
    else:
      print("There is no monster here.")
  
  elif command == "quit":
    game_over = True
    win = False

if win == True:
  print("You Won!")
else:
  print("game over")
