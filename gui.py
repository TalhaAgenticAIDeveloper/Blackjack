# import tkinter as tk
# import random

# class BlackjackGame:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Blackjack Game")
#         self.cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#         self.setup_ui()
#         self.reset_game()

#     def setup_ui(self):
#         self.result_label = tk.Label(self.root, text="", font=("Helvetica", 14))
#         self.result_label.pack(pady=10)

#         self.your_cards_label = tk.Label(self.root, text="", font=("Helvetica", 12))
#         self.your_cards_label.pack()

#         self.computer_cards_label = tk.Label(self.root, text="", font=("Helvetica", 12))
#         self.computer_cards_label.pack()

#         self.hit_button = tk.Button(self.root, text="Hit", width=10, command=self.hit)
#         self.hit_button.pack(pady=5)

#         self.stand_button = tk.Button(self.root, text="Stand", width=10, command=self.stand)
#         self.stand_button.pack(pady=5)

#         self.restart_button = tk.Button(self.root, text="Restart", width=10, command=self.reset_game)
#         self.restart_button.pack(pady=10)

#     def reset_game(self):
#         self.your_cards = [random.choice(self.cards), random.choice(self.cards)]
#         self.computer_cards = [random.choice(self.cards), random.choice(self.cards)]
#         self.update_scores()
#         self.result_label.config(text="")
#         self.hit_button.config(state=tk.NORMAL)
#         self.stand_button.config(state=tk.NORMAL)
#         self.update_ui()

#     def update_scores(self):
#         self.your_score = sum(self.your_cards)
#         self.computer_score = sum(self.computer_cards)

#     def update_ui(self):
#         self.update_scores()
#         self.your_cards_label.config(text=f"Your cards: {self.your_cards} (Score: {self.your_score})")
#         self.computer_cards_label.config(text=f"Computer's first card: {self.computer_cards[0]}")

#     def hit(self):
#         self.your_cards.append(random.choice(self.cards))
#         self.update_ui()

#         if self.your_score > 21:
#             self.result_label.config(text="You lose! You went over 21.")
#             self.end_game()

#     def stand(self):
#         self.update_scores()

#         # Reveal computer's hand
#         while self.computer_score < 17:
#             self.computer_cards.append(random.choice(self.cards))
#             self.update_scores()

#         self.computer_cards_label.config(text=f"Computer's cards: {self.computer_cards} (Score: {self.computer_score})")

#         if self.computer_score > 21:
#             result = "You win! Computer went over 21."
#         elif self.your_score > self.computer_score:
#             result = "You win! Your score is higher than the computer."
#         elif self.your_score < self.computer_score:
#             result = "You lose! Your score is lower than the computer."
#         else:
#             result = "It's a draw!"

#         self.result_label.config(text=result)
#         self.end_game()

#     def end_game(self):
#         self.hit_button.config(state=tk.DISABLED)
#         self.stand_button.config(state=tk.DISABLED)

# # Run the game
# root = tk.Tk()
# game = BlackjackGame(root)
# root.mainloop()







import streamlit as st
import random

# Initialize session state
if "your_cards" not in st.session_state:
    st.session_state.your_cards = []
    st.session_state.computer_cards = []
    st.session_state.game_over = False
    st.session_state.result = ""

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def start_game():
    st.session_state.your_cards = [random.choice(cards), random.choice(cards)]
    st.session_state.computer_cards = [random.choice(cards), random.choice(cards)]
    st.session_state.game_over = False
    st.session_state.result = ""

def calculate_score(card_list):
    score = sum(card_list)
    # Handle Aces (11 can be 1 if over 21)
    while score > 21 and 11 in card_list:
        card_list[card_list.index(11)] = 1
        score = sum(card_list)
    return score

def end_game():
    your_score = calculate_score(st.session_state.your_cards)
    computer_score = calculate_score(st.session_state.computer_cards)
    
    # Computer draws until 17 or more
    while computer_score < 17:
        st.session_state.computer_cards.append(random.choice(cards))
        computer_score = calculate_score(st.session_state.computer_cards)

    if your_score > 21:
        st.session_state.result = "You lose! You went over 21."
    elif computer_score > 21:
        st.session_state.result = "You win! Computer went over 21."
    elif your_score > computer_score:
        st.session_state.result = "You win! Your score is higher."
    elif your_score < computer_score:
        st.session_state.result = "You lose! Computer score is higher."
    else:
        st.session_state.result = "It's a draw!"
    
    st.session_state.game_over = True

# Streamlit UI
st.title("🃏 Blackjack Game")

if st.button("Start New Game"):
    start_game()

if st.session_state.your_cards:
    your_score = calculate_score(st.session_state.your_cards)
    st.write(f"**Your cards:** {st.session_state.your_cards} | **Score:** {your_score}")
    st.write(f"**Computer's first card:** {st.session_state.computer_cards[0]}")

    if not st.session_state.game_over:
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Hit"):
                st.session_state.your_cards.append(random.choice(cards))
                if calculate_score(st.session_state.your_cards) > 21:
                    end_game()

        with col2:
            if st.button("Stand"):
                end_game()

    if st.session_state.game_over:
        st.write("---")
        st.write(f"**Computer's cards:** {st.session_state.computer_cards} | **Score:** {calculate_score(st.session_state.computer_cards)}")
        st.subheader(st.session_state.result)
