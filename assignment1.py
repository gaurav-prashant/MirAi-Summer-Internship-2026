#TASK 1:- THE UI SHELL

import streamlit as st

st.title("The Void")

st.write("Enter your name and message, then click the Transmit button.")

#TASK 2:-  Multi-Data Collection

user_name = st.text_input("Enter your Name")

user_message = st.text_input("Enter your Message")

#TASK 3:- The Action Gate

if st.button("Transmit"):

    #TASK 4:- Conditional Routing

    if user_name == "":
        st.error("Please provide your name.")

    elif user_message == "":
        st.warning("Please type a message to transmit.")

    else:

        #Task 5:- The Formated Output

        st.success(f"Transmission successful! Greetings, {user_name}. We received your message: {user_message}")

        #Advanced Challenge Token Cost Estimator
        char_count = len(user_message)
        token_count = char_count // 4
        st.info(f"System Check: Your message will consume approximately {token_count} tokens from our context window.")
