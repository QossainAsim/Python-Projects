import random

print("Welcome to Number Guessing!")
startingNo = int(input("Enter the starting number: "))
endingNo = int(input("Enter the ending number: "))

print(f"You have to choose a number between {startingNo} and {endingNo} and you have 5 chances.")
choose = random.randrange(startingNo,endingNo)
count = 0
chances = 5
while(chances > count):
    count = count + 1
    number  = int(input("Enter the number: "))

    if(number == choose):
        print(f"Congulurations you guessed the corresct number {choose} in {count} chances")  
    elif(number > choose):
        print("The number you enter is too big.")    
    elif(number < choose):
        print("The number you enter is too small.")  
else:
    print(f"You lost the number was {choose} and you have availed your chances {chances}.") 