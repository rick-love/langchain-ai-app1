# Overview:
## Project Based on Free Code Camp Video

This project is based on the following Free Code Camp video tutorial using Langchain and Python:

[Free Code Camp Video Tutorial](https://www.youtube.com/watch?v=lG7Uxts9SXs)

1. Pet Name Generator
2. Youtube Assistant


# Technical Setup:
VS Code
Python3 - Install, upgrade and Activate the Virtual Environment

## Activate the Virtual Environment
cmdline: source App Folder Path + /venv/bin/activate
(venv)

## Packages Used:
pip3 install langchain openai streamlit python-dotenv tiktoken youtube-transcript-api faiss-cpu watchdog
Streamlit for Python UI Creation Command:
streamlit run main.py


# Python Virtual Environment Setup Instructions

## Install Virtualenv

- If you haven't already installed virtualenv, open your terminal and run:
  ```
  pip3 install virtualenv
  ```
- Virtualenv is a tool to create isolated Python environments.

## Create a New Virtual Environment

1. Navigate to your project directory in the terminal.
2. Run the following command to create a new virtual environment named 'venv':
   ```
   virtualenv venv
   ```
   You can name it anything you like.

## Activating the Virtual Environment

1. In the terminal, navigate to your project directory.
2. Run the following command to activate the virtual environment:
   ```
   source venv/bin/activate
   ```
   You'll know it's activated when you see `(venv)` before the prompt in your terminal.

## Setting Up in VS Code

1. Open your project in VS Code.
2. Press `Cmd + Shift + P` to open the Command Palette.
3. Type and select `Python: Select Interpreter`.
4. Choose the interpreter that matches your virtual environment.

## Verifying the Setup

- To ensure everything is set up correctly, open a new terminal in VS Code.
- The virtual environment should automatically activate (you'll see `(venv)` in the terminal). If not, you can manually activate it as described above.

## Deactivating the Virtual Environment

- When you're done working, you can deactivate the virtual environment by simply typing `deactivate` in the terminal.
