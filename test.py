import random

def play_blackjack():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    while True:
        choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
        if choice != "y":
            print("You have successfully exited the game.")
            break

        your_cards = [random.choice(cards), random.choice(cards)]
        computer_cards = [random.choice(cards), random.choice(cards)]

        your_score = sum(your_cards)
        computer_score = sum(computer_cards)

        print(f"Your cards: {your_cards}, current score: {your_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if your_score == 21:
            print("You win! You have a Blackjack!")
            continue
        elif your_score > 21:
            print("You lose! You went over 21.")
            continue

        # Player draw phase
        while your_score < 21:
            con = input("Do you want to pick another card? Type 'yes' or 'no': ").lower()
            if con == "yes":
                your_cards.append(random.choice(cards))
                your_score = sum(your_cards)
                print(f"Your cards: {your_cards}, current score: {your_score}")
                if your_score > 21:
                    print("You lose! You went over 21.")
                    break
            elif con == "no":
                break
            else:
                print("Invalid input. Please type 'yes' or 'no'.")

        # Show final hands
        print(f"Your final hand: {your_cards}, final score: {your_score}")
        print(f"Computer's final hand: {computer_cards}, computer's score: {computer_score}")

        # Game result
        if your_score > 21:
            print("You lose! You went over 21.")
        elif computer_score > 21:
            print("You win! Computer went over 21.")
        elif your_score > computer_score:
            print("You win! Your score is higher than the computer.")
        elif your_score < computer_score:
            print("You lose! Your score is lower than the computer.")
        else:
            print("It's a draw!")

        # Restart prompt
        restart = input("Do you want to play again? Type 'yes' or 'no': ").lower()
        if restart != "yes":
            print("You have successfully exited the game.")
            break

# Start the game
play_blackjack()
