# InitialExtractor.py
import streamlit as st

def extract_initials(full_name: str) -> str:
    # Strip leading/trailing spaces and split the name
    words = full_name.strip().split()
    # Extract first letter from each word and convert to uppercase
    initials = ''.join(word[0].upper() for word in words if word)
    return initials

# Streamlit App UI
st.set_page_config(page_title="Initial Extractor", page_icon="🔤")

st.title("🔤 Initial Extractor")
st.write("Enter a full name to extract and display the initials in uppercase.")

# User input
user_input = st.text_input("Full Name", placeholder="e.g., John Doe")

if user_input:
    initials = extract_initials(user_input)
    st.success(f"✅ Initials: **{initials}**")

# Footer
st.markdown("---")
st.caption("Built with ❤️ using Streamlit")
