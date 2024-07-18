import gspread
from google.oauth2.service_account import Credentials
import pandas as pd

# Set up Google Sheets API credentials and access
SCOPE = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
CREDS = Credentials.from_service_account_file('creds.json', scopes=SCOPE)
CLIENT = gspread.authorize(CREDS)

# Access your Google Sheet
SHEET = CLIENT.open('taylorswift_erastour')
worksheet = SHEET.get_worksheet(0)
records = worksheet.get_all_records()
df = pd.DataFrame(records)


# Defined functions for each question
"""
Counts the different genders from the survey data
"""
def compare_genders():
    gender_counts = df['Gender'].value_counts()
    print(f"Number of females: {gender_counts.get('Female', 0)}")
    print(f"Number of males: {gender_counts.get('Male', 0)}")
    print(f"Number of non-binary: {gender_counts.get('Non-binary', 0)}")
    print(f"Numbe6r of other: {gender_counts.get('Other', 0)}")
"""
Calculates the average age of the fans from the survey data
"""
def average_age():
    avg_age = df['Age'].mean()
    print(f"The average age of the fans is: {avg_age:.2f}")
"""
Calculates the majority country of the fans from the survey data
"""
def most_fans_country():
    country_counts = df['Country'].value_counts()
    most_fans = country_counts.idxmax()
    print(f"The country with the most fans attending is: {most_fans}")
"""
Calculates the highest favourite album response from the survey data
"""
def favorite_album():
    fav_album_counts = df['Favourite Album'].value_counts()
    fav_album = fav_album_counts.idxmax()
    print(f"The favourite album of the fans is: {fav_album}")
"""
Calculates the highest favourite song response from the survey data
"""
def favorite_song():
    fav_song_counts = df['Favourite Song'].value_counts()
    
    fav_song = fav_song_counts.idxmax()
    print(f"The favourite song of the fans is: {fav_song}")
"""
Calculates album stats from each album from the survey data, including average age, gender and country
"""
def album_stats(album):
    album_fans = df[df['Favourite Album'] == album]
    if album_fans.empty:
        print(f"No data available for the album '{album}'")
        return
    
    avg_age_album = album_fans['Age'].mean()
    gender_counts_album = album_fans['Gender'].value_counts()
    country_counts_album = album_fans['Country'].value_counts()
    
    most_common_gender = gender_counts_album.idxmax()
    most_common_country = country_counts_album.idxmax()
    
    print(f"Statistics for '{album}' fans:")
    print(f" - Average age: {avg_age_album:.2f}")
    print(f" - Most common gender: {most_common_gender}")
    print(f" - Country with most fans: {most_common_country}")

# Main function to get user input and call the appropriate function
def get_survey_data():
    """
    Prints the questions to the user, so they can select a number relating to each one
    """
    while True:
        print("\nFind out more from our Eras Tour Survey\n")
        print("1. How many females compared to males were there?")
        print("2. What is the average age of the fans?")
        print("3. What country had the most fans attending?")
        print("4. What was the favourite album of the fans?")
        print("5. What was the favourite song from the fans?")
        print("6. Get detailed statistics for a specific album")
        print("0. Exit")

        try:
            question_number = int(input("Enter your question number here: \n"))
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
            elif question_number == 6:
                albums = ["Speak Now", "Evermore", "Fearless", "Folklore", "Lover", "Midnights", "Red", "Reputation"]
                print("\nChoose your album from the list:")
                for counter, album in enumerate(albums):
                    print(f"{counter + 1}. {album}")
                album_number = int(input("Enter the number corresponding to your album: "))
                if 1 <= album_number <= len(albums):
                    album = albums[album_number - 1]
                    album_stats(album)
                else:
                    print("Invalid album number.")
            elif question_number == 0:
                print("Exiting the survey.")
                break
            else:
                print("Invalid question number. Please enter a number between 1 and 6.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Run the main function
get_survey_data() 