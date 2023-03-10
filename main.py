# Create a list of 5 students, print, add a new student and print the 3rd student

names_of_students = ['jadon', 'fred', 'martinez', 'christine', 'monica']
print(names_of_students)
names_of_students.append('alberta')
print(names_of_students)
third_student = names_of_students[2]
print(third_student)

# A dictionary containing a list of joel's information

joels_info = {
    'name': 'joel',
    'age': 13,
    'hobbies': {
        'outdoor': ['roaming', 'shouting'], 'indoor': ['teletabies', 'ludu']
    }

}

hobbies = joels_info['hobbies']
print(f'My hobbies are {hobbies}')

outdoor = hobbies['outdoor']
print(f'Outdoor hobbies are {outdoor}')

# Building from an empty dictionary, deleting an item from a dictionary

students_grade = {}
students_grade['mike'] = 'A'
students_grade['aaron'] = 'B'
students_grade['berto'] = 'C'
students_grade['jadon'] = 'D'
print(students_grade)
del students_grade['aaron']
print(students_grade)

# user input
prompt = 'What is your age?: \n'

age = input(prompt)
print(f'Your age is {age}')