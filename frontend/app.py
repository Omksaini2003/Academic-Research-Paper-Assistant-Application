import streamlit as st
import requests

PORT = 8501

# Title of the Streamlit app
st.title("Academic Research Paper Assistant")

# Text input for the search query
query = st.text_input("Enter your topic:")

# Button to trigger the search
if st.button("Search"):
    if query:  # Ensure query is not empty
        try:
            # Sending GET request to the backend search endpoint
            response = requests.get(f"http://localhost:{PORT}/search", params={"query": query})
            
            # Check if the response has content
            if response.status_code == 200:
                try:
                    data = response.json()  # Try to parse JSON
                    st.write(data)  # Display the JSON response from the server
                except ValueError:
                    st.error("The response does not contain valid JSON.")
                    st.write(response.text)  # Show raw response text
            else:
                st.error(f"Failed to fetch data from the server. Status code: {response.status_code}")
                st.write(response.text)  # Show raw response content for debugging
        except requests.exceptions.RequestException as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a topic to search.")

# Text area for asking a question about a paper
question = st.text_area("Ask a question about a paper:")

# Input field for the paper ID
paper_id = st.text_input("Paper ID")

# Button to trigger the question-answer request
if st.button("Get Answer"):
    if question and paper_id:  # Ensure both fields are filled out
        try:
            # Sending POST request with question and paper ID
            response = requests.post(f"http://localhost:{PORT}/qa/", json={"question": question, "paper_id": paper_id})
            
            # Check if the response has content
            if response.status_code == 200:
                try:
                    data = response.json()  # Try to parse JSON
                    st.write(data)  # Display the answer from the server
                except ValueError:
                    st.error("The response does not contain valid JSON.")
                    st.write(response.text)  # Show raw response text
            else:
                st.error(f"Failed to get an answer from the server. Status code: {response.status_code}")
                st.write(response.text)  # Show raw response content for debugging
        except requests.exceptions.RequestException as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please provide both a question and a paper ID.")
