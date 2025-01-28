import smtplib
email=input("sender email: ")
receiver_email=input("receiver email: ")

subject=input("subject: ")
message=input("message: ")

text=f"Subject: {subject}\n\n{message}"

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()

server.login(email, "lxqw wsty zfnd rahi")
server.sendmail(email, receiver_email, text)

print("Email sent successfully to",receiver_email)
