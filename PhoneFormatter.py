# PhoneFormatter.py
"""
Streamlit App: Phone Number Formatter (10-digit -> (XXX) XXX-XXXX)
Author: [Your Name]
"""

import streamlit as st
import re

def format_phone_number(raw: str) -> str:
    """
    Cleans input and formats a 10-digit number as (XXX) XXX-XXXX.
    Returns an error message if input is invalid.
    """
    digits = re.sub(r'\D', '', raw)  # Remove non-digit characters

    if len(digits) != 10:
        return "❌ Invalid input: must contain exactly 10 digits"

    return f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"


# ---------------- Streamlit UI ----------------

st.set_page_config(page_title="📞 Phone Number Formatter", layout="centered")
st.title("📞 Phone Number Formatter")
st.write("Format a 10-digit number into the style **(XXX) XXX-XXXX**. Non-digit characters will be ignored.")

# Input
phone_input = st.text_input("Enter phone number:")

# Format button
if st.button("Format"):
    if not phone_input.strip():
        st.warning("⚠️ Please enter a phone number.")
    else:
        result = format_phone_number(phone_input)
        st.subheader("📱 Formatted Number")
        st.code(result, language="text")

# Optional Console Test Cases
if __name__ == "__main__":
    test_numbers = [
        "1234567890",
        " 987 654 3210 ",
        "111-222-3333",
        "12345",
        "abcd1234567"
    ]
    print("\n📞 Phone Number Formatter Test Results:")
    for number in test_numbers:
        print(f"{number} -> {format_phone_number(number)}")
