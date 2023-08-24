#Created a string's containing a sentence with repeated words.
u = "yashu had been saying that he had been there"
v = "she been saying that her name is yashu"
w = "he had had he"

#Implement a function to count the occurrences of a specific word in the sentence.
print('Number of occurrence of had :', u.count('had'))
print('Number of occurrence of had :', v.count('yashu'))
print('Number of occurrence of had :', w.count('he'))

#Write a program to replace a chosen word in the sentence with another word.
u = "yashu had been saying that he had been there"
u1="he"
u2="she"

x = u.replace(u1, u2)
print(x)

print("Original String :", u)
print("Modified String :", x)
