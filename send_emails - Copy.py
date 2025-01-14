import smtplib
import ssl
from email.message import EmailMessage
import time
import openpyxl

# Email configuration (should be moved to a more secure location, like Secret Manager)
email_sender = 'ali.elsayed@donnate.org'
email_password = 'galp orav wnep gofc'  # Consider using Secret Manager
subject = 'test is successful'

def send_emails_from_xlsx(filepath, limit=100):
    """Sends emails to recipients listed in an Excel file.

    Args:
        filepath: Path to the Excel file.
        limit: Maximum number of emails to send.
    """

    try:
        workbook = openpyxl.load_workbook(filepath)
        sheet = workbook.active  # Assumes data is in the first sheet

        sent_count = 0
        for row in sheet.iter_rows(min_row=2, values_only=True): # Start from row 2 assuming headers in row 1.
            name, email_receiver = row[0], row[1]  # Assuming name is in column A and email in column B. Adjust indices as needed.

            if email_receiver is not None and str(email_receiver).strip() != "" and sent_count < limit: #Check for null/empty email
                body = f"""
                Dear {name},
                This is a message.
                """

                em = EmailMessage()
                em['From'] = email_sender
                em['To'] = email_receiver
                em['Subject'] = subject
                em.set_content(body)

                context = ssl.create_default_context()
                with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
                    smtp.login(email_sender, email_password)
                    smtp.sendmail(email_sender, email_receiver, em.as_string())

                sent_count += 1
                time.sleep(3)  # Wait for 3 seconds


    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
    except Exception as e:
        print(f"An error occurred: {e}")



# Example usage: Replace 'contacts.xlsx' with your actual file name
send_emails_from_xlsx('contacts.xlsx')