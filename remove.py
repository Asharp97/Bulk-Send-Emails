import pandas as pd

# Load the original CSV file
input_file = 'UK_charities.csv'

# Read the CSV file
data = pd.read_csv(input_file)

# Filter out rows where email starts with 'null'
data = data[~data['email'].astype(str).str.startswith('null')]

# Save the updated data back to the original file
data.to_csv(input_file, index=False)

print("Rows where email starts with 'null' have been removed.")
