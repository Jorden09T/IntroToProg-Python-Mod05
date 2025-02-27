# ------------------------------------------------------------------------------------------ #
# Title: Assignment03
# Desc: This assignment demonstrates using conditional logic and looping
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   <Jorden Thomas>,<2.26.25>, <Assignment05.py>
# ------------------------------------------------------------------------------------------ #
import json

# Define the Data Constants
MENU: str = """
---- Course Registration Program ---
Select from the following Menu:
1. Register a student for a Course
2. Show current data
3. Save data to a file
4. Exit the program
------------------------------------
"""
FILE_NAME: str = 'Enrollments.csv'

# Define the Data Variables
student_first_name: str = ''
student_last_name: str = ''
course_name: str = ''
student_data: dict = {}
students: list = []
csv_data: str = ''
file = None
menu_choice: str

try:
    file = open(FILE_NAME, 'r')
    #print(type(file))
    #for row in file.readlines():
    #    student_data = row.split(',')
    #    student_data = [student_data[0], student_data[1], student_data[2].strip()]
    #    students.append(student_data)

    #json Answer
    students = json.load(file)
    file.close()

except Exception as e:
    print("Error: There was a problem with the file.")
    print("Please check that the file exists and is also in json format.")
    print("------Error--Message --------")
    print(e.__doc__)
    print(e.__str__())
finally:
    if type(file) == "<class '_io.TextIOWrapper'>":
        if file.closed == False:
            file.close()

# Present and Process the data
while True:
    # Present the menu of choices
    print(MENU)
    menu_choice: str = input('Please Select from the following menu (1, 2, 3, or 4): ')

    # Input user data
    if menu_choice == '1':
        try:
            student_first_name = input("What is the Student's first name? ")
            if not student_first_name.isalpha():
                raise ValueError('First name should only have alphabetic characters!')
            student_last_name = input("What is the Student's last name? ")
            if not student_last_name.isalpha():
                raise ValueError('First name should only have alphabetic characters!')
            course_name = input("What is the name of the course? ")
            student_data = {"FirstName": student_first_name,
                            "LastName": student_last_name,
                            "CourseName": course_name}
            students.append(student_data)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}")
        except ValueError as e:
            print(e)
            print("---Error--Message---")
            print(e.__doc__)
            print(e.__str__())
        except Exception as e:
            print("Error: Input error, please check the data your have entered.")
            print("---Error-Message---")
            print(e.__doc__)
            print(e.__str__())
        continue
    # Present the current data
    elif menu_choice == '2':
        print("-"*50)
        for student in students:
            print(f'Student {student["FirstName"]}'
                  f' {student["LastName"]} is enrolled in {student["CourseName"]}')
        print("-"*50)
        continue

        # Save the data to a file
    elif menu_choice == '3':
        try:
            file = open(FILE_NAME, 'w')
            json.dump(students, file)

            file.close()
            print("loading...")
            for student in students:
                print("Complete: ")
                print(f'Student {student["FirstName"]}'
                      f' {student["LastName"]} is enrolled in {student["CourseName"]}')
        except Exception as e:
            if file.closed() == False:
                file.close()
            print("Error: Problem with writing the file.")
            print("Please check the file and make sure it is not opened in another program!")
            print("---Error-Message---")
            print(e.__doc__)
            print(e.__str__())
        continue

        # Stop the loop
    elif menu_choice == '4':
        print("Good bye!")
        exit()

    else:
        print("Please select 1, 2, 3, or 4!")


