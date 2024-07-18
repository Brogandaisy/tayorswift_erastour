# Taylor Swift Eras Tour Survey Data
Project 3 - Brogan Carpenter

[View Live Project](https://brogandaisy.github.io/Plant-Water-Fire/)

# About the Project

This project is analysing the data found in a survey created for fans who attended one of the Eras Tour shows by Taylor Swift. The survey asked 150 fans the following questions:

- Name
- Age
- Gender
- Country
- Favourite Taylor Swift Song
- Favourite Taylor Swift Album

With this data collected, I used the following python code to create a program for users to quickly get select types of data fast from the survey. 
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

For question 6, it is a little different. As I wanted the user to be asked a second question so they can select their chosen album. Instead of allowing the user to input the album as a string, which could allow mistakes to be made (spelling, c




