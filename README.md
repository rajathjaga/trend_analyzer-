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
   git clone <repository-url>
   cd post-composer-app

2. **Create and activate a virtual environment:**

   ```sh
   python -m venv venv
   venv\Scripts\activate

3. **Install the dependencies:**

   ```sh
   pip install -r requirements.txt

