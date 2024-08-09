# Gets users name and initializes loop condition
user_name = input("Hello! What's your name?\n")
loop_cont = "y"

# While loop continues to get user integer input until they want to stop the program
while True:
    # User break condition
    if loop_cont.lower() == "n":
        break
    # Tests if the user inputs anything other than an integer
    try:
        user_num = int(input(f"{user_name}, please enter an integer between 1 and 100:\n"))
        print(f"You entered: {user_num}")

        # Conditionals for integers between 1 and 100
        if user_num > 0 and user_num < 101:

            if user_num % 2 != 0 and user_num < 60:
                print(f"{user_num} is odd and less than 60.")

            elif user_num % 2 == 0 and user_num < 25 and user_num > 1:
                print(f"{user_num} is even and less than 25.")

            elif user_num % 2 == 0 and user_num < 61 and user_num > 25:
                print(f"{user_num} is even and between 26 and 60 inclusive.")

            elif user_num % 2 == 0 and user_num > 60:
                print(f"{user_num} is even and greater than 60.")

            elif user_num % 2 != 0 and user_num > 60:
                print(f"{user_num} is odd and greater than 60.")

            loop_cont = input("Would you like to enter another number?(y/n) \n")
        # Condition for any integer not between 1 and 100
        else:
            print("Error...Please try entering a valid number")
            loop_cont = input("Would you like to enter another number?(y/n) \n")
    # Catches if user input is anything other than an integer and asks if they want to try again
    except ValueError:
        print("Error...Please try entering a valid number")
        loop_cont = input("Would you like to enter another number?(y/n) \n")
