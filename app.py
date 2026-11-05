
import streamlit as st
from chatbot import CollegeChatbot
from knowledge_base import COLLEGE_FAQS

# Page configuration
st.set_page_config(
    page_title="College Enquiry Chatbot",
    page_icon="🎓",
    layout="centered"
)

# Custom CSS
st.markdown("""
<style>
.main {
    background-color: #f5f7fb;
}
.title {
    text-align: center;
    color: #1e3a8a;
    font-size: 32px;
    font-weight: bold;
}
.subtitle {
    text-align: center;
    color: #555;
    font-size: 16px;
}
</style>
""", unsafe_allow_html=True)

# Heading
st.markdown(
    '<p class="title">🎓 College Enquiry Chatbot</p>',
    unsafe_allow_html=True
)

st.markdown(
    '<p class="subtitle">Ask questions about admissions, courses, fees and facilities.</p>',
    unsafe_allow_html=True
)

st.divider()

# Initialize chatbot
@st.cache_resource
def load_chatbot():
    return CollegeChatbot(COLLEGE_FAQS)

bot = load_chatbot()

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": (
                "Hello! 👋 Welcome to the College Enquiry Chatbot. "
                "How can I help you today?"
            )
        }
    ]

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
prompt = st.chat_input("Type your college enquiry here...")

if prompt:
    # Display user message
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate chatbot response
    response = bot.get_response(prompt)

    # Display response
    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )

    with st.chat_message("assistant"):
        st.markdown(response)

# Sidebar
with st.sidebar:
    st.title("🎓 College Help Desk")

    st.write("You can ask questions about:")

    st.markdown("""
    - 📚 Courses
    - 📝 Admissions
    - 💰 Fees
    - 🏠 Hostel facilities
    - 🚌 Transportation
    - 📖 Library
    - 📅 Examinations
    - 💼 Placements
    """)

    st.divider()

    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

    st.caption("Powered by Python, NLTK and Streamlit")
