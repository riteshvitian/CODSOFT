import random
while True:
    print("rock")
    print("paper")
    print("scissor")

    values = ["rock", "paper", "scissor"]
    user_selection = input("Enter a choice: ").lower()
    computer_selection = random.choice(values)

    if user_selection not in values:
        print("Invalid choice! Please enter rock, paper, or scissor.")
    else:
        print("Computer selected:", computer_selection)

        if user_selection == computer_selection:
            print("Result: Tie")
        elif (user_selection == "rock" and computer_selection == "scissor"):
            print("User Wins")
        elif (user_selection == "scissor" and computer_selection == "paper"):
            print("User Wins")
        elif (user_selection == "paper" and computer_selection == "rock"):
            print("User Wins")
        else:
            print("User Lost")
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("\nThanks for playing!")
            break

