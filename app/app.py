import streamlit as st
from src.chatbot import ask_algo_whiz

# Streamlit app setup
st.set_page_config(page_title="AlgoWhiz: Your AI DSA Guru-Bot", layout="wide")
st.title("AlgoWhiz: Your AI DSA Guru-Bot")
st.write("Ask any question about data structures and algorithms!")

# Sidebar for Instructions
st.sidebar.header("Instructions")
st.sidebar.write("""
- Enter your question in the input box below.
- You can ask about algorithms, data structures, time complexities, etc.
- Click on the buttons below for predefined answers.
""")

# Examples of questions
st.subheader("**Examples of questions you can ask:**")
example_questions = [
    "What is a binary search tree?",
    "How do I implement a quick sort algorithm?",
    "Can you explain dynamic programming?",
    "What is the time complexity of a linear search?",
    "Write code for a merge sort.",
    "What are the different types of data structures?"
]
for question in example_questions:
    st.markdown(f"- **{question}**")

# Text input box for user questions
user_input = st.text_input("You:", placeholder="Type your question here...")

# Respond to user's input
if user_input:
    response = ask_algo_whiz(user_input)
    
    # Error handling for the response
    if isinstance(response, str):
        st.write("**AlgoWhiz:** ", response)
    elif isinstance(response, list):
        st.write("**AlgoWhiz:** Here are some responses:")
        for res in response:
            st.write(f"- {res}")
    else:
        st.write("**AlgoWhiz:** I could not generate a valid response. Please try again.")

# Predefined DSA code for Bubble Sort
def show_bubble_sort_code():
    return """
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
    """

# Button to show predefined answers
if st.button("Show Bubble Sort Code", key="bubble_sort_button"):
    bubble_sort_code = show_bubble_sort_code()  # Call the function to get the code
    st.code(bubble_sort_code, language="python")

# You can add more buttons for other algorithms similarly:
# if st.button("Show Selection Sort Code"):
#     selection_sort_code = show_selection_sort_code()
#     st.code(selection_sort_code, language="python")
