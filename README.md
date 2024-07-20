# Taylor Swift Eras Tour Survey Data
Project 3 - Brogan Carpenter

[View Live Project]()

# About the Project

This project is analysing the data found in a google sheet from a survey asked to fans who attended one of the Eras Tour shows by Taylor Swift. The survey asked 150 fans the following questions:

- Name
- Age
- Gender
- Country
- Favourite Taylor Swift Song
- Favourite Taylor Swift Album

See google sheet data below.

![Google Sheet Data](https://github.com/Brogandaisy/tayorswift_erastour/blob/main/assets/images/ts.googlesheet.png)

With the data collected in a google sheet, I used the following python code to create a program for users to quickly get select types of data fast from the survey. 
Including:

- Average age of fans attending
- Gender breakdown of fans attending
- Most visited country fans are attending from
- Most requested favourite album
- Most requested favourite song

I then also included the following data about the fans depending on their favourite album. For example, if you wanted to know the average age and most common gender of fans whose favourite album is 'Red'.

![App Display](https://github.com/Brogandaisy/tayorswift_erastour/blob/main/assets/images/ts_app_display1.png)

# Features

Within the python code, I included a range of features to allow the data to be pulled quickly, efficiently and accurately. The google sheet is connected by using google cloud and installing Google Drive and Google Sheets API's, and downloading the credentials to the code. This allowed the data to be pulled directly from the google sheet when using my functions.

## Number Based Question System
This allowed the data to be easily understood from the Google Sheet, and it also allowed the user to decide what data they needed from the survey.

The questions were printed to the program followed by a number. The user was then asked to type in the number displayed next to the question they wanted to ask. 
For example, 

    print("1. How many females compared to males were there?")
    print("2. What is the average age of the fans?")
    print("3. What country had the most fans attending?")
    print("4. What was the favourite album of the fans?")
    print("5. What was the favourite song from the fans?")
    print("6. Get detailed statistics for a specific album")

The user would enter 5 if they wanted to know the favourite song of the fans.

The code used for this is an if/elif statement, with an equals == to the number matching the question, followed by the function call for the question. This makes it reactive to what the user inputs to the program. See below:

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

![Number Question System](https://github.com/Brogandaisy/tayorswift_erastour/blob/main/assets/images/ts.app.display6.png)

For question 6, it is a little different. As I wanted the user to be asked a second question so they can select their chosen album using the number system. Instead of allowing the user to input the album as a string, which could allow mistakes to be made (spelling, capitalization errors, or an album not listed in the survey). Using a list and number system allowed the user to get the correct data for their chosen album.

![Question 6, Secondary Question](https://github.com/Brogandaisy/tayorswift_erastour/blob/main/assets/images/ts_app_display3.png)

![Question 6, Answer Display](https://github.com/Brogandaisy/tayorswift_erastour/blob/main/assets/images/ts_app_display4.png)

## While Loop
The program includes a 'while loop', which repeats the question input box after their answer has been processed. There is also an exit function to the loop, using the same easy to use number system, '0' to exit. 

    while True:
        print("\nFind out more from our Eras Tour Survey\n")
        print("1. How many females compared to males were there?")
        print("2. What is the average age of the fans?")
        print("3. What country had the most fans attending?")
        print("4. What was the favourite album of the fans?")
        print("5. What was the favourite song from the fans?")
        print("6. Get detailed statistics for a specific album")
        print("0. Exit")

    elif question_number == 0:
                print("Exiting the survey.")
                break

## Enumerate / Counter

            elif question_number == 6:
                albums = ["Speak Now",
                          "Evermore",
                          "Fearless",
                          "Folklore",
                          "Lover",
                          "Midnights",
                          "Red",
                          "Reputation"]
                print("\nChoose your album from the list:")
                for counter, album in enumerate(albums):
                    print(f"{counter + 1}. {album}")
                album_number = int(input("Enter the album number: "))
                if 1 <= album_number <= len(albums):
                    album = albums[album_number - 1]
                    album_stats(album)
## Pandas Install / Data Frames

I installed the Pandas library to my program for the following reasons:

- Easy to read data for the user, using lists
- Enhanced performance, reading data faster and more efficiently
- Multiple data frames and methods in an easy to read way

      import pandas as pd
      df = pd.DataFrame(records)

      def average_age():
          avg_age = df['Age'].mean()
          avg_age_rounded = round(avg_age)  # Round avg_age to the nearest whole number(intg)
          print(f"The average age of the fans is: {avg_age_rounded}")

## Floating Point Number to Integer Number
When asking for the average age of the fans, the original function displayed a a floating point number, with a decimal, for example: Average age 30.62. This wasn't the most readable for the end user. I added the following code to change the answer to a round number, which roudned the answer to the nearest whole number. For example: Average age 31.

    def average_age():
        avg_age = df['Age'].mean()
        avg_age_rounded = round(avg_age)  # Round avg_age to the nearest whole number(intg)
        print(f"The average age of the fans is: {avg_age_rounded}")

# Testing
To test the functionality of the program I used the following systems:

- pep8ci.herokuapp.com / Which checks for any errors in my python code
- Heroku / App deployment, testing the user experience

Testing included typing in the correct requirements for each question multiple times to show it provides the right data each time, but equally testing incorrect data entry, for example: using a number which was not listed. See image below, when answering the album list with '0' it returned an error message, which shows the code is working.

I also tried using incorrect formats such as string/words which displayed the correct error message also.

When testing on pep8, the errors returned were line character maximums and function spacing errors. This was updated and tested again.

<table>
  <thead>
    <tr>
      <th>Function Test</th>
      <th>Test Response</th>
      <th>Test Reaction/Fix</th>
     
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Google Sheet Connection</td>
      <td>After printing the data frames to the terminal the response returned 'Unable to locate file name taylorswift_erastour'</td>
      <td>Ensured the creds.json file was updated and the google sheet had authroised access to edit. (Adding the client email taylorswift-erastour@macro-virtue-429510-d5.iam.gserviceaccount.com)</td>
    </tr>
    <tr>
       <td>Question Number System</td>
       <td>After checking different numbers into the user input box, I can check the error messages displayed. When using numbers 1-6, the functions returned the answers correctly, but when using a number outside of this range, an error message returned. On one occasion, when entering '5' the function was not called, and data answers were produced and no error message were displayed.</td>
      <td>When checking the function for question 5, it was the 'favourite song' function, when going back into the code i realised there had been some spacing issues which resulted in the function not being called. Once this was fixed, i ran the test of question 5 again, where it displayed the favourite song.</td>
    </tr>
    <tr>
      <td>Deployment Tests</td>
      <td>When deploying the code to the app platform heroku, it kept providing an error message of not locating the creds.json file, or gspread.</td>
      <td>I went in and tested each option, checking the creds.json file, the settings on heroku, and noticed the additional config var was not added, and the programs and code libraries were not all installed. Once installed, and config var was added, the file was called without issue.</td>
    </tr>
    <tr>
    <td>Testing User Messaging</td>
    <td>When first writing my code and doing the first test, I noticed the text displayed to the user was in an incorrect order. This meant understanding where to put the user input was confusing.</td></td>
    <td>I adjusted the order of the print text and when they were called within my python code to amend the order the user read the text. I also added line breaks, to make it even clearer when using the while loop and getting the data answers.</td>
 
  </tbody>
</table>


![Testing](https://github.com/Brogandaisy/tayorswift_erastour/blob/main/assets/images/ts_app_display5.png)

# Bugs
Whilst working on my program, and with each new function, I was consistently checking for bugs and errors. The following errors appeared as I wrote:

- Indent errors, where code had been written with an incorrect indent, not allowing the code to be called/read
- Spacing errors between functions
- The wrong function name was displayed, not allowing the correct function to be called
- Error messages displaying disconnects to the 'gspread', 'google.oauth2.service_account' and 'Credentials' when deploying
- Average age displaying a decimal number

Whilst checking these at each stage of the project I was able to correct my errors as I worked, without losing track of each working function. I tested each function by using 'python3 run.py' and answering the question as the user. 

No bugs remain in the project, all functions working well.

# Validator Testing

PEP8 Test Returns Clear.


# Deployment
This project was deployed using Heroku. My code had been written using gitpod, and committed to github. I used the template repository from Code Institute.

I followed the steps below to create the app display on Heroku:

- Create new app, enter name and country
- Connect to Github account and choose the correct repository
- Select auto deployments, or choose to manually pull (auto ensures it pulls your most up to date commits from github)
- Go to settings and adjust the following:
- Add in your creds.json file as a config var, copy and paste from gitpod, and enter in the box (As this file is hidden from your public github repository)
- Add in the additional config var, (port/8000)
- Install the following buildpacks:
- python and nodejs (ensure they are downloaded in this order)

Once you have this connected, and you have commited your latest edits to github, press 'Open App' at the top of the page and it will display your running program. Here you can test further the user experience.
![Heroku App Deployment](https://github.com/Brogandaisy/tayorswift_erastour/blob/main/assets/images/ts_heroku.png)

# References
I used the following resources to complete this project.

- W3Schools for pandas library explanation, and how to include an enumerate function
- Love Sandwiches walk through project for deployment, and googlesheet import/connection

Author - Brogan Carpenter



  
  
    
  




