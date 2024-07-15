import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

# Set up Google Sheets API credentials and access
SCOPE = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
CREDS = ServiceAccountCredentials.from_json_keyfile_name('/workspace/tayorswift_erastour/creds.json', SCOPE)
CLIENT = gspread.authorize(CREDS)
SHEET = CLIENT.open('taylorswift_erastour')
worksheet = SHEET.get_worksheet(0)
records = worksheet.get_all_records()
df = pd.DataFrame(records)


# Define functions for each question
def compare_genders():
    gender_counts = df['Gender'].value_counts()
    print(f"Number of females: {gender_counts.get('Female', 0)}")
    print(f"Number of males: {gender_counts.get('Male', 0)}")
    print(f"Number of non-binary: {gender_counts.get('Non-binary', 0)}")
    print(f"Number of other: {gender_counts.get('Other', 0)}")
def average_age():
    avg_age = df['Age'].mean()
    print(f"The average age of the fans is: {avg_age:.2f}")
def most_fans_country():
    country_counts = df['Country'].value_counts()
    most_fans = country_counts.idxmax()
    print(f"The country with the most fans attending is: {most_fans}")
def favorite_album():
    fav_album_counts = df['Favourite Album'].value_counts()
    fav_album = fav_album_counts.idxmax()
    print(f"The favourite album of the fans is: {fav_album}")
def favorite_album():
    fav_album_counts = df['Favourite Album'].value_counts()
    fav_album = fav_album_counts.idxmax()
    print(f"The favourite album of the fans is: {fav_album}")
def favorite_song():
    fav_song_counts = df['Favourite Song'].value_counts()
    fav_song = fav_song_counts.idxmax()

# Main function to get user input and call the appropriate function
def get_survey_data():
    """
    Get survey data from the Google Sheet / taylorswift_erastour.
    """
    print("Find out more from our Eras Tour Survey\n")
    print("1. How many females compared to males were there?")
    print("2. What is the average age of the fans?")
    print("3. What country had the most fans attending?")
    print("4. What was the favourite album of the fans?")
    print("5. What was the favourite song from the fans?")

    try:
        question_number = int(input("Enter your question number here: "))
        if question_number == 1:
            compare_genders()
        elif question_number == 2:
            average_age()
        elif question_number == 3:
            most_fans_country()
        elif question_number == 4:
            favorite_album()
        elif question_number == 5:
            favorite_song()
        else:
            print("Invalid question number. Please enter a number between 1 and 8.")
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 8.")

# Run the main function
get_survey_data()

