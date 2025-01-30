# 📩 Daily Report Generator from .py Files

This project automates the process of summarizing Python script files and sending daily progress reports via email. It leverages Google's Generative AI (Gemini) to generate summaries and SMTP for email delivery.

## Features

- Reads a Python script file and generates a concise summary using AI.
- Formats the summary into a structured email.
- Sends the email to the specified recipient using Gmail SMTP.
- Stores sensitive information (API key & email credentials) securely in a `.json` file.

## Installation

### Prerequisites

- Python 3.x
- A Gmail account with [App Passwords](https://support.google.com/accounts/answer/185833?hl=en) enabled.
- Google Generative AI API key.
- `pip` for installing dependencies.

### Setup

1. Clone this repository:

   ```bash
   git clone https://github.com/noornabeelak/daily-report-generator-from-.py-files
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.json` file in the root directory and add your credentials:

   ```bash
   EMAIL_API_KEY=your_google_api_key
   EMAIL_APP_PASSWORD=your_gmail_app_password
   ```

4. Run the script:

   ```bash
   python main.py
   ```

## Usage

1. When you run the script (main.py) , it will prompt you to enter:
   - Path to the `.py` file
   - Sender email
   - Receiver email
   - Receiver’s name
   - Your name
2. The script will generate a summary of the Python file and send an email formatted as:
   ```
   Hey [Receiver's Name],

   Today's progress is:
   [Summary of the Python file]

   Thanks & Regards,
   [Your Name]
   ```

## Project Structure
```
.
├── main.py                # Main script to summarize and send emails
├── genai_summarizer.py    # Handles AI-based code summarization
├── send_email.py          # Manages email sending functionality
├── config.json            # Stores API keys and credentials (not included in repo)
├── LICENSE                # License for the project
└── README.md              # Project documentation
```


## Technologies Used

- **Python** for scripting
- **Google Generative AI (Gemini)** for summarization
- **SMTP (Gmail)** for sending emails
- **dotenv** for environment variable management

## Contribution

Contributions are welcome! Feel free to open issues and submit pull requests for enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Author

**Noor Nabeela K**

---

Give a ⭐ if you found this helpful!

