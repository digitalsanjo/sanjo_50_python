# GradeAverage.py
import streamlit as st

# Configure the Streamlit app
st.set_page_config(page_title="Grade Average Checker", page_icon="📘", layout="centered")

# App title
st.title("📘 Grade Average Calculator")

# Tabs for homepage and calculator
tab1, tab2 = st.tabs(["🏠 Home", "📊 Grade Checker"])

# Home Tab
with tab1:
    st.header("🏠 Welcome!")
    st.write("""
    This simple app allows you to:
    - Enter 5 test scores
    - Calculate the average
    - Determine if the student has passed or failed
    
    **Pass Criteria:** Average score ≥ 50  
    Use the **Grade Checker** tab to get started.
    """)

# Grade Checker Tab
with tab2:
    st.header("📊 Enter Your Test Scores")
    
    score1 = st.number_input("Test Score 1", min_value=0.0, max_value=100.0, step=1.0)
    score2 = st.number_input("Test Score 2", min_value=0.0, max_value=100.0, step=1.0)
    score3 = st.number_input("Test Score 3", min_value=0.0, max_value=100.0, step=1.0)
    score4 = st.number_input("Test Score 4", min_value=0.0, max_value=100.0, step=1.0)
    score5 = st.number_input("Test Score 5", min_value=0.0, max_value=100.0, step=1.0)

    if st.button("Calculate Average"):
        average = (score1 + score2 + score3 + score4 + score5) / 5
        result = "✅ Pass" if average >= 50 else "❌ Fail"
        
        st.success(f"Average Score: {average:.2f}")
        st.info(f"Result: {result}")
