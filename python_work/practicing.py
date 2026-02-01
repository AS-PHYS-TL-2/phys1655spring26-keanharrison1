
# Sunday, Jan 18 ---------------------------------------------------------------------------------------------------

# Create a variable called name with your full name,
# then print it in lowercase, uppercase, and title case (three separate print() calls)
print ("------------------------------")

name = "kean harrison" 
print (name.lower())
print (name.upper())
print (name.title())

# Create two variables, first_name and last_name, then use an f-string to print:
# Hello, <first_name> <last_name>!
print ("------------------------------")

fn = "kean"
ln = "harrison"
print (f"Hello, {fn} {ln}! How are you today?")

# Create a variable with your name that includes whitespace on both sides (use spaces, \t, or \n), 
# then print it once raw and once using strip().
print ("------------------------------")

name = " Kean "
print (f"|{name}|")
print (f"|{name.strip()}|")

# Create a string that uses both \n and \t to print your name in a stacked, indented format.
print ("------------------------------")

print (name)
print (f" \n\t{name} \n\t{name} \n\t{name} \n\t{name} \n\t{name}")

# Assign "https://uva.edu" to a variable and print only uva.edu using removeprefix().
print ("------------------------------")

website = "https://uva.edu"
print (website.removeprefix("https://"))

# Assign "notes_week1.py" to a variable and print the filename without the .py extension using removesuffix().
print ("------------------------------")

file_name = "notes_week1.py"
print (file_name.removesuffix(".py"))

# Use multiple assignment to assign three integers to three variables, then print their sum.
print ("------------------------------")

a, b, c = 4, 5, 6
sum = int(a + b + c)
print (sum)

# Write four different math operations (using +, -, *, /) that each evaluate to 10, 
# and print each result on its own line.
print ("------------------------------")

a = int(1 + 9)
b = int(11 - 1)
c = int(10 / 1)
d = int(10 * 1)
e = int(3.2 ** 2)
print (a,b,c,d,e)

# Store a large number using underscores, then print it inside a short f-string sentence.
print ("------------------------------")

num = 40_000_000_000
print (f"Fuck everyone who don't got {num} in dey bank!")

# Create a constant (ALL CAPS) representing a fixed limit (e.g., max users or max output), 
# then print a sentence explaining what it represents using an f-string.
print ("------------------------------")

FIXED_LIMIT = 10_000
print (f"The maximum number of people allowed in Disney Land is {FIXED_LIMIT}")

# Create a list of usernames. Loop through it and print "ADMIN" in all caps if the username is "admin", 
# otherwise print the username in title case.
print ("------------------------------")

usernames = ["bob1", "lisa2", "todd3", "admin"]
for username in usernames:
    if username == "admin":
        print ("ADMIN")
    else:
        print (username.title())


# Store a variable password. 
# Use an if statement to print "Access granted" only if the password equals "python123".
print ("------------------------------")

password = "python000"
if password == "python123":
    print ("Access granted")
else: 
    print ("Try again")

# Create a variable drink. Use != to print a warning message only if the drink is not "water".
print ("------------------------------")

drink = "red bull vodka"
if drink != "water":
    print ("Not water!")

# Create two numbers. Use and to print "Both passed" only if both numbers are greater than 60.
print ("------------------------------")

num1 = 45
num2 = 69

if num1 > 60 and num2 > 60:
    print ("Both passed")
elif num1 > 60 or num2 > 60:
    print ("At least one passed")
else: 
    print ("None passed")

# Create two numbers. Use or to print "At least one passed" only if either number is greater than 60.
print ("------------------------------")

if num1 > 60 or num2 > 60:
    print ("At least one passed")

# Make a list of banned words. Check if a given word is in the list; print "Blocked" if it is.
print ("------------------------------")

words = ["fuck", "shit", "bitch", "motherfucker"]
variable = "fuck"
if variable in words:
    print ("Blocked")

# Make a list of guests. If "Kean" is not in the list, print "Invite Kean".
print ("------------------------------")

guests = ["McCoy", "Diego", "Phil"]
my_name = "Kean" 
if my_name not in guests: 
    print ("Invite Kean")

# Write an if-elif-else chain that assigns a ticket price based on age (child, student, adult).
print ("------------------------------")

age = 50
if age < 18: 
    print ("Child: $20")
elif age >= 18 and age < 22:
    print ("Student: $50")
else:
    print ("Adult: $75") 

# Create a list of tasks. If the list is empty, print "No tasks today"; otherwise, 
# loop through the list and print each task.
print ("------------------------------")

tasks = ["clean", "shop", "make calls"]
for task in tasks: 
    print (tasks)

# Create a list of numbers. Loop through it and print only the numbers that are greater than 10.
print ("------------------------------")

nums = [11, 12, 88, 3, 7, 90, 6, 4, 10]
for num in nums: 
    if num >= 10:
        print (num)


# Monday, Jan 19 ---------------------------------------------------------------------------------------------------

# Create a variable called message with the value "Hello, World!", then print it.
print ("------------------------------")

full_name = " kEaN HarrisoN "
print (f"Hello, {full_name.title().strip()}!")

# Print only results.DATA (no spaces, no .txt) using string methods—no hard-coding.
print ("------------------------------")


filename = "    results.DATA.txt.  "
print (filename.strip().removesuffix(".txt.")) 

# Create two variables a and b. Print which one is larger, 
# or print "Equal" if they’re the same—use an if / elif / else chain.
print ("------------------------------")

a = 11
b = 11
if a > b: 
    print ("a")
elif b > a: 
    print ("b")
else:
    print ("equal")        

# Given a list of numbers, loop through it and print only the even numbers that are greater than 10.
print ("------------------------------")

nums = [2, 40, 56, 8, 99, 2, 14, 61, 1, 0, 20]
for num in nums: 
    if num > 10 and num % 2 == 0:
        print (num)

# Given a list of usernames, 
# print "Duplicate" if the same name appears more than once; otherwise print "All unique".
print ("------------------------------")

usernames = ["kean", "bob", "jack", "selena", "bob", "rachel"]
unique_names = set(usernames)

if len(usernames) == len(unique_names): 
    print ("All unique")
else: 
    print ("Duplicates")

# Given a list of numbers, print the first number greater than 50, 
# then stop the loop immediately once it’s found
print ("------------------------------")

nums = [2, 40, 56, 8, 99, 2, 14, 61, 1, 0, 20]

for num in nums: 
    if num > 50:
        print (num) 
        break

# Loop through a list of numbers and count how many are greater than 10, then print the count.
print ("------------------------------")

nums = [2, 40, 56, 8, 99, 2, 14, 61, 1, 0, 20]

count = 0
for num in nums: 
    if num > 10:
        count += 1
print (count)

# Given a list of strings, print only the strings longer than 5 characters, in title case.
print ("------------------------------")

strings = ["hello", "ciao", "bonjour", "ola" ,"hi", "what's up"]

for string in strings:
    if len(string) > 5:
        print (string.title())

# Given a list of numbers, create a new list that contains only the numbers greater than 10, 
# then print that new list.
print ("------------------------------")

nums1 = range(1, 50)
nums2 = []

for num1 in nums1: 
    if num1 > 10: 
        (nums2.append(num1)) 
print (nums2)

# From nums1 = range(1, 50), create a new list that contains only even numbers greater than 10, then print it.
print ("------------------------------")

nums1 = range(1, 50)
nums3 = []

for num1 in nums1:
    if num1 > 10 and num1 % 2 == 0:
        (nums3.append(num1))
print (nums3)

# Given a list of numbers, print whether all numbers are positive.
#	•	If all are positive → print "All positive"
#	•	Otherwise → print "Contains non-positive"
print ("------------------------------")

nums = [1, 2, 2, 4, 5, 6, 7, 8, 10]

if num in nums >= 0:
    print ("All positive")
else: 
    print ("Contains non-positive")
