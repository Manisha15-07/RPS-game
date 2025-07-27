import streamlit as st
import random

st.set_page_config(page_title="Rock Paper Scissors", page_icon="✊✋✌️")

st.title("✊✋✌️ Rock Paper Scissors")
st.write("Choose your move and play against the computer!")

choices = ["Rock", "Paper", "Scissors"]
emojis = {"Rock": "✊", "Paper": "✋", "Scissors": "✌️"}

# Initialize game state
if "result" not in st.session_state:
    st.session_state.result = ""
if "user_choice" not in st.session_state:
    st.session_state.user_choice = ""
if "computer_choice" not in st.session_state:
    st.session_state.computer_choice = ""

# User selection
user_choice = st.radio("Your move:", choices, horizontal=True)

if st.button("Play"):
    computer_choice = random.choice(choices)

    # Save choices to session state
    st.session_state.user_choice = user_choice
    st.session_state.computer_choice = computer_choice

    # Determine winner
    if user_choice == computer_choice:
        st.session_state.result = "It's a Tie!"
        
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        st.session_state.result = "🎉 You Win!"
        st.balloons()
    else:
        st.session_state.result = "💻 Computer Wins!"
        st.balloons()

# Display results
if st.session_state.user_choice:
    st.write(f"**You chose:** {emojis[st.session_state.user_choice]} {st.session_state.user_choice}")
    st.write(f"**Computer chose:** {emojis[st.session_state.computer_choice]} {st.session_state.computer_choice}")
    st.markdown(f"### 🏆 {st.session_state.result}")

# Reset button
if st.button("Reset Game"):
    st.session_state.result = ""
    st.session_state.user_choice = ""
    st.session_state.computer_choice = ""
