'''Write a Python program to read a paragraph and count the number of vowels, consonants, and spaces using for loops.
Print the length of the paragraph and display the counts of vowels, consonants, and spaces separately. 




paragraph = ""Technology is changing the world rapidly.
It makes our daily tasks easier and faster.
People can communicate from anywhere in seconds.
Learning new technologies is important for the future.
We should use technology wisely for a better life.""

count_spaces = 0
count_vowels = 0
count_consonants = 0

#spaces
for ch in paragraph:
    if ch == " ":
        count_spaces += 1

#vowels
for ch in paragraph:
    if ch in "aeiouAEIOU":
        count_vowels += 1

#consonants
for ch in paragraph:
    if ch.isalpha() and ch not in "aeiouAEIOU":
y        count_consonants += 1


print("Length of paragraph is:", len(paragraph))
print("Number of spaces:", count_spaces)
print("Number of vowels:", count_vowels)
print("Number of consonants:", count_consonants) 



#A for loop is used for iterating over a sequence(that is either a list,a tuple, a dictonary,a set of a string).
a=9
print(b)
for j in range(1,10):
    print(j)  # it will be error becacuse there is a difference between initial variable and normal variable
    
#now
a=9
for j in range(1,100):
    print(j)

#range() ---> this is used to generate number
#syntax---> range(start,end,step)

for j in range (0,30,2):  #we have to give "j" to move two positions okay
    print(j)

any = "abc"
print(list(any))
print(tuple(any))

any = "123"
print(int(any))
print(list(any))
print(tuple(any))

so = 123
print(str(so))

rev_str = "vidhyanjali"
empty_= ""
for j in rev_str:
    empty_= j + empty_
    print(empty_)    '''

name= "madam"
rev = ""

for j in name:
    rev = j + rev

if  name == rev:
    print("palindrome")
else:
    print("not palindrome")
    




