#Created a string's containing a sentence with repeated words.
u = "yashu had been saying that he had been there"
v = "she been saying that her name is yashu"
w = "he had had he"

#Implement a function to count the occurrences of a specific word in the sentence.
def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if  word == 'the':
            if word in counts:
                counts[word] += 1
            else:
                counts[word] = 1

    return counts

print( word_count('the quick brown fox jumps over the lazy dog.'))


print( word_count('the quick brown fox jumps over the lazy dog.'))

#Write a program to replace a chosen word in the sentence with another word.
u = "yashu had been saying that he had been there"
u1="he"
u2="she"

x = u.replace(u1, u2)
print(x)

print("Original String :", u)
print("Modified String :", x)
