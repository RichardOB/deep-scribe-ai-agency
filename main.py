import os
from getpass import getpass

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

if not os.getenv('OPENAI_KEY'):
    os.environ['OPENAI_API_KEY'] = getpass('Enter Open AI API Key: ')


if not os.getenv('TAVILY_API_KEY'):
    os.environ['TAVILY_API_KEY'] = getpass('Enter Tavily Search API Key: ')


if __name__ == '__main__':
    print("Welcome to the beginnings of your Advanced Deep Researcher employee")