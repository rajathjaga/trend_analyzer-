import streamlit as st
import requests
import json

# API URLs
post_url = 'https://eandz94j6f.execute-api.eu-north-1.amazonaws.com/demo/'
trending_hashtags_url = 'https://eandz94j6f.execute-api.eu-north-1.amazonaws.com/demo/'

# Initialize session state
if 'trending_hashtags' not in st.session_state:
    st.session_state.trending_hashtags = []

def invoke_lambda(url, payload=None):
    try:
        if payload:
            response = requests.post(url, json=payload)
            print('POST response:', response.text)  # Print the response content
        else:
            response = requests.get(url)
            print('GET response:', response.text)  # Print the response content

        response.raise_for_status()
        return response.json()  # Parse JSON response
    except requests.exceptions.RequestException as e:
        st.error(f"Error: {e}")
        return None

# Streamlit UI
st.title("Post Composer & Trending Hashtags")

# Post Section
st.header("Compose a Post")
post_text = st.text_area("Write your post here (use hashtags like #example):")
if st.button("Post"):
    if post_text:
        post_content = {"text": post_text}
        response = invoke_lambda(post_url, post_content)
        # Handle Lambda response
        if response:
            st.success("Post submitted successfully!")
        else:
            st.error("There was an error submitting your post.")
    else:
        st.error("Please enter some text before submitting!")

# Get Trending Hashtags Section
st.header("Trending Hashtags")

if st.button("Get Trending Hashtags"):
    response = invoke_lambda(trending_hashtags_url)
    print('Trending Hashtags Response:', response)
    if response and 'trending_hashtags' in response:
        # Split the hashtags by newline characters to create a list
        st.session_state.trending_hashtags = response['trending_hashtags'].split('\n')

# Display trending hashtags
if st.session_state.trending_hashtags:
    st.write("Trending Hashtags:")
    for hashtag in st.session_state.trending_hashtags:
        st.write(f"- {hashtag}")
else:
    st.info("No trending hashtags at the moment.")
