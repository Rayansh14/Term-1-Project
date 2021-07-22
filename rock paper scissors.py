import random

score = 0

def generate_random():
    return random.choice(["rock", "paper", "scissors"])


def is_valid(user_move):
    if user_move in ["rock", "paper", "scissors", "r", "p", "s"]:
        return True
    return False


def result(comp_move, user_move):
    if comp_move == "rock":
        if user_move == "rock" or user_move == "r":
            return "tie"
        elif user_move == "paper" or user_move == "p":
            return "user"
        elif user_move == "scissors" or user_move == "s":
            return "comp"
        
    elif comp_move == "paper":
        if user_move == "rock" or user_move == "r":
            return "comp"
        elif user_move == "paper" or user_move == "p":
            return "tie"
        elif user_move == "scissors" or user_move == "s":
            return "user"
        
    elif comp_move == "scissors":
        if user_move == "rock" or user_move == "r":
            return "user"
        elif user_move == "paper" or user_move == "p":
            return "comp"
        elif user_move == "scissors" or user_move == "s":
            return "tie"


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
print("write 'quit' to terminate")
print("Score: 0\n")

while True:

    user_input = input("What's your move: ").lower()
    if user_input == "quit":
        break
    if not is_valid(user_input):
        print("Invalid Move")
        print("Your possible moves are: rock, paper, scissors, r, p or s\n")
        continue
    comp_choice = generate_random()

    scorekeeper(comp_choice, user_input)

    print()
