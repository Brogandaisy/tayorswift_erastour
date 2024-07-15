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


def get_survey_data():
    """
    Get survey data from the google sheet / taylorswift_erastour.
    """
    print("Find out more from our Eras Tour Survey\n")
    print("1. How many females compared to males were there?")
    print("2. What is the average age of the fans?")
    print("3. What country had the most fans attending?")
    print("4. What was the favourite album of the fans?")
    print("5. What was the favourite song from the fans?")
    print("6. What was the lowest inputted favourite song and album?")
    print("7. What was the average age of 'Reputation' fans?")
    print("8. What was the majority gender for fans of 'Lover'? \n")

    data_str = input("Enter the question number here: ")
    print(f"The data provided is {data_str}")

get_survey_data()
