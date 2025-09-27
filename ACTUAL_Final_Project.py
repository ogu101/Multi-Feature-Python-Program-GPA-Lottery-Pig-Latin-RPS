# FINAL PROJECT
import random

# Program Menu
program_menu = ("Welcome to the final project.\n"
                "Enter 1 to calculate GPA\n"
                "Enter 2 for Lottery Number Generator\n"
                "Enter 3 for Pig Latin\n"
                "Enter 4 for Rock, Paper, Scissors\n"
                "Enter 9 to exit the program")

# Function 'get_user_menu_choice' - Gets the user's menu choice
def get_user_menu_choice():
    user_menu_choice = input("Enter menu option: 1, 2, 3, 4, or 9 to exit:")
    valid_menu_inputs = ["1", "2", "3", "4", "9"]
    while user_menu_choice not in valid_menu_inputs:
        user_menu_choice = input(f"Invalid input. Enter menu option 1, 2, 3, 4, or 9 to exit:")
    return user_menu_choice

# Program Choices

# Program 1: Calculate Student GPA
class Course:
    # Function '__init__' - Initializes "Course" Class
    def __init__(self, course_name, credit_hours, letter_grade):
        self.course_name = course_name
        self.credit_hours = credit_hours
        self.letter_grade = letter_grade
    # Function '__str__' - Formats "Course" Class output
    def __str__(self):
        return f'{self.course_name}, {self.credit_hours} credits, Grade: {self.letter_grade}'

class Student:
    # Function '__init__' - Initializes "Student" Class
    def __init__(self, full_name, email, major, project_info):
        self.full_name = full_name
        self.email = email
        self.major = major
        self.project_info = project_info
        self.courses = []
        self.letter_grade_to_gpa_dictionary = {'A+': 4.0, 'A': 4.0, 'A-': 3.7, 'B+': 3.3,
                                               'B': 3.0, 'B-': 2.7, 'C+': 2.3, 'C': 2.0,
                                               'C-': 1.7, 'D+': 1.3, 'D': 1.0}
    # Function 'add_course' - Adds course to "Student" object "courses" attribute; "courses" = list type
    def add_course(self, course):
        return self.courses.append(course)
    # Function 'letter_grade_to_gpa' - Converts "Student" object letter grade to corresponding gpa
    def letter_grade_to_gpa(self, letter_grade):
        self.letter_grade = letter_grade
        course_gpa = 0
        for dict_letter_grade, dict_GPA in self.letter_grade_to_gpa_dictionary.items():
            if letter_grade == dict_letter_grade:
                course_gpa = dict_GPA
        return course_gpa
    # Function 'print_student_gpa' - Prints the output
    def print_student_gpa(self, overall_gpa):
        self.overall_gpa = overall_gpa
        print()
        print(f'{self.full_name}, {self.email}, {self.major}, {self.project_info}')
        print()
        print(f'COURSES:')
        for iteration in range(len(self.courses)):
            print(f'{self.courses[iteration]}')
        print()
        print(f'FINAL GPA: {self.overall_gpa:.2f}')

    def calculate_gpa(self):
        total_quality_points = 0
        total_credit_hours = 0

        for i in range(len(self.courses)):
            letter_grade = self.courses[i].letter_grade
            course_gpa = self.letter_grade_to_gpa(letter_grade)
            credit_hours = self.courses[i].credit_hours
            quality_points = course_gpa * credit_hours

            total_quality_points += quality_points
            total_credit_hours += credit_hours

        overall_gpa = total_quality_points / total_credit_hours

        return overall_gpa


# Function 'calculate_student_gpa' - Calculates and outputs student gpa & info from  student info input and course info input
def calculate_student_gpa():
    # Creates a 'my_student'object in the Student class with user input
    student_info = input("Enter full name, email, major, & project information (Separated by commas):")
    student_info_list = student_info.split(",")
    my_student = Student(student_info_list[0], student_info_list[1], student_info_list[2], student_info_list[3])

    # Gets and validates number_of_courses
    number_of_courses = input("How many courses do you want to add (2-6):")
    valid_number_of_courses = ["2", "3", "4", "5", "6"]
    while number_of_courses not in valid_number_of_courses:
        number_of_courses = input("Invalid input. How many courses do you want to add (2-6):")
    number_of_courses = int(number_of_courses)

    # Creates a course object for each user inputted course + Stores the created course objects in my_student.courses
    for iteration in range(number_of_courses):
        # Get Course Information
        course_info = input("Enter course name, credit hours, and letter grade (Separated by commas):")
        course_info_list = course_info.split(",")
        course_name = course_info_list[0]
        credit_hours = float(course_info_list[1])
        letter_grade = course_info_list[2]
        course = Course(course_name, credit_hours, letter_grade)
        my_student.add_course(course)

    # Calculates Course GPA + Displays Output
    overall_gpa = my_student.calculate_gpa()

    my_student.print_student_gpa(overall_gpa)


# Program 2: Lottery Number Generator

# Function 'lottery_number_generator' - Performs lottery generator program
def lottery_number_generator():
    lottery_number = []

    # Creates a lottery number (list type) with non-repeating number values
    for iteration in range(5):
        lottery_number_value = random.randint(1, 69)
        while lottery_number_value in lottery_number:
            lottery_number_value = random.randint(1, 69)
        lottery_number.append(lottery_number_value)
    lottery_number_last_value = random.randint(1, 26)
    lottery_number.append(lottery_number_last_value)
    lottery_number.sort()

    # Prints the lottery number
    print(f'Your Powerball Numbers:', end=" ")
    for iteration in range(len(lottery_number)):
        print(lottery_number[iteration], end=" ")
    print()


# Program 3: Pig Latin

# Function 'pig_latin' - Performs pig latin program
def pig_latin():
    user_sentence = (input("Enter sentence to be converted into Pig Latin:")).upper()
    user_sentence_list = user_sentence.split()
    converted_sentence = ""

    # Converts each word in user_sentence_list to pig latin and stores it in converted_sentence
    for word in user_sentence_list:
        first_letter = word[0]
        converted_word = word[1:] + first_letter + "AY"
        converted_sentence += converted_word + " "
    print(converted_sentence)

# Program 4: Rock, Paper, Scissors Game

# Computer Choice v User Choice Comparison

# Function 'get_computer_choice' - Relates the randomly generated computer_number to a rock, paper, scissors value
def get_computer_choice():
    computer_number = random.randint(1, 3)
    computer_number_dictionary = {1: "Rock", 2: "Paper", 3: "Scissors"}
    computer_choice = ""

    # Relates the random number to rock, paper, scissors value
    for computer_number_dictionary_keys, computer_number_dictionary_values in computer_number_dictionary.items():
        if computer_number == computer_number_dictionary_keys:
            computer_choice = computer_number_dictionary_values
    return computer_choice

# Function 'get_user_choice' - Retrieves the value of user_choice from the user and validates it
def get_user_choice():
    user_choice = (input("Enter a choice (rock, paper, or scissors):")).lower()
    user_possible_choice_list = ["rock", "paper", "scissors"]
    # Input validation for user_choice
    while user_choice not in user_possible_choice_list:
        user_choice = (input("Invalid input. Enter a choice (rock, paper, or scissors):")).lower()
    return user_choice

# Function 'determine_winner_and_circumstance' - Compares  computer_choice and user_choice to return  winner and circumstance outcome
def determine_winner_and_circumstance(computer_choice, user_choice):
    if computer_choice == "Rock":
        if user_choice == "paper":
            winner = "Player wins."
            circumstance = "winner"
        elif user_choice == "scissors":
            winner = "Computer wins."
            circumstance = "winner"
        else:
            winner = "It's a tie.You both chose the same rock."
            circumstance = "tie"

    elif computer_choice == "Paper":
        if user_choice == "rock":
            winner = "Computer wins."
            circumstance = "winner"
        elif user_choice == "scissors":
            winner = "Player wins."
            circumstance = "winner"
        else:
            winner = "It's a tie. You both chose the same paper."
            circumstance = "tie"

    else:
        if user_choice == "paper":
            winner = "Computer wins."
            circumstance = "winner"
        elif user_choice == "rock":
            winner = "Player wins."
            circumstance = "winner"
        else:
            winner = "It's a tie. You both chose the same scissors."
            circumstance = "winner"

    return [winner, circumstance]


# Function 'rock_paper_scissors_game' - Performs the rock, paper, scissors, game, program
def rock_paper_scissors_game():
    # Computer Choice
    computer_choice = get_computer_choice()

    # User Choice
    user_choice = get_user_choice()

    # Computer Object v User Object Comparison
    winner, circumstance = determine_winner_and_circumstance(computer_choice, user_choice)
    while circumstance == "tie":
        print(winner)
        computer_choice = get_computer_choice()
        user_choice = get_user_choice()
        winner, circumstance = determine_winner_and_circumstance(computer_choice, user_choice)

    # Print Output
    print(f'{winner}\n'
          f'Players Choice: {user_choice}\n'
          f'Computers Choice: {computer_choice.lower()}')

# Function 'main' - Main body of code + utilized for loop mechanism
def main():
    print(program_menu)
    user_menu_choice = get_user_menu_choice()
    separator = "------------------------------------------"

    # Runs calculate student GPA program
    while user_menu_choice == 1:
        calculate_student_gpa()
        # Program loop
        print(separator)
        print(program_menu)
        user_menu_choice = get_user_menu_choice()

    # Runs lottery number generator program
    while user_menu_choice == 2:
        lottery_number_generator()
        # Program loop
        print(separator)
        print(program_menu)
        user_menu_choice = get_user_menu_choice()

    # Runs pig latin program
    while user_menu_choice == 3:
        pig_latin()
        # Program loop
        print(separator)
        print(program_menu)
        user_menu_choice = get_user_menu_choice()

    # Runs rock, paper, scissors game program
    while user_menu_choice == 4:
        rock_paper_scissors_game()
        # Program loop
        print(separator)
        print(program_menu)
        user_menu_choice = get_user_menu_choice()

    # Exits the program
    while user_menu_choice == 9:
        print("You selected option 9. Exiting the program. Good-bye.")
        exit()


if __name__ == "__main__":
    main()