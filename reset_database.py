import pandas as pd
import sqlite3

# Create/connect to SQLite database
conn = sqlite3.connect('email_tracking.db')
cursor = conn.cursor()

# cursor.execute('''
# CREATE TABLE IF NOT EXISTS email_status (
#     id INTEGER PRIMARY KEY,
#     Name TEXT,
#     email TEXT,
#     email_sent BOOLEAN DEFAULT 0
# )
# ''')

# data = pd.read_csv('UK_charities.csv')
# data.to_sql('email_status', conn, if_exists='replace', index=False)

# Query for unsent emails
sent_emails = pd.read_sql('SELECT * FROM email_status WHERE email_sent = 1', conn)


# Process unsent emails
for _, row in sent_emails.iterrows():
    print(f"Sending email to {row['Name']} at {row['email']}...")

    cursor.execute('UPDATE email_status SET email_sent = 0 WHERE id = ?', (row['id'],))

    conn.commit()

conn.close()


