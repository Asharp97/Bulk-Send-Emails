# Donnate Charity Email Automation

This project automates the process of sending partnership invitation emails to UK charities, tracking email status, and managing charity contact data. It uses Python, SQLite, and pandas for data handling and email automation.

## Features

- **Bulk Email Sending:** Sends personalized HTML emails to charities listed in a CSV file.
- **Email Tracking:** Uses an SQLite database to track which charities have been contacted.
- **Data Cleaning:** Removes invalid email entries from the CSV.
- **Database Reset:** Resets the email tracking status for testing or re-sending purposes.

## File Overview

- `main.py`: Main script to send emails to charities that have not yet been contacted.
- `add.py`: Adds an `email_sent` column to the CSV for tracking purposes.
- `remove.py`: Cleans the CSV by removing rows where the email is invalid (starts with 'null').
- `reset_database.py`: Resets the `email_sent` status in the database, allowing emails to be resent.
- `UK_charities.csv`: The source CSV file containing charity names and email addresses.
- `email_tracking.db`: SQLite database for tracking email status.
- `body.html`: (Optional) HTML template for the email body.
- `image.png`, `store1.png`, `store2.png`: Images used in the email signature.

## Setup Instructions

1. **Install Dependencies:**
   ```bash
   pip install pandas
   ```
2. **Prepare Data:**
   - Place your charity data in `UK_charities.csv` with columns for `Name` and `email`.
   - Run `add.py` to add the `email_sent` column if not present.
   - Run `remove.py` to clean invalid emails.
3. **Initialize Database:**
   - The database is created automatically by the scripts if it does not exist.
   - You can reset the database using `reset_database.py`.
4. **Configure Email Credentials:**
   - Update `email_sender` and `email_password` in `main.py` with your Gmail credentials (use an app password for Gmail).
5. **Send Emails:**
   - Run `main.py` to send emails to all charities that have not yet been contacted.

## Usage

- To send emails:
  ```bash
  python main.py
  ```
- To reset email status (for testing):
  ```bash
  python reset_database.py
  ```
- To clean the CSV:
  ```bash
  python remove.py
  ```
- To add the tracking column:
  ```bash
  python add.py
  ```

## Notes

- Make sure to enable access for less secure apps or use an app password for Gmail.
- The email body is hardcoded in `main.py` but can be moved to `body.html` for easier editing.
- Images referenced in the email should be accessible to recipients (consider hosting them online for production use).

## License

This project is for educational and outreach purposes. Please adapt as needed for your organization.
