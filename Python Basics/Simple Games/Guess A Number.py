import random

# Generate a random answer
def generate_answer(lower_bound, upper_bound):
    answer = random.randint(lower_bound, upper_bound)
    return answer

# Get the number by user's input and check whether the user input is valid
def get_input(lower_bound, upper_bound):
    while True:
        user_input = int(input(f"Please enter a number between {lower_bound} to {upper_bound}"))
        if (user_input >= lower_bound) and (user_input <= upper_bound):
            return user_input
        else:
            print(f"Please enter a number between the correct range : {lower_bound} to {upper_bound}")
            continue

def check_ans(lower_bound, upper_bound):
    Iscorrect = False
    limit = 20
    answer = generate_answer(lower_bound, upper_bound)
    # Check if the user input equals to the generated answer
    while Iscorrect == False:
        user_input = get_input(lower_bound,upper_bound)
        if user_input == answer:
            Iscorrect = True
            return "Well done! You win the game!"
        # If incorrect, minus 1 limit
        limit -= 1
        if limit == 0:
            return "The limit is reached! You lose!"
        # Update the lower bound and upper bound
        if (answer - user_input) > (user_input - answer):
            lower_bound = user_input
        else:
            upper_bound = user_input
        # If the limit becomes 0, the user will lose the game
        print(f"Please try again (Limit lefted): {limit}")
        continue
