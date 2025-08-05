# TextFileReaderApp.py

import streamlit as st

# --- Streamlit Config ---
st.set_page_config(page_title="📄 Text File Reader", page_icon="📘")

# --- App Title & Instructions ---
st.markdown("""
    <h1 style="color:#4A90E2;">📄 Text File Reader</h1>
    <p style="font-size:17px;">
        Upload a <code>.txt</code> file to count the total number of <b>lines</b> and <b>words</b>.
    </p>
    <hr>
""", unsafe_allow_html=True)

# --- File Upload ---
uploaded_file = st.file_uploader("📤 Upload your .txt file here", type=["txt"])

if uploaded_file:
    try:
        content = uploaded_file.read().decode('utf-8')
        lines = content.strip().split('\n')
        total_lines = len(lines)
        total_words = sum(len(line.split()) for line in lines)

        st.success("✅ File processed successfully!")
        st.markdown(f"**📝 File Name:** `{uploaded_file.name}`")
        st.markdown(f"**📌 Total Lines:** `{total_lines}`")
        st.markdown(f"**📌 Total Words:** `{total_words}`")

        with st.expander("🔍 View File Content"):
            st.text(content)

    except Exception as e:
        st.error(f"❌ Error reading file: {e}")
else:
    st.info("Please upload a .txt file to begin.")
