# TextStatistics.py
"""
Streamlit App: Text Statistics Analyzer
Author: [Your Name]
"""

import streamlit as st
import re

def get_text_statistics(text: str) -> dict:
    """
    Returns a dictionary with character count, word count, and sentence count.
    """
    text = text.strip()
    char_count = len(text)
    word_count = len(text.split())
    sentence_count = len(re.findall(r'[.!?]', text))

    return {
        "Characters": char_count,
        "Words": word_count,
        "Sentences": sentence_count
    }

# ---------------- Streamlit UI ----------------

st.set_page_config(page_title="📝 Text Statistics Analyzer", layout="centered")
st.title("📝 Text Statistics Analyzer")
st.write("Paste a paragraph below and click 'Analyze' to get counts of **characters, words, and sentences**.")

# Input area
user_input = st.text_area("Enter your paragraph here:", height=200)

# Analyze button
if st.button("Analyze"):
    if not user_input.strip():
        st.warning("⚠️ Please enter some text.")
    else:
        stats = get_text_statistics(user_input)
        st.subheader("📊 Text Summary")
        st.markdown(f"- **Characters**: `{stats['Characters']}`")
        st.markdown(f"- **Words**: `{stats['Words']}`")
        st.markdown(f"- **Sentences**: `{stats['Sentences']}`")

# Optional Console Test Cases
if __name__ == "__main__":
    test_inputs = [
        "Hello world! Welcome to text analysis. Let's get started.",
        "One. Two. Three?",
        "",
        "Just one sentence",
        "Edge case... With lots... Of dots..."
    ]
    print("\n🧪 Test Results:")
    for text in test_inputs:
        print(f"\nInput: {repr(text)}")
        print(get_text_statistics(text))
