import streamlit as st

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
✔ Quiz-based learning  

Built for students & educators.
""")

# ---------------- AI FUNCTIONS ----------------
def generate_explanation(topic, level, language):
    return f"""
This is a **{level.lower()} level explanation** of **{topic}** in **{language}**.

EduBridge AI adapts content based on the learner’s level and preferred language,
making education accessible, inclusive, and effective.
"""

def generate_quiz(topic):
    return [
        f"What is the main idea of {topic}?",
        f"Why is {topic} important?",
        f"Give one real-life example of {topic}."
    ]

# ---------------- INPUTS ----------------
topic = st.text_input(
    "🧠 Enter Topic",
    placeholder="e.g. Photosynthesis, Blockchain, Newton's Laws"
)

col1, col2 = st.columns(2)

with col1:
    level = st.selectbox("📚 Student Level", ["Beginner", "Intermediate", "Advanced"])

with col2:
    language = st.selectbox("🌍 Language", ["English", "Hindi", "Spanish", "French"])

# ---------------- STATE ----------------
if "explanation" not in st.session_state:
    st.session_state.explanation = None

# ---------------- BUTTONS ----------------
if st.button("🚀 Generate Explanation", disabled=not topic):
    with st.spinner("EduBridge AI is creating a personalized explanation..."):
        st.session_state.explanation = generate_explanation(topic, level, language)

# ---------------- OUTPUT ----------------
if st.session_state.explanation:
    st.success("Explanation Ready!")

    st.markdown(
        f"""
        <div style='
            padding:20px;
            border-radius:10px;
            border-left:5px solid #4CAF50;
            background-color: rgba(76, 175, 80, 0.1);
        '>
        <h4>📖 Explanation</h4>
        <p>{st.session_state.explanation}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # QUIZ BUTTON
    if st.button("🧪 Generate Quiz"):
        quiz = generate_quiz(topic)

        st.markdown("### 📝 Quick Quiz")
        for i, q in enumerate(quiz, 1):
            st.markdown(f"**Q{i}. {q}**")

# ---------------- FOOTER ----------------
st.markdown(
    "<hr><p style='text-align:center; color:gray;'>Built for Hackathon | EduBridge AI</p>",
    unsafe_allow_html=True
)