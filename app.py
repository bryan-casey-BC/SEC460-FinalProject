# Simple guessing game that generates a random number that the user must guess.
# Game logic will run in a function.
# There will be three difficulties that the user may select.

# Import random functions for use in the game
import random
import streamlit as st  # type: ignore

# Global variables stored in session state
if "game_active" not in st.session_state:
    st.session_state.game_active = False
if "random_number" not in st.session_state:
    st.session_state.random_number = None
if "num_tries" not in st.session_state:
    st.session_state.num_tries = 0
if "tries" not in st.session_state:
    st.session_state.tries = 0
if "player_wins" not in st.session_state:
    st.session_state.player_wins = 0
if "player_losses" not in st.session_state:
    st.session_state.player_losses = 0

# Function to start the game
def start_game(difficulty):
    if difficulty == "Easy":
        st.session_state.random_number = random.randint(1, 10)
        st.session_state.num_tries = 5
    elif difficulty == "Moderate":
        st.session_state.random_number = random.randint(1, 100)
        st.session_state.num_tries = 8
    elif difficulty == "Hard":
        st.session_state.random_number = random.randint(1, 1000)
        st.session_state.num_tries = 10

    st.session_state.tries = 0
    st.session_state.game_active = True  # Start the game

# UI Setup
st.title("Number Guessing Game")
st.write("I am thinking of a random number. Can you guess it?")

# Difficulty Selection
st.write("Select a difficulty to begin:")
if st.button("Easy"):
    start_game("Easy")
if st.button("Moderate"):
    start_game("Moderate")
if st.button("Hard"):
    start_game("Hard")

# Game Logic
if st.session_state.game_active:
    guess = st.number_input("Enter your guess:", min_value=1, step=1)
    if st.button("Submit Guess"):
        st.session_state.tries += 1
        if guess == st.session_state.random_number:
            st.success(f"Congratulations! You guessed the number {st.session_state.random_number} correctly!")
            st.session_state.player_wins += 1
            st.session_state.game_active = False  # End game
        else:
            st.warning(f"Incorrect guess. {st.session_state.num_tries - st.session_state.tries} attempts left.")
            if st.session_state.tries >= st.session_state.num_tries:
                st.error(f"Game Over! The correct number was {st.session_state.random_number}")
                st.session_state.player_losses += 1
                st.session_state.game_active = False  # End game

# Show Score
st.write(f"Total Wins: {st.session_state.player_wins}, Total Losses: {st.session_state.player_losses}")
