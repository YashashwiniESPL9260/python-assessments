'''Exercise: Working with Dictionaries
- Create a dictionary with student names as keys and their corresponding marks as values.
- Implement a function that finds the student with the highest marks and prints their name and score.
- Add a new student to the dictionary and update their marks.'''


# creating a dictionary
student1 = {
  "name": "yashu",
  "age": "23",
  "test": [75]
}
student2 = {
  "name": "teju",
  "age": "26",
  "test": [85]
}
student3 = {
  "name": "pushu",
  "age": "18",
  "test": [35]
}
def ranker(test):
  for i in students:
    if (test >= 85):
      print(i[ "name" ])
      print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
      print("highest marks of %s is : %s " % (i[ "name" ],
                                              ranker(i)))
    else:
      print("no one scored hightest marks")



