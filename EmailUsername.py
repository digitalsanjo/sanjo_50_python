# EmailUsername.py
"""
Streamlit App: Extract Username from Email Address
Author: [Your Name]
"""

import streamlit as st

def extract_username(email: str) -> str:
    """
    Extracts the username part from an email address.
    Returns an error message if the input is invalid.
    """
    email = email.strip()
    if '@' not in email or email.startswith('@') or email.endswith('@'):
        return "❌ Invalid email address"
    
    username = email.split('@')[0]
    return username

# ---------------- Streamlit UI ----------------

st.set_page_config(page_title="📧 Email Username Extractor", layout="centered")
st.title("📧 Email Username Extractor")
st.write("Enter an email address to extract the part **before '@'** (the username).")

# Input field
email_input = st.text_input("Enter email address:")

# Button click
if st.button("Extract"):
    if not email_input.strip():
        st.warning("⚠️ Please enter an email address.")
    else:
        result = extract_username(email_input)
        st.subheader("🧾 Result")
        st.code(result, language="text")

# Optional Console Test Cases
if __name__ == "__main__":
    test_emails = [
        "user@example.com",
        "hello.world@domain.org",
        "   test@demo.net   ",
        "noatsymbolhere",
        "@missingusername.com",
        "missingdomain@"
    ]
    print("\n📧 Email Username Test Results:")
    for email in test_emails:
        print(f"{email} -> {extract_username(email)}")
