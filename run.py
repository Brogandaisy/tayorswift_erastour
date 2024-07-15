import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

# Define the scope
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

# Add credentials to the account
creds = ServiceAccountCredentials.from_json_keyfile_name('/workspace/tayorswift_erastour/creds.json', scope)

# Authorize the client sheet 
client = gspread.authorize(creds)

# Get the instance of the Spreadsheet
sheet = client.open('taylorswift_erastour')

# Get the first sheet of the Spreadsheet
worksheet = sheet.get_worksheet(0)

# Get all the records of the data
records = worksheet.get_all_records()

# Convert the records to a DataFrame
df = pd.DataFrame(records)

# Display the first few rows of the DataFrame
print(df.head())

# Perform data analysis (e.g., descriptive statistics)
print(df.describe())
