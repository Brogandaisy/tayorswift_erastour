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

![Google Sheet Data](https://github.com/Brogandaisy/tayorswift_erastour/blob/main/assets/images/ts.googlesheet.png)

With the data collected in a google sheet, I used the following python code to create a program for users to quickly get select types of data fast from the survey. 
Including:

- Average age of fans attending
- Gender breakdown of fans attending
- Most visited country fans are attending from
- Most requested favourite album
- Most requested favourite song

I then also included the following data about the fans depending on their favourite album. For example, if you wanted to know the average age and most common gender of fans whose favourite album is 'Red'.



# Features

Within the python code, I included a range of features to allow the data to be pulled quickly, efficiently and accurately. 

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

For question 6, it is a little different. As I wanted the user to be asked a second question so they can select their chosen album using the number system. Instead of allowing the user to input the album as a string, which could allow mistakes to be made (spelling, capitalization errors, or an album not listed in the survey). Using a list and number system allowed the user to get the correct data for their chosen album.

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

# Bugs
Whilst working on my program, and with each new function, I was consistently checking for bugs and errors. The following errors appeared as I wrote:

- Indent errors, where code had been written with an incorrect indent, not allowing the code to be called/read
- Spacing errors between functions
- The wrong function name was displayed, not allowing the correct function to be called
- Error messages displaying disconnects to the 'gspread', 'google.oauth2.service_account' and 'Credentials' when deploying
- Average age displaying a decimal number

Whilst checking these at each stage of the project I was able to correct my errors as I worked, without losing track of each working function. I tested each function by using 'python3 run.py' and answering the question as the user. 

No bugs remain in the project, all functions working well.

# Deployment

# References
I used the following resources to complete this project.

- W3Schools for pandas library explanation, and how to include an enumerate function
- Love Sandwiches walk through project for deployment, and googlesheet import/connection

Author - Brogan Carpenter



  
  
    
  




