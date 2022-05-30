import random

# Generate a random answer
def generate_answer():
    answer = random.randint(1, 3)
    if answer == 1:
       answer = "rock"
    elif answer == 2:
       answer = "paper"
    elif answer == 3:
       answer = "scissors"
    return answer

# Get the user input and check if it is a valid input
def get_input():
    while True:
        user_input = input("Please select one of 'rock', 'paper', or 'scissors'").lower()
        if user_input == "rock" or user_input == "paper" or user_input == "scissors":
           return user_input
        else:
           print("Invalid input. Please select one of 'rock', 'paper', or 'scissors'")
           continue
        
def check_ans(rounds):
    # Record how many times that the user and the computer win seperately
    user_wins = 0
    com_wins = 0
                 
    while rounds > 0:
        answer = generate_answer()
        user_input = get_input()
        rounds -= 1
        # Check whether the user or the computer win until rounds become 0
        if user_input == answer:
            print("It is a tie!")
        elif user_input == "rock" and answer == "paper":
            print("You lose!")
            com_wins += 1
        elif user_input == "rock" and answer == "scissors":
            print("You win!")
            user_wins += 1
        elif user_input == "paper" and answer == "rock":
            print("You win!")
            user_wins += 1
        elif user_input == "paper" and answer == "scissors":
            print("You lose!")
            com_wins += 1
        elif user_input == "scissors" and answer == "paper":
            print("You win!")
            user_wins += 1
        elif user_input == "scissors" and answer == "rock":
            print("You lose!")
            com_wins += 1
        continue
    
    # Tell user the result
    if user_wins > com_wins:
        result = "you"
    elif com_wins > user_wins:
        result = "the computer"
    else:
        result = "no one"
    
    print(f"Winner: {result}")
