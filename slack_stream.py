import streamlit as st
import requests

# Replace with your actual webhook URL
WEBHOOK_URL = "https://hooks.slack.com/services/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"  # REMOVE THIS AFTER TESTING

st.title("Slack Message Poster")

user_text = st.text_area("Enter your message here:", height=150)

if st.button("Post to Slack"):
    if user_text:
        try:
            payload = {"text": user_text}
            response = requests.post(WEBHOOK_URL, json=payload)

            if response.status_code == 200:
                st.success("Message successfully posted to Slack!")
            else:
                st.error(f"Error posting message. Status code: {response.status_code}. Response: {response.text}")  # Display error details

        except requests.exceptions.RequestException as e:
            st.error(f"An error occurred: {e}")  # Handle network or other request-related errors

    else:
        st.warning("Please enter a message before posting.")
