# Post Composer & Trending Hashtags App

This is a Streamlit-based web application that allows users to compose and publish posts, with integrated real-time trending hashtag analysis using AWS Lambda and DynamoDB.

## Features

- Users can compose and publish posts containing text and hashtags.
- Posts are processed by AWS Lambda and stored in DynamoDB, maintaining the integrity of the post text and hashtags.
- The application accurately identifies and displays trending hashtags based on the analysis of posts in DynamoDB.
- Trending hashtags are updated dynamically after a new post is made, providing real-time insights.

## Prerequisites

To run this project, you need to have the following installed:

- Python 3.7+
- pip
- virtualenv

## Setup Instructions

1. **Clone the repository:**

   ```sh
   git clone https://github.com/rajathjaga/trend_analyzer-.git
   cd post-composer-app

2. **Create and activate a virtual environment:**

   ```sh
   python -m venv venv
   venv\Scripts\activate

3. **Install the dependencies:**

   ```sh
   pip install -r requirements.txt

## Running the Application

1. **Start the Streamlit application:**

   ```sh
   streamlit run app.py

## Usage

- Compose a Post: 
      Write your post in the text area provided on the app interface and click the "Post" button. Your post will be processed by AWS Lambda and stored in DynamoDB.

- Trending Hashtags: 
      After a successful post, trending hashtags are updated automatically to reflect the latest trending terms in real time.

## Technologies Used

- Python: Backend logic using requests, json, and other standard libraries.
- Streamlit: Framework for creating the web UI.
- AWS Lambda: Serverless function to handle post requests and process data.
- DynamoDB: NoSQL database for storing posts and hashtags.

## How it Works

- Users compose posts, which may contain hashtags (e.g., #example).
- Posts are sent to an AWS Lambda function, which processes and stores them in DynamoDB.
- When a new post is successfully submitted, users can click the 'Get Trending Hashtags' button to fetch and update the latest trending hashtags
- Users can view the trending hashtags in real time.