import streamlit as st
import os

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="EduBridge AI",
    page_icon="🎓",
    layout="centered"
)

# ---------------- HEADER ----------------
st.markdown(
    """
    <h1 style='text-align:center;'>🎓 EduBridge AI</h1>
    <h4 style='text-align:center; color: gray;'>
    Personalized Learning • Any Topic • Any Language
    </h4>
    <hr>
    """,
    unsafe_allow_html=True
)

# ---------------- SIDEBAR ----------------
st.sidebar.title("🎓 EduBridge AI")
st.sidebar.markdown("""
**Bridging learning gaps with AI**

✔ Personalized explanations  
✔ Multilingual support  
✔ Real-time responses  

Built for students & educators.
""")

# ---------------- AI FUNCTION ----------------
def generate_explanation(topic, level, language):
    # OFFLINE / DEMO MODE (NO API NEEDED)
    return f"""
This is a **{level.lower()} level explanation** of **{topic}** in **{language}**.

EduBridge AI adapts explanations based on the learner’s understanding level
and preferred language, making education more accessible and effective.

(For hackathon demo, this represents AI-generated personalized learning.)
"""

# ---------------- INPUTS ----------------
topic = st.text_input(
    "🧠 Enter Topic",
    placeholder="e.g. Photosynthesis, Blockchain, Newton's Laws"
)

col1, col2 = st.columns(2)

with col1:
    level = st.selectbox(
        "📚 Student Level",
        ["Beginner", "Intermediate", "Advanced"]
    )

with col2:
    language = st.selectbox(
        "🌍 Language",
        ["English", "Hindi", "Spanish", "French"]
    )

# ---------------- BUTTON & OUTPUT ----------------
if st.button("🚀 Generate Explanation", disabled=not topic):
    with st.spinner("EduBridge AI is creating a personalized explanation..."):
        explanation = generate_explanation(topic, level, language)

    st.success("Explanation Ready!")

    st.markdown(
        f"""
        <div style='
            background-color:#f8f9fa;
            padding:20px;
            border-radius:10px;
            border-left:5px solid #4CAF50;
        '>
        <h4>📖 Explanation</h4>
        <p>{explanation}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

# ---------------- FOOTER ----------------
st.markdown(
    "<hr><p style='text-align:center; color:gray;'>Built for Hackathon | EduBridge AI</p>",
    unsafe_allow_html=True
)