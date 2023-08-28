'''Exercise: File Handling
- Write a program that reads a text file and prints the content to the console.'''

with open(r"C:\Users\espl9260\Desktop\sample.txt","r")as f:
    text_file_contents = f.read()
    print(text_file_contents)
