answer = input("player 1 Please Insert Number Between (1 - 100): ")
answer = int(answer)

bool1 = False
Count = 0

while Count < 10 and bool1 == False:
    guess = int(input("Player 2 Please Guess a Number Between (1 - 100): "))
    if guess == answer:
        print("Player 2 Won!")
        bool1 = True
    elif guess > answer:
        print("Your Guess Is Greater Than The Number!")
        Count += 1
    else:
        print("Your Guess Is Smaller Than The Number!")
        Count += 1

if bool1 == False:
    print("Player 2, You Used 10 Guesses And Lost!")

