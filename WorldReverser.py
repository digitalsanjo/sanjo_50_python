# WordReverser.py
"""
Streamlit App to Reverse Each Word in a Sentence
Author: [Your Name]
"""

import streamlit as st
import re

def reverse_words(sentence: str) -> str:
    """
    Reverses each word in the input sentence while preserving the word order and spacing.
    """
    tokens = re.findall(r'\S+|\s+', sentence)
    reversed_tokens = [token[::-1] if not token.isspace() else token for token in tokens]
    return ''.join(reversed_tokens)

# ------------------- Streamlit UI -------------------

st.set_page_config(page_title="Word Reverser", layout="centered")

st.title("🔄 Word Reverser")
st.write("Reverse each word in a sentence while keeping the original order and spacing.")

# User input
user_input = st.text_area("Enter a sentence:", height=100)

if st.button("Reverse Words"):
    if user_input.strip() == "":
        st.warning("Please enter a sentence to reverse.")
    else:
        result = reverse_words(user_input)
        st.subheader("🔁 Reversed Sentence")
        st.code(result, language='text')

# Optional: Console test cases
if __name__ == "__main__":
    test_sentences = [
        "Hello world",
        "Python is fun!",
        " AI   will change\n the world ",
    ]
    for i, sentence in enumerate(test_sentences, 1):
        print(f"Test {i}: '{sentence}' -> '{reverse_words(sentence)}'")
