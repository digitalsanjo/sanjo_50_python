# NumberCheckerApp.py

import streamlit as st

# --- Helper Functions ---
def is_positive(number):
    return number > 0

def is_even(number):
    return number % 2 == 0

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

# --- Streamlit Config ---
st.set_page_config(page_title="Number Checker", page_icon="🔍")

# --- App Header ---
st.markdown("""
    <h1 style="color:#4A90E2;">🔢 Number Checker</h1>
    <p style="font-size:18px;">Check if your number is <b style="color:green;">Positive</b>, <b style="color:#f39c12;">Even</b>, or <b style="color:#e74c3c;">Prime</b> in a fun and interactive way.</p>
    <hr>
""", unsafe_allow_html=True)

# --- Input Section ---
number = st.number_input("✨ Enter a number", step=1, format="%d")

# --- Result Section ---
if st.button("🔍 Check Number"):
    st.markdown("### ✅ Results")
    st.markdown(f"**🧮 Number Entered:** `{number}`")

    # Evaluate conditions
    positive = is_positive(number)
    even = is_even(number)
    prime = is_prime(number)

    # Styled responses
    st.success("🔹 Positive: Yes ✅" if positive else "🔹 Positive: No ❌")
    st.info("🔹 Even: Yes ✅" if even else "🔹 Even: No ❌")
    st.warning("🔹 Prime: Yes ✅" if prime else "🔹 Prime: No ❌")

    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("<p style='color:gray;font-size:14px;'>Built with ❤️ using Streamlit</p>", unsafe_allow_html=True)
