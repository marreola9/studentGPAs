# Author: Maria Arreola
# File name:studentGPAs.py
""" Description: This application accepts the first name, last name, 
and GPA of students and will determine if they qualify for the Dean's 
list or the Honor Roll."""

while True:
    last_name = input("Enter the student's last name (type ZZZ to quit): ")
    if last_name == 'ZZZ':
        break
        
    first_name = input("Enter the student's first name: ")
    gpa = float(input("Enter the student's GPA: "))
    
    if gpa >= 3.5:
        print(f"{first_name} {last_name} has made the Dean's List.")
    elif gpa >= 3.25:
        print(f"{first_name} {last_name} has made the Honor Roll.")
    else:
        print(f"{first_name} {last_name} has not qualified for either the Dean's List or the Honor Roll.")
