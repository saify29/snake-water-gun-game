import random as rd

options=["s","w","g"]
print("snake:s ,water:w, gun:g")

user_score=comp_score =0
round=1

t_r=int(input("how many rounds you want to play: "))

while round<=t_r:
    comp=rd.choice(options)
    user = input("enter your choice:").lower()
    if user not in options:
        print("please pick correct option.")
        continue
    print(f"computer chose:{comp}")
    if user==comp:
        print("draw")

    elif (user=="s" and comp=="w") or (user=="w" and comp=="g") or (user=="g" and comp=="s"):
        print("you win\n")
        user_score+=1
    else:
        print("computer won!\n")
        comp_score+=1
    round+=1
    
if user_score < comp_score:
    print("Computer won the game")

elif user_score > comp_score:
    print("you win the game.")

else:
    print("score is equal")


print(f"\nFinal scores:\nYour Score: {user_score}.\nComputer Score: {comp_score}.")




#this is just start to understand  the git and github, a test feature1(branch)
