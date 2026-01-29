import streamlit as st
import datetime
import requests
import sys 

BASE_URL = "http://localhost:8000" # Frontend URL

st.set_page_config(
    page_title = " Travel Planner Agentic Application",
    page_icon = "✈️",
    layout = "centered",
    initial_sidebar_state = "expanded",
)

st.title("✈️ Travel Planner Agentic Application")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
st.header("How can I help you in planning a trip? Let me know where do you want to visit!")

# Chat input box at the bottom
with st.form(key = "query_form", clear_on_submit=True):

    user_input = st.text_input("User Input", placeholder="E.g., Plan a trip to Paris for 5 days with a budget of $2000")
    submit_button = st.form_submit_button("Send")

if submit_button and user_input.strip():
    try:
        ## Show user message in chat
        # show thinking spinner while backend processes the request
        with st.spinner("Planning your trip..."):
            payload = {"question": user_input}
            response = requests.post(f"{BASE_URL}/query", json=payload)

        if response.status_code == 200:
            answer = response.json().get("answer", "Sorry, I could not get a response.")
            markdown_answer = f'''# AI Travel Plan'''

            # **Generates:** {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
            # **Created by:** Travel Planner Agentic Application
            ---
            {answer}
            ---
            '''
            *This travel plan was generted by AI. Please verify all information, especially prices, operation cost.
            '''
            st.markdown(markdown_content)
        else:
           st.error("Bot failed to respond:" + response.text)

    except Exception as e:
        raise f"The responce failed due to {e}"