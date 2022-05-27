import random
def generate_answer(lower_bound, upper_bound):
    answer = random.randint(lower_bound, upper_bound)
    return answer
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
    while Iscorrect == False:
        user_input = get_input(lower_bound,upper_bound)
        if user_input == answer:
            Iscorrect = True
            return "Well done! You win the game!"
        limit -= 1
        if limit == 0:
            return "The limit is reached! You lose!"
        if (answer - user_input) > (user_input - answer):
            lower_bound = user_input
        else:
            upper_bound = user_input
        print(f"Please try again (Limit lefted): {limit}")
        continue
