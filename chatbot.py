import streamlit as st
import pandas as pd
import re
import os

st.title("Chitter-for jobless")
st.write("This is a bot for those who are seeking jobs, currently under development.")

# Preset Q&A
predefined_pairs = [
    {"prompt": "hi", "response": "Hello! How can I assist you today?"},
    {"prompt": "how are you", "response": "I'm just a bot, but I'm doing great!"},
    {"prompt": "what is your name", "response": "I'm Chitter Bot "},
    {"prompt": "bye", "response": "Goodbye! Have a great day!"},
    {"prompt": "job", "response": "Good to Know, I have some startup ideas. If you'd like to know, type 'buis'"},
    {"prompt": "buis", "response": "Before we dive into the topic, may I know your age? Type 'startupp' to know ideas"},
    {"prompt": "startupp", "response": "1) FarmFresh AI – An AI-powered marketplace connecting local farmers with urban consumers and restaurants. Want more? Type 'more'"},
    {"prompt": "thanks", "response": "You're welcome! Do you want to know about job-getting apps? If yes, type 'app'"},
    {"prompt": "app", "response": "There are many apps! Here are some: LinkedIn, Naukri, Indeed. May I know your qualifications (UG, PG, Nothing(ignore if provided))?"},
    {"prompt": "more", "response": "2) SkillBridge – A platform matching students and freshers with real-world micro-projects. Want job apps? Type 'app'"},
    {"prompt": "ug", "response": "Oh, you're a graduate. Try upskilling your degree — Google it! If you provide your email, I can send job links."},
    {"prompt": "pg", "response": "So you're a master's holder. If you'd like job updates, please provide your email."},
    {"prompt": "nothing", "response": "I can still share various job opportunities. Please give me your email. Take care!"}
]

# Initialize chat
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        {"prompt": None, "response": "👋 Hi! Ask me anything! May I know your name (please respond with 'my name is')?"}
    ]

# Chat input
if prompt := st.chat_input("Say something"):

    user_input = str(prompt).lower().strip()
    matched = False

    # 1. Capture Name
    if "my name is" in user_input:
        name = prompt.split("my name is")[-1].strip().split()[0]
        st.session_state.user_name = name
        response = f"Nice to meet you, {name}! May i know your job?"
        matched = True

    # 2. Capture Age
    elif not matched and user_input.isdigit() and 0 < int(user_input) < 120:
        st.session_state.user_age = int(user_input)
        response = "Great! What's your qualification? (UG, PG, Nothing (ignore if provided))"
        matched = True

    # 3. Capture Qualification
    elif not matched and user_input in ["ug", "pg", "nothing"]:
        st.session_state.user_qualification = user_input.lower()
        for pair in predefined_pairs:
            if pair["prompt"] in user_input:
                response = pair["response"]
                if "user_name" in st.session_state:
                    response = response.replace("{name}", st.session_state.user_name)
                matched = True
                break
        # response = "Thanks! Could you please provide your email?"
        matched = True

    # 4. Capture Email and Save to CSV
    elif not matched:
        email_match = re.search(r'[\w\.-]+@[\w\.-]+', user_input)
        if email_match:
            st.session_state.user_email = email_match.group(0)
            response = " All set! Your details have been saved. We'll contact you with job updates soon."
            matched = True

            # Save to CSV using pandas
            if all(k in st.session_state for k in ["user_name", "user_age", "user_qualification", "user_email"]):
                user_data = pd.DataFrame([{
                    "Name": st.session_state.user_name,
                    "Age": st.session_state.user_age,
                    "Qualification": st.session_state.user_qualification,
                    "Email": st.session_state.user_email
                }])

                file_path = "user_data.csv"
                if os.path.exists(file_path):
                    existing = pd.read_csv(file_path)
                    updated = pd.concat([existing, user_data], ignore_index=True)
                    updated.to_csv(file_path, index=False)
                else:
                    user_data.to_csv(file_path, index=False)

    # 5. Predefined prompt matching
    if not matched:
        for pair in predefined_pairs:
            if pair["prompt"] in user_input:
                response = pair["response"]
                if "user_name" in st.session_state:
                    response = response.replace("{name}", st.session_state.user_name)
                matched = True
                break

    # 6. Fallback response
    if not matched:
        response = "Sorry, I didn't understand that. Try asking something else. I'm still learning."

    # Save to chat history
    st.session_state.chat_history.append({"prompt": prompt, "response": response})

    # Also save chat log (safe encoding)
    with open("chat_log.txt", "a", encoding="utf-8") as f:
        f.write(f"User: {prompt}\n")
        f.write(f"Bot: {response}\n\n")

# Display chat history
for pair in st.session_state.chat_history:
    if pair["prompt"]:
        with st.chat_message("user"):
            st.write(pair["prompt"])
    with st.chat_message("assistant"):
        st.write(pair["response"])
