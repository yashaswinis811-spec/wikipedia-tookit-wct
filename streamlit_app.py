
import streamlit as st
import requests
import random

st.set_page_config(page_title="WikiQuiz", page_icon="🧠")
st.title("🧠 WikiQuiz - Wikipedia Quiz")
st.write("Test your knowledge from Wikipedia!")

# Quiz questions from Wikipedia topics
questions = [
    {
        "q": "Which is the largest Wikipedia language edition by number of articles?",
        "options": ["German", "English", "French", "Spanish"],
        "answer": "English"
    },
    {
        "q": "Wikipedia was launched in which year?",
        "options": ["1999", "2001", "2003", "2005"],
        "answer": "2001"
    },
    {
        "q": "What does 'Wiki' mean in Hawaiian?",
        "options": ["Knowledge", "Quick", "Free", "Open"],
        "answer": "Quick"
    },
    {
        "q": "Who co-founded Wikipedia with Jimmy Wales?",
        "options": ["Larry Sanger", "Tim Berners-Lee", "Sergey Brin", "Mark Zuckerberg"],
        "answer": "Larry Sanger"
    },
    {
        "q": "Which tool uses Wikipedia data to show article connections?",
        "options": ["Wiki Structure Visualizer", "Google Maps", "Excel", "Photoshop"],
        "answer": "Wiki Structure Visualizer"
    }
]

if 'score' not in st.session_state:
    st.session_state.score = 0
    st.session_state.current_q = 0

q = questions[st.session_state.current_q]
st.subheader(f"Q{st.session_state.current_q+1}: {q['q']}")

choice = st.radio("Choose your answer:", q['options'])

if st.button("Submit Answer"):
    if choice == q['answer']:
        st.success(f"Correct! ✅ Answer is {q['answer']}")
        st.session_state.score += 1
    else:
        st.error(f"Wrong ❌ Correct answer is {q['answer']}")
    
    if st.session_state.current_q < len(questions)-1:
        st.session_state.current_q += 1
        st.rerun()
    else:
        st.balloons()
        st.write(f"### Final Score: {st.session_state.score}/{len(questions)}")
        if st.button("Restart Quiz"):
            st.session_state.score = 0
            st.session_state.current_q = 0
            st.rerun()

st.sidebar.write(f"Score: {st.session_state.score}")
