choices = ["rock", "paper", "sissor"]
wins = []
while True:
    answer = input("your tuen: ")
    answer = answer.lower()
    import random
    move = random.choice(choices)
    print(move)
    
    
    if move == answer:
        print("Draw!")
        wins.append("draw")
    elif move == "sissor" and answer == "paper":
        winner = "cumputer"
        wins.append(winner)
        print("computer wins")
    elif move == "sissor" and answer == "rock":
        winner = "you"
        wins.append(winner)
        print("you win")
    elif move == "rock" and answer == "paper":
        winner = "you"
        wins.append(winner)
        print("you win")
    elif move == "rock" and answer == "sissor":
        winner = "cumputer"
        wins.append(winner)
        print("cumputer wins")
    elif move == "paper" and answer == "rock":
        winner = "cumputer"
        wins.append(winner)
        print("computer wins")
    elif move == "paper" and answer == "sissor":
        winner = "you"
        wins.append(winner)
        print("you win")
    if answer == "exit":
        
        print(f"""=============
game over!
=============     
your wins: {wins.count("you")}
computer wins: {wins.count("computer")}
draws: {wins.count("draw")}
              """)
        break