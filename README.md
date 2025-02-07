# BrainChat AI

## Overview
BrainChat AI is a chatbot application built using Flask and LangChain. It utilizes a Hugging Face model for inference and FAISS for efficient retrieval of relevant context from pre-embedded documents.

## Features
- Loads data from a specified URL.
- Uses FAISS for vector search.
- Embeds text using `sentence-transformers/all-MiniLM-L6-v2`.
- Generates responses using `mistralai/Mistral-7B-Instruct-v0.3`.
- Simple web interface built with HTML, CSS (Bootstrap), and JavaScript.

## Requirements
Ensure you have the following installed:
- Python 3.8+
- Flask
- LangChain
- FAISS
- Hugging Face Hub
- dotenv

## Installation
1. Clone this repository:
   ```bash
   git clone <repository_url>
   cd BrainChat-AI
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up environment variables:
   - Create a `.env` file and add your Hugging Face token:
     ```
     HF_TOKEN=your_huggingface_token
     ```
4. Run the application:
   ```bash
   python app.py
   ```
5. Open your browser and visit:
   ```
   http://127.0.0.1:5000/
   ```

## Usage
- Enter a query in the chatbot interface.
- The AI processes your input and returns a response.
- No source information is displayed.



## Future Improvements
- Improve response accuracy with better embedding models.
- Add support for additional document sources.
- Enhance frontend UI with more interactive features.

## License
This project is licensed under the MIT License.

