# ============================================
# PYTHON STRINGS - COMPLETE GUIDE WITH EXAMPLES
# ============================================

# 🔹 1. Strings Basics
# Strings can be created using single (' ') or double (" ") quotes

a = 'hello'
b = "hello"

print(a == b)  # True → both are same


# 🔹 2. Indexing & Slicing
# Strings are sequences → index starts from 0

text = "Hello world"

# Indexing
print(text[0])   # H
print(text[6])   # w

# Slicing → [start : end]
print(text[6:9])   # wor

# Negative indexing (from end)
print(text[-1])   # d
print(text[-5:-1])  # worl


# 🔹 3. Another Slicing Example
name = "Vidhyanjali"

print(name[5:10])  # anjal


# 🔹 4. Strings are Immutable
# You cannot change original string directly

lang = "python programming"

# replace() creates a NEW string
new_lang = lang.replace("python", "java")

print(new_lang)  # java programming
print(lang)      # original remains same


# 🔹 5. Advanced Slicing
day = "Iam vidhyanjali from Rajamundry, Iam a Masters student"

# Extract name
print(day[4:16])

# Reverse string
print(day[::-1])

# Skip characters
print(day[::2])   # every 2nd char
print(day[::3])   # every 3rd char

# Length of string
print(len(day))


# 🔹 6. split() Method
# Converts string → list

sentence = "python is a programming language"

print(sentence.split(" "))  
# ['python', 'is', 'a', 'programming', 'language']

# Split by word
print(sentence.split("programming"))
# ['python is a ', ' language']


# 🔹 7. lower() and upper()

print(sentence.lower())  # all lowercase
print(sentence.upper())  # all uppercase


# 🔹 8. Checking substring

if "A" in sentence:
    print("Yes, it is there")
else:
    print("No, it is not there")  
# Output → No (case-sensitive)


# 🔹 9. replace() Method

text2 = "I like python"

updated_text = text2.replace("python", "java")

print(updated_text)  # I like java


# 🔹 10. Extra Useful String Operations

# Concatenation
first = "Hello"
second = "World"
print(first + " " + second)

# Repetition
print("Hi " * 3)

# Membership
print("python" in sentence)   # True
print("java" in sentence)     # False


# 🔹 11. Formatting Strings (f-strings)

name = "Vidhyanjali"
place = "Rajamundry"

print(f"My name is {name} and I am from {place}")


# ============================================
# END OF SCRIPT
# ============================================

# 💡 Summary:
# - Strings are immutable
# - Index starts from 0
# - Use slicing to extract data
# - Common methods:
#   split(), replace(), lower(), upper()
# ============================================
