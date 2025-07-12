# NameListApp.py

import streamlit as st

st.title("Name Length Checker")

st.write("Enter 5 names below:")

# Input fields for 5 names
name1 = st.text_input("Enter Name 1")
name2 = st.text_input("Enter Name 2")
name3 = st.text_input("Enter Name 3")
name4 = st.text_input("Enter Name 4")
name5 = st.text_input("Enter Name 5")

# Button to process the names
if st.button("Show Name Lengths"):
    names = [name1, name2, name3, name4, name5]
    
    # Filter out empty strings
    valid_names = [name for name in names if name.strip() != ""]

    if len(valid_names) != 5:
        st.warning("Please enter all 5 names.")
    else:
        st.subheader("Name List with Lengths:")
        for name in valid_names:
            st.write(f"Name: {name}, Length: {len(name)}")

        st.success(f"Total names processed: {len(valid_names)}")
