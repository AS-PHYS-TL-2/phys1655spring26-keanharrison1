
print ("Hello, World!")

#-- Creating variables 
# Message is the VARIABLE. Every variable is connected to a VALUE.
# Variables = labels you assign values to. 
message = "Hello, World!"
print (message)

#--Strings: series of characters
my_names = "Kean " + "Thurman " + "Harrison"
print (my_names)

# Changing case of strings
# .title() makes all words upper case
# the dot (.) tells Python to make the title() method act on the variable name
name = "kean thurman harrison"
print (name.title()) 
# You can also change a name to all upper/lower case
print (name.upper())
print (name.lower())

# using variable's value inside string (using f-strings). F is for format.
# to insert variable's value into a string, place letter F before opening quotation marks
first_name = "Kean"
last_name = "Harrison"
full_name = f"{first_name} {last_name}"
print (full_name)

# completing messages using f-string
print (f"Hello, {first_name} {last_name}")

# using f-string to 1) compose message and 2) assign message to variable
message = (f"Hey, {first_name}! How are you?")
print (message)

# whitespace: non-printing characters; spaces, tabs, end-of-line symbols
# \t can be used to add a tab to your text
print ("Python")
print ("\tPython")

# to add a newline in a string, use \n
print ("Note to self: \nI\nLove\nLearning\n!")

# combining tab and newline
print ("Hello\n\tMy\n\tName\n\tIs\n\tKean!")

# eliminating whitespace on R & L sides of string using rstrip() method
favorite_language = 'python '
print (f"|{favorite_language}|")
print (f"|{favorite_language.rstrip()}|") # wrapped in delimiters to show spacing diff

# PERMANENTLY removing whitespace from <favorite_language> requires associated stripped value with variable name
favorite_language = favorite_language.rstrip()
print (f"|{favorite_language.rstrip()}|") # new value of favorite_language is "python", not "python "

# lstrip() --> stripping from left side
# rstrip() --> stripping from right side

fl = " python "
print (f"|{fl}|") # unstripped
print (f"|{fl.rstrip().lstrip()}|") #stripped L&R

# removing prefixes using removeprefix(), which leaves the original UNCHANGED
url = "https://nostarch.com"
print (url)
print (url.removeprefix("https://"))

# EXERCISES FOR THE NOTES ABOVE

# Save each of the following exercises as a separate file, with a name like name_cases.py. If you get stuck, take a break or see the suggestions in Appendix C.

# 2-3. Personal Message: Use a variable to represent a person’s name, and print a message to that person. Your message should be simple, such as, “Hello Eric, would you like to learn some Python today?”

# 2-4. Name Cases: Use a variable to represent a person’s name, and then print that person’s name in lowercase, uppercase, and title case.

# 2-5. Famous Quote: Find a quote from a famous person you admire. Print the quote and the name of its author. Your output should look something like the following, including the quotation marks:

# 2-6. Famous Quote 2: Repeat Exercise 2-5, but this time, represent the famous person’s name using a variable called famous_person. Then compose your message and represent it with a new variable called message. Print your message.

# 2-7. Stripping Names: Use a variable to represent a person’s name, and include some whitespace characters at the beginning and end of the name. Make sure you use each character combination, "\t" and "\n", at least once.
# Print the name once, so the whitespace around the name is displayed. Then print the name using each of the three stripping functions, lstrip(), rstrip(), and strip().

# 2-8. File Extensions: Python has a removesuffix() method that works exactly like removeprefix(). Assign the value 'python_notes.txt' to a variable called filename. Then use the removesuffix() method to display the filename without the file extension, like some file browsers do.



# Integers 
print (2 + 4)
print (2 * 4)
print (2 / 4)
print (2 - 4)

# Python uses order of ops
print (2 + 3 * 4)
print (2 / 6 * 2 + 1 - 5)

# Floats - any number with a decimal point
print (0.1 + 0.1)

# When you divide two numbers, even if they're integers that result in a whole number, you'll ALWAYS get a float
print (4 / 2)

# underscores in numbers - when writing long numbers, group digits using underscores for readability
universe_age = 14_000_000_000
print (universe_age)

# multiple assignment
x, y, z = 1, 2, 3
print (x, y, z)

# constants: variable whose value stays the same throughout the life of a program
# Python programmers use all caps to indicate this. Python doesn't have built-in constant types
MAX_OUTPUT = 5000

# EXERCISES FOR THE ABOVE NOTES

# 2-9. Number Eight: Write addition, subtraction, multiplication, and division operations that each result in the number 8. Be sure to enclose your operations in print() calls to see the results. You should create four lines that look like this:
# print(5+3)
# Your output should be four lines, with the number 8 appearing once on each line.

# 2-10. Favorite Number: Use a variable to represent your favorite number. Then, using that variable, create a message that reveals your favorite number. Print that message.


# Python community's philosophy is contained in the "Zen of Python" by Tim Peters
# Book is basically a brief set of principles for writing good Python, accessible by using:
import this
