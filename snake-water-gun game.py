import random

print("s=snake, w=water, g=gun")
options = ["s","w","g"]

def comp_choice():
    return random.choice(options)
    #generates a rendom choice from the options and return it

def user_input():
    while True:
        user = input("enter your choice: ").lower()
        if user in options:
            return user
        print("The input is invalid, enter the valid option.")
        #takes the user input and validate it.

def display_result(user_score,comp_score):
    #print the final scores.
    print(f"\nFinal scores:\nYour Score: {user_score}.\nComputer Score: {comp_score}.\n")
    # make the display_result of who wins.  
    if user_score < comp_score:
        return("Computer won the game")

    elif user_score > comp_score:
        return("You win the game.")

    else:
        return("Score is equal. Game Drawn!")
    
def main():
    #main function includes the conditionals, tracks and return the score of players
    user_score = comp_score =0
    total_rounds = int(input("how many rounds you want to play: "))

    for i in range(1, total_rounds+1):
        user = user_input()
        comp = comp_choice()

        print(f"computer chose: {comp}")
        if user == comp:
            print("draw\n")

        elif (user == "s" and comp == "w") or (user == "w" and comp == "g") or (user == "g" and comp == "s"):
            print("you win\n")
            user_score += 1
        else:
            print("computer won!\n")
            comp_score += 1
        

    return user_score, comp_score


# Captures the returned values from the main function
user_score, comp_score = main()

#prints the name of the winner or drawn
print(display_result(user_score, comp_score))


