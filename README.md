# DeepScribe AI Agency

DeepScribe AI Agency is a cutting-edge research and reporting platform powered by AI. It performs deep investigations into topics of interest and compiles comprehensive, insightful reports. Whether you're delving into market trends, scientific research, or any other subject, DeepScribe helps you get to the core of the data.

## Features

- **Deep Research:** Leverages advanced AI to perform thorough analyses.
- **Automated Reporting:** Compiles clear, detailed reports based on research data.
- **Easy Setup:** Utilizes Python 3.13.1, a conda environment, and pip tools for dependency management.

## Prerequisites

- **Python:** Version 3.13.1
- **Conda:** For managing environments ([Conda Installation](https://docs.conda.io/en/latest/miniconda.html))
- **pip-tools:** For compiling dependencies from `requirements.in` to `requirements.txt`

## Installation

Follow these steps to get the project running on your machine:

1. **Clone the Repository**
   ```bash
    git clone git@github.com:RichardOB/deep-scribe-ai-agency.git
    cd deep-scribe-ai-agency
   ```
   
2. Create and Activate a Conda Environment
    ```bash
    conda create -n deepscribe python=3.13.1
    conda activate deepscribe
    ```

3. Install Dependencies First, compile your requirements.in into requirements.txt (if you haven’t already):
    ```bash
    pip install pip-tools  # if not already installed
    pip-compile requirements.in
    ```
   
4. Then install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

5. Set Up Environment Variables Copy the example environment file and update it with your secret keys:
    ```bash
    cp .env.example .env   
    ```
   
6. Open .env in your preferred text editor and add your credentials:
    ```bash
    OPENAI_KEY=your_openai_key_here
    TAVILY_API_KEY=your_tavily_api_key_here
    ```

## Running the Project

After installing the dependencies and configuring the environment, you can start the DeepScribe AI Agency:

```bash
python main.py
```