#Name:                  Task 9.py
#Author:                Derek Baker
#Date Created:          24-02-2023
#Date Last Modified:    24-02-2023
#
#Purpose:
#
#The purpose of this program is to take the student's information and then prompt the student to enter in the course codes of the programs 
#they want to register for. The program will then display they information and courses they entered.

courses = []
#defining the list

class Program:
    def __init__(self, name, code):
        self.name = name
        self.code = code
#initializing the class

    def courseSelection():
        if 'PROG1234' in course:
            courses.append(program1.name + ' - ' + program1.code) 
        if 'INFO4321' in course:
            courses.append(program2.name + ' - ' + program2.code)
        if 'TECH9876' in course:
            courses.append(program3.name + ' - ' + program3.code)
        if 'PROG7685' in course:
            courses.append(program4.name + ' - ' + program4.code)
#creating a method to add the selected program details to a new list

program1 = Program('Programming 101', 'PROG1234')
program2 = Program('Computer Systems', 'INFO4321')
program3 = Program('Technology 102', 'TECH9876')
program4 = Program('Programming 545', 'PROG7685')
#defining the available courses as objects in the class

student = []
#defining a new list

firstName = input('Please enter your firstname: ').capitalize().strip()
student.append(firstName)
#asking for the user's first name and adding it to the list

lastName = input('Please enter your last name: ').capitalize().strip()
student.append(lastName)
#asking for last name and adding to list

studentNumber = int(input('Please enter your student number: '))
student.append(studentNumber)
#asking for student number and adding to list

print("\n{0:^20s}".format('Available Courses'))
print('{0:-^20s}'.format('-'))
print('{} - {}\n{} - {}\n{} - {}\n{} - {}\n'.format(program1.name, program1.code, program2.name, program2.code, program3.name, program3.code, program4.name, program4.code))
#printing the available courses to the user

course = input('Please enter the program codes you wish to register '
               'for (put a comma between each code): ').upper().strip().replace(' ', '')
#getting the user's input for the courses they want to register to 

while True:
    if course == '':
        course = input("You did not enter any courses. Would you like to exit the program?[yes/no]: ")
        if course == 'yes':
            exit()
            #will close the program if the user does not enter any input and if they type yes to exit
    elif 'PROG1234' or 'INFO4321' or 'TECH9876' or 'PROG7685' in course:
        break
    else:
        course = input('Please only enter available course codes: ').upper().replace(' ', '')
    #asking for the course codes from user and adding to a new list  
      
Program.courseSelection()
#running the method to create the new list

courseList = course.split(',')
#creating a new list with the info the user entered

path = "C:\Selected Courses.txt"
#creating a new path

file = open(path, 'a')
#opening the new file

file.write('{:<35} {} {}'.format('Student Name:', firstName, lastName))
file.write('\n{:<35} {}'.format('Student Number:', studentNumber))
file.write('\nTotal Number of Registered Courses: {0:d}'.format(len(courseList)))
file.write('\n{0:-^40}'.format('-'))
file.write('\nCourse registration has been confirmed for the following courses:\n')
for i in range(0, len(courses)):
    file.write("Course#{}: {}".format(i + 1, courses[i]))
    #writing the information into the file

print("\nThe selected courses have been saved to a file called 'Selected Courses.txt' with the path: " + path)
#telling the user that the information they entered is in the specified file
file.close()
#closing the file