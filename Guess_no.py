import random
randNum = random.randint(1,100)
print(randNum)
print("\n")

while True:
    User_choice=(input("Guess a Number or Quit(Q): "))
    if (User_choice=="Q"):
        break
    User_choice=int(User_choice)
    if User_choice==randNum:
        print(" Your Guess is correct")
        print(f"And your gussed no is {randNum}")
        break

    elif(User_choice<randNum):
        print("Your No is Smaller... Try bigger")
    elif (User_choice > randNum):
        print("Your No is Bigger... Try Smaller")
    else:
        print("Try a No from 1 to 100")
print("\n")
print("The No is: ",randNum)



