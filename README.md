

---


```markdown
# 🤖 ChitterBot – A Chatbot for Job Seekers

**ChitterBot** is a lightweight Streamlit-based chatbot built to interact with users who are looking for jobs. It captures and logs user data like name, age, qualification, and email, then offers startup ideas, job app suggestions, and tailored responses.

---

## 🚀 Features

- Interactive chat interface using **Streamlit**
- Predefined conversational flows
- Captures:
  - Name
  - Age
  - Qualification (UG, PG, None)
  - Email
- Recommends startup ideas and job search platforms
- Logs chat history and saves user data to a CSV file

---

## 📂 Project Structure

```

chitterbot/
├── chatbot.py            # Main Streamlit app
├── user\_data.csv         # Saved user details (auto-generated)
├── chat\_log.txt          # Conversation log (auto-generated)
├── README.md             # Project documentation

````

---

## 🛠️ Built With

- 🐍 Python
- 🧠 Streamlit
- 🧾 Pandas
- 🔍 Regex
- 💾 CSV for data logging

---

## 🎯 How to Run

1. Clone the repository:

```bash
git clone https://github.com/Shadinbm/chitterbot.git
cd chitterbot
````

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the Streamlit app:

```bash
streamlit run chatbot.py
```

---

## 📌 Example Use Case

* User types: `my name is Alex`
* Bot responds: `Nice to meet you, Alex! May I know your job?`
* Continues the conversation based on age, qualification, and responses

---

## 📧 Contact

* **Author**: Muhammed Shadin Bm
* 📬 Email: [bmshadin43@gmail.com](mailto:bmshadin43@gmail.com)
* 🔗 LinkedIn: [muhammed-shadin-bm](https://www.linkedin.com/in/muhammed-shadin-bm-23871432b)

---

> ⚠️ *ChitterBot is currently under development. Contributions, feature ideas, and feedback are welcome!*

```


