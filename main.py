from genai_summarizer import summarize_code, generate_email_content
from send_email import send_email

if __name__ == "__main__":
    # Input details
    file_path = input("Enter the path to the .py file: ")
    sender_email = input("Sender email: ")
    receiver_email = input("Receiver email: ")
    receiver_name = input("Receiver's Name: ")
    sender_name = input("Your Name: ")
    subject = "Today's Progress Update"

    # Summarize the Python script
    summary = summarize_code(file_path) 
    print("Summary:\n", summary)

    # Generate formatted email content
    email_content = generate_email_content(receiver_name, summary, sender_name)  
    
    # Send the email
    send_email(sender_email, receiver_email, subject, email_content)
