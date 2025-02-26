import streamlit as st
import requests
import json

# --- Slack Webhook URL (Replace with your actual webhook) ---
webhook_url = "https://hooks.slack.com/services/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"  # Use the one you provided

def send_slack_message(message_text):
    """Sends a message to Slack via the webhook.

    Args:
        message_text: The text of the message to send.

    Returns:
        None
    """
    message = {
        "text": message_text
    }
    headers = {
        'Content-Type': 'application/json',
    }
    response = requests.post(webhook_url, headers=headers, data=json.dumps(message))

    if response.status_code == 200:
        st.success("Message sent to Slack successfully!")  # Streamlit success message
    else:
        st.error(f"Error sending message to Slack: {response.status_code}, {response.text}") # Streamlit error message


# --- Streamlit App ---
st.title("Slack Message Sender")

# Text Input
message_input = st.text_area("Enter your message:", "Hola para todos")  # Default message

# Send Button
if st.button("Send to Slack"):
    if message_input:  # Check if the message is not empty
        send_slack_message(message_input)
    else:
        st.warning("Please enter a message to send.")

# --- Optional:  Add some extra UI elements ---
st.sidebar.header("About")
st.sidebar.markdown("This app sends messages to a Slack channel using a webhook.")
