# creating a dictionary
student1 = {
  "name": "yashu",
  "age": "23",
  "marks": [75, 75]
}
student2 = {
  "name": "teju",
  "age": "26",
  "marks": [50, 15]
}
student3 = {
  "name": "pushu",
  "age": "18",
  "marks": [35, 65]
}


# printing the dictionary
print(student1)
print(student2)
print(student3)


# Function calculates average
def calculate_total_average(students):
    marks = get_average(students["marks"])
    return marks
# Student list consisting the
# dictionary of all students
students = [student1,student2,student3]

# Calculate letter grade of each student
def assign_letter_grade(marks):
    if test >= 90:
        return "A"
    elif test >= 80:
        return "B"
    elif test >= 70:
        return "C"
    elif test >= 60:
        return "D"
    else:
        return "E"


for i in students:
    print(i[ "name" ])
    print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
    print("Average marks of %s is : %s " % (i[ "name" ],
                                            calculate_total_average(i)))

    print("Letter Grade of %s is : %s" % (i[ "name" ],
                                          assign_letter_grade(calculate_total_average(i))))

    print()

