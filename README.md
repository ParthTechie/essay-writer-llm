# Essay Writer LLM

An AI-powered essay generator using Groq's LLM API.

## Features

- Generate high-quality essays on any topic
- Streamlit web interface for easy interaction
- Configurable parameters (model, length, temperature)
- Download generated essays as text files

## Project Structure

essay_writer_project/

- config/            # Configuration settings
- models/            # LLM essay generation models
- utils/             # Helper utilities
- app.py             # Streamlit application
- requirements.txt   # Project dependencies

## Installation

1. Clone this repository:
   - git clone https://github.com/YourUsername/essay-writer-llm.git
   - cd essay-writer-llm

2. Install dependencies:
   - pip install -r requirements.txt

3. Create a `.env` file with your Groq API key:
   - GROQ_API_KEY=your_api_key_here

## Usage

4. Run the Streamlit application:
   - streamlit run app.py

