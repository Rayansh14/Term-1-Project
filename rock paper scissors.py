import random

score = 0

def generate_random():
    return random.choice(["rock", "paper", "scissors"])


def is_valid(user_move):
    if user_move in ["rock", "paper", "scissors", "r", "p", "s"]:
        return True
    return False


def result(comp_move, user_move):
    if comp_move == user_move:
        return "tie"
    
    if comp_move == "rock":
        if user_move == "paper":
            return "user"
        else:
            return "comp"
        
    elif comp_move == "paper":
        if user_move == "rock":
            return "comp"
        else:
            return "user"
        
    elif comp_move == "scissors":
        if user_move == "rock":
            return "user"
        else:
            return "comp"


def scorekeeper(comp_choice, user_input):
    global score
    my_result = result(comp_choice, user_input)
    
    if my_result == "user":
        print(f"You chose {user_input} and the computer chose {comp_choice}, so you won.")
        score += 1
        print(f"Score: {score}")
    elif my_result == "comp":
        print(f"You chose {user_input} and the computer chose {comp_choice}, so you lost.")
        score -= 1
        print(f"Score: {score}")
    elif my_result == "tie":
        print(f"You chose {user_input} and the computer chose {comp_choice}, so it was a tie.")
        print(f"Score: {score}")

print("This is a game of Rock-Paper-Scissors")
print("Your possible moves are: rock, paper, scissors, r, p or s")
print("Write 'quit' to terminate")
print("Score: 0\n")

while True:

    user_input = input("What's your move: ").lower()
    if user_input == "quit":
        if score < 0:
            print(f"The Computer won by {score} points!")
        elif score > 0:
            print(f"Congratulations! You won by {score} points!")
        else:
            print("The game was a tie!")
        break
    if not is_valid(user_input):
        print("Invalid Move")
        print("Your possible moves are: rock, paper, scissors, r, p or s\n")
        continue
    
    if user_input == "r":
        user_input = "rock"
    elif user_input == "s":
        user_input = "scissors"
    else:
        user_input = "paper"
        
    comp_choice = generate_random()

    scorekeeper(comp_choice, user_input)

    print()
