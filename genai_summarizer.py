# import google.generativeai as genai
# import os

# # Set your Google API key
# genai.configure(api_key="AIzaSyDZj-6lNVCVIb3XMtJSa1k_iJOAbdBOAgM")

# def summarize_code(file_path):
#     """
#     Reads a .py file and generates a summary using Google's Generative AI API.
    
#     Args:
#         file_path (str): Path to the Python file to summarize.

#     Returns:
#         str: The summary of the Python code or an error message.
#     """
#     try:
#         # Check if the file exists
#         if not os.path.exists(file_path):
#             return "Error: File not found. Please provide a valid file path."

#         # Read the Python file
#         with open(file_path, "r", encoding="utf-8") as file:
#             code_content = file.read()

#         # Create a model instance
#         model = genai.GenerativeModel("gemini-1.5-flash")

#         # Generate a summary using Gemini AI
#         prompt = f"Summarize the following Python code:\n\n{code_content}"
#         response = model.generate_content(prompt)

#         return response.text if response else "Error: No response from the model."
    
#     except Exception as e:
#         return f"Error during summarization: {str(e)}"


import google.generativeai as genai 
import os
import json

# Load the config file
with open('config.json', "r") as file:
    config = json.load(file)

# Configure Google API key
genai.configure(api_key=config.get("google_api_key")) 


def summarize_code(file_path):
    """
    Reads a .py file and generates a summary using Google's Generative AI API.
    
    Args:
        file_path (str): Path to the Python file to summarize.

    Returns:
        str: The summary of the Python code or an error message.
    """
    try:
        if not os.path.exists(file_path):
            return "Error: File not found. Please provide a valid file path."

        with open(file_path, "r", encoding="utf-8") as file:
            code_content = file.read()

        model = genai.GenerativeModel("gemini-1.5-flash")
        prompt = f"Summarize the following Python code:\n\n{code_content}"
        response = model.generate_content(prompt)

        return response.text.strip() if response else "Error: No response from AI."
    
    except Exception as e:
        return f"Error during summarization: {str(e)}"

def generate_email_content(receiver_name, summary, sender_name):
    """
    Generates an email message using Google's Generative AI.

    Args:
        receiver_name (str): Name of the email recipient.
        summary (str): The summarized Python code.
        sender_name (str): Name of the sender.

    Returns:
        str: A formatted email message.
    """
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        prompt = f"""Write a friendly and professional email.

        Hey {receiver_name},

        Today's progress is:

        {summary}

        Thanks & Regards,
        {sender_name}
        """
        response = model.generate_content(prompt)
        
        return response.text.strip() if response else "Error: No response from AI."
    
    except Exception as e:
        return f"Error generating email content: {str(e)}"
