choices = ["rock", "paper", "sissors"]
wins = []
while True:
    answer = input("your turn: ")
    answer = answer.lower()
    import random
    move = random.choice(choices)
    print(f"computer turn: {move}")
    
    if move == answer:
        print("Draw!")
        wins.append("draw")
    elif move == "sissors" and answer == "paper":
        winner = "computer"
        wins.append(winner)
        print("computer wins")
    elif move == "sissors" and answer == "rock":
        winner = "you"
        wins.append(winner)
        print("you win")
    elif move == "rock" and answer == "paper":
        winner = "you"
        wins.append(winner)
        print("you win")
    elif move == "rock" and answer == "sissors":
        winner = "computer"
        wins.append(winner)
        print("computer wins")
    elif move == "paper" and answer == "rock":
        winner = "computer"
        wins.append(winner)
        print("computer wins")
    elif move == "paper" and answer == "sissors":
        winner = "you"
        wins.append(winner)
        print("you win")
    else:
        print("try again")
    if answer == "exit":
        
        print(f"""=============
game over!
=============     
your wins: {wins.count("you")}
computer wins: {wins.count("computer")}
draws: {wins.count("draw")}
              """)
        break
    