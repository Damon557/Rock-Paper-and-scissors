from random import choice
possible_actions = ["rock", "paper", "scissors", "spock"]
computer_action = choice(possible_actions)
user = input ("Do you want to play? Yes or No: ")
while True:
    if user.lower() == "no":
        print("FINE!!! I didn't want to play anyways.")
        break
    if user.lower() == "yes":
            user_action = input("Choose an action (Rock, paper, scissors, or Spock): ")
            if user_action == computer_action:
                print(f"Both players selected {user_action}. It's a tie!")
            elif user_action == "rock":
                if computer_action == "scissors":
                    print("Rock smashes scissors! You win!")
                else:
                    print("Paper covers rock! DEAD.")
            elif user_action == "paper":
                if computer_action == "rock":
                    print("Paper covers rock! You win!")
                else:
                    print("Scissors cuts paper! DEAD.")
            elif user_action == "scissors":
                if computer_action == "paper":
                    print("Scissors cuts paper! You win!")
                else:
                    print("Rock smashes scissors! DEAD.")
            elif user_action == "spock":
                print("Spock destroys all, good job.")
            else: print("Thats not a option stupid.")


    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        print("Get lost.")
        break
