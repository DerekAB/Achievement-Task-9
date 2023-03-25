#Name:                  Task 9.py
#Author:                Derek Baker
#Date Created:          24-02-2023
#Date Last Modified:    24-02-2023
#
#Purpose:
#
#The purpose of this program is to take the student's information and then prompt the student to enter in the course codes of the programs 
#they want to register for. The program will then display they information and courses they entered.

class Program:
    def __init__(self, name, code):
        self.name = name
        self.code = code

program1 = Program('Programming 101', 'PROG1234')
program2 = Program('Computer Systems', 'INFO4321')
program3 = Program('Technoloy 102', 'TECH9876')
program4 = Program('Programming 545', 'PROG7685')

student = []

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

course = input('Please enter the program codes you wish to register '
               'for (put a comma between each code): ').upper().strip().replace(' ', '')

while True:
    if course == '':
        course = input("You did not enter any courses. Would you like to exit the program?[yes/no]: ")
        if course == 'yes':
            exit()
    elif not(course == 'PROG1234' or course == 'INFO4321' or course == 'TECH9876' or course == 'PROG7685'):
        course = input('Please only enter available course codes: ').upper().replace(' ', '')
    else:
        break
        

courseList = course.split(',') #splitting string into list

#asking for the course codes from user and adding to a new list



print('') #adding blank space

print('Student Information: \n')

print(*student, sep='\n') #printing student information

print('') #blank space

print('Registered Courses: \n')

for i in courseList:
    print(i)
#printing course list