# SimpleCipher.py
"""
Streamlit App: Simple Caesar Cipher (+1 Shift)
Author: [Your Name]
"""

import streamlit as st

def simple_cipher(text: str) -> str:
    """
    Shifts each alphabet character in the text by +1 (Caesar Cipher).
    Wraps around z→a and Z→A. Non-alphabet characters are unchanged.
    """
    result = []

    for char in text:
        if char.isalpha():
            if char.islower():
                shifted = chr((ord(char) - ord('a') + 1) % 26 + ord('a'))
            else:
                shifted = chr((ord(char) - ord('A') + 1) % 26 + ord('A'))
            result.append(shifted)
        else:
            result.append(char)

    return ''.join(result)

# ---------------- Streamlit UI ----------------

st.set_page_config(page_title="🔐 Simple Cipher", layout="centered")
st.title("🔐 Simple Caesar Cipher (+1 Shift)")
st.write("Shift each letter in your sentence by +1. Non-letters stay the same.")

# Input Area
user_input = st.text_area("Enter your text to encrypt:", height=120)

# Encrypt Button
if st.button("Encrypt"):
    if user_input.strip() == "":
        st.warning("⚠️ Please enter some text.")
    else:
        ciphered_text = simple_cipher(user_input)
        st.subheader("🔏 Encrypted Output")
        st.code(ciphered_text, language="text")

# Optional Console Tests
if __name__ == "__main__":
    test_cases = [
        "abc",
        "Zebra-493",
        "Hello World!",
        "zZ",
        "Test @ 2025"
    ]
    print("\n🔐 Simple Cipher Test Results:")
    for text in test_cases:
        print(f"{text} -> {simple_cipher(text)}")
