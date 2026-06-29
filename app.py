import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="EduBridge AI", layout="centered")
st.title("📘 EduBridge AI")
st.subheader("Personalized Learning Without Barriers")

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

topic = st.text_input("Enter Learning Topic")
language = st.selectbox("Select Language", ["English", "Hindi", "Spanish", "French"])
level = st.selectbox("Select Level", ["Beginner", "Intermediate", "Advanced"])

def generate_explanation(topic, level, language):
    return f"""
📘 Topic: {topic}
👤 Level: {level}
🌍 Language: {language}

This is a personalized explanation generated for the student.
The content is adapted to their learning level and language.
This demonstrates how AI removes language barriers
and personalizes education in real time.
"""

def generate_quiz(topic, level, language):
    return f"""
1. What is {topic}?
Answer: A basic concept explanation.

2. Why is {topic} important?
Answer: It helps understand real-world problems.

3. Give one example of {topic}.
Answer: Example based on daily life.
"""
    prompt = f"""
    Create 3 quiz questions on {topic}
    Difficulty: {level}
    Language: {language}
    Include answers.
    """
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role":"user","content":prompt}]
    )
    return response.choices[0].message.content

if st.button("🎓 Generate Learning"):
    explanation = generate_explanation(topic, level, language)
    st.success("Explanation Generated!")
    st.write(explanation)

if st.button("📝 Generate Quiz"):
    quiz = generate_quiz(topic, level, language)
    st.info("Quiz Ready!")
    st.write(quiz)

st.markdown("---")
st.subheader("👩‍🏫 Educator Dashboard (Demo)")
st.table({
    "Student": ["Demo User"],
    "Topic": [topic if topic else "—"],
    "Level": [level],
    "Status": ["Learning Completed"]
})