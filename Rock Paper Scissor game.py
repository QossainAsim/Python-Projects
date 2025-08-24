import random

print("--------- Welcome to Rock Paper Scissor Game ----------")
def choice_check(choice):
    if choice == 1:
        return 'Rock'
    elif choice == 2:
        return 'Paper' 
    else:
        return 'Scissor'
         
while True:
    print("Take your choice: \n 1: Rock \n 2: Paper \n 3: Scissor \n")
    choice = int(input("Enter your choice (1-3): "))
    while choice > 3 or choice < 1:
        choice = int(input("Enter the valid input please: "))

    choice_name = choice_check(choice)
    print(f"User choice is {choice_name}")
    print("Now it's computer's turn!")

    comp_choice = random.randint(1,3)
    comp_choice_name = choice_check(comp_choice)
    print(f"Computer choice is {comp_choice_name}")
    print(f"{choice_name} vs {comp_choice_name}")

    if choice == comp_choice:
        print("<== It's a tie! ==>")
    elif (choice == 1 and comp_choice == 3) or \
    (choice == 2 and comp_choice == 1) or (choice == 3 and comp_choice == 2):
        print("<== User wins! ==>")
    else:
        print("<== Computer wins! ==>")

    ans = input("Do you wnat to paly again? (Y/N)").lower()
    if ans == 'n':
        break

print("Thanks for Playing")
    









       
    
