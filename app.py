import streamlit as st
import pandas as pd
import datetime

# Set up the page title and icon
st.set_page_config(page_title="Personal Journal", page_icon="📝")

# Title of the app
st.title("Personal Journal")
st.markdown("Keep track of your thoughts and daily activities. ✍️")

# Load existing entries
if 'entries' not in st.session_state:
    st.session_state.entries = pd.DataFrame(columns=["Date", "Mood", "Entry"])

# Input fields for the journal entry
date = st.date_input("Date", datetime.date.today())
mood = st.selectbox("Mood", ["Happy", "Sad", "Productive", "Motivated", "Neutral"])
entry = st.text_area("Journal Entry", "")

# Button to submit entry
if st.button("Add Entry"):
    if entry:
        new_entry = pd.DataFrame([[date, mood, entry]], columns=["Date", "Mood", "Entry"])
        st.session_state.entries = pd.concat([st.session_state.entries, new_entry], ignore_index=True)
        st.success("Entry added!")
    else:
        st.warning("Please write an entry before submitting.")

# Display past entries
st.markdown("---")
st.subheader("Past Entries")
if not st.session_state.entries.empty:
    st.write(st.session_state.entries)
else:
    st.write("No entries found.")

# Provide options to clear entries (for the sake of development/testing)
if st.button("Clear All Entries"):
    st.session_state.entries = pd.DataFrame(columns=["Date", "Mood", "Entry"])
    st.success("All entries cleared!")