''' #dictionaries
#A dictionary is used to store data in key : value pairs.

student = {
    "name": "vidhyanjali",
    "age": 22,
    "course": "Mca"
}


#Characteristics (Rules)
#Keys must be unique
#Keys must be immutable (string, int, tuple)
#Values can be any datatype
#Dictionary is mutable (can change)

1. keys() Method

#Returns all keys from the dictionary.
 syntax: dict_name.keys()

 example:

student = {
    "name": "vidhyanjali",
    "age": 22,
    "course": "BTech"
}

print(student.keys())

2. values() Method
Returns all values from the dictionary.
syntax: dict_name.values()

example:

student = {
    "name": "vidhyanjali",
    "age": 22,
    "course": "BTech"


3. clear() Method 

Removes all items from the dictionary.
syntax: dict_name.clear()

example 

student = {
    "name": "vidhyanjali",
    "age": 22,
    "course": "BTech" 
}

student.clear()

print(student)

print(student.values())


4. get() (VERY IMPORTANT)

Safe way to access value

print(student.get("name"))     # vidhyanjali
print(student.get("marks"))    # None
print(student.get("marks", 0)) # 0




4th data type
Sets in Python {}
What is a Set?

A set is a collection of unique elements.
s = {1, 2, 3, 4}

No duplicates allowed
No order (unordered)
Mutable (can change)
Uses {}

s = {1, 2, 2, 3, 4}
print(s)   #duplicates removed

Set Operations (VERY IMPORTANT)



Union (|): this is used add or get 2 different sets without duplicated. 
a = {1, 2}
b = {2, 3}

print(a | b)
#check wheather user entered pin is write or wrong? '''
correct_pin = {"1234"}   # set

user_pin = input("Enter PIN: ")

if user_pin in correct_pin:
    print("Correct PIN ")
else:
    print("Wrong PIN ")


