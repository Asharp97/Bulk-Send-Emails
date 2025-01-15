import pandas as pd 
 
# Read the existing CSV file into a DataFrame 
df = pd.read_csv('UK_charities.csv', on_bad_lines='skip')  # or 'warn' or 'error'
 
# Add a new column with default values (e.g., NaN or a specific value) 
df['email_sent'] = False  # You can also use a list of values if you have specific values for each row 
 
# Write the updated DataFrame back to the CSV file 
df.to_csv('UK_charities.csv', index=False)