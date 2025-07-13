# GradeAverageApp.py

import streamlit as st

st.title("Grade Average Calculator")

st.write("Enter 5 test scores (0 to 100):")

# Input fields
score1 = st.number_input("Test Score 1", min_value=0, max_value=100)
score2 = st.number_input("Test Score 2", min_value=0, max_value=100)
score3 = st.number_input("Test Score 3", min_value=0, max_value=100)
score4 = st.number_input("Test Score 4", min_value=0, max_value=100)
score5 = st.number_input("Test Score 5", min_value=0, max_value=100)

if st.button("Calculate Average"):
    scores = [score1, score2, score3, score4, score5]
    average = sum(scores) / len(scores)
    result = "Pass" if average >= 50 else "Fail"

    st.subheader("Summary Report")
    st.write(f"Scores: {scores}")
    st.write(f"Average: {average:.2f}")
    st.write(f"Result: **{result}**")
