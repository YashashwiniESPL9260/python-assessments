import json

'''Exercise: JSON File Handling
- Create a JSON file with information about 10 books (title, author, publication year).
- Write a Python program to read the JSON file and print the details of each book.'''

#Created a JSON file with information about 10 books
books_data = [{"id":"001","language":"java","edition":"third","author":"Herbert Schildt"},\
              {"id":"002","language":"c++","edition":"second","author":"Herbert Schildt"},\
              {"id":"00388","language":"c","edition":"first","author":"Herbert Schildt"},\
              {"id":"004","language":"python","edition":"third","author":"Herbert Schildt"},\
              {"id":"005","language":"sql","edition":"third","author":"Herbert Schildt"},\
              {"id":"006","language":"oracal","edition":"third","author":"Herbert Schildt"},\
              {"id":"007","language":"git","edition":"third","author":"Herbert Schildt"},\
              {"id":"008","language":"aws","edition":"third","author":"Herbert Schildt"},\
              {"id":"009","language":"cloud computing","edition":"third","author":"Herbert Schildt"},\
              {"id":"010","language":"html","edition":"third","author":"Herbert Schildt"}]

#storing the above data into json file
with open("books_details.json", "w") as book:
   json.dump(books_data, book)

print("json creaated ...................................")

#reading a json file
with open('books_details.json', 'r')as book:
    files_content= book.read()
    print(files_content)

