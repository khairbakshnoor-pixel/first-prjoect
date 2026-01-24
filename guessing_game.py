import random

while True:
    level = int(input("Enter level (1, 2, 3): "))

    # -------------------- LEVEL 1 -------------------------
    if level == 1:
        lives = 7
        start = int(input("Enter starting range: "))
        end = int(input("Enter ending range: "))
        num = random.randint(start, end)

        while True:
            print("\nLives left:", lives)
            guess = int(input("Enter your guess: "))

            if guess == num:
                print("You WIN!")

                if lives >= 6:
                    print("You scored 100 points")
                elif lives >= 5:
                    print("You scored 80 points")
                elif lives >= 3:
                    print("You scored 60 points")
                elif lives >= 2:
                    print("You scored 40 points")
                elif lives >= 1:
                    print("You scored 20 points")
                else:
                    print("You scored 0 points")
                break

            elif guess < num:
                print("Too LOW!")
            else:
                print("Too HIGH!")

            lives -= 1
            if lives < 1:
                print("Your lives are over! The number was:", num)
                break

        play = input("Play again? (1 = yes, 0 = no): ")
        if play != "1":
            print("Thanks for playing!")
            break

    # -------------------- LEVEL 2 -------------------------
    elif level == 2:
        lives = 5
        start = int(input("Enter starting range: "))
        end = int(input("Enter ending range: "))
        num = random.randint(start, end * 2)

        while True:
            print("\nLives left:", lives)
            guess = int(input("Enter your guess: "))

            if guess == num:
                print("You WIN!")

                if lives == 5:
                    print("You scored 100 points")
                elif lives == 4:
                    print("You scored 80 points")
                elif lives == 3:
                    print("You scored 60 points")
                elif lives == 2:
                    print("You scored 40 points")
                elif lives == 1:
                    print("You scored 20 points")
                else:
                    print("You scored 0 points")
                break

            elif guess < num:
                print("Too LOW!")
            else:
                print("Too HIGH!")

            lives -= 1
            if lives < 1:
                print("Your lives are over! The number was:", num)
                break

        play = input("Play again? (1 = yes, 0 = no): ")
        if play != "1":
            print("Thanks for playing!")
            break

    # -------------------- LEVEL 3 -------------------------
    elif level == 3:
        lives = 3
        start = int(input("Enter starting range: "))
        end = int(input("Enter ending range: "))
        num = random.randint(start, end * 3)

        while True:
            print("\nLives left:", lives)
            guess = int(input("Enter your guess: "))

            if guess == num:
                print("You WIN!")

                if lives == 3:
                    print("You scored 100 points")
                elif lives == 2:
                    print("You scored 80 points")
                elif lives == 1:
                    print("You scored 60 points")
                else:
                    print("You scored 0 points")
                break

            elif guess < num:
                print("Too LOW!")
            else:
                print("Too HIGH!")

            lives -= 1
            if lives < 1:
                print("Your lives are over! The number was:", num)
                break

        play = input("Play again? (1 = yes, 0 = no): ")
        if play != "1":
            print("Thanks for playing!")
            break

    else:
        print("Invalid level! Choose 1, 2, or 3.")
