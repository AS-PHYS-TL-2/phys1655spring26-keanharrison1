

# Chapter 5 notes - Python crash course

# If statements - allows you to examine the current state of a program and respond appropriately to that state

cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars: # 'car' is a made up variable loop
    if car == 'bmw': 
        print (car.upper())
    else: 
        print (car.title()) # capitalizes the first letter of each word regardless of prior casing

# equality operator: == (car == 'bmw') -- does car equal to bmw
# assignment operator: = (car = 'bmw') -- sets the value of car to 'bmw'

# SIMPLE EXAMPLE ----------
car = 'Audi'
car.lower() == 'audi'
print (car.lower())

# INEQUALITY OPERATOR ----------
requested_topping = "mushrooms"
if requested_topping != "anchovies":
    print ("Hold the anchovies!")

# IF AND ELSE STATEMENTS ----------
age1 = 18
age2 = 18
if age1 >= 21 and age2 >= 21:
    print ("True")
else:
    print ("False")

if age1 >= 21 or age2 >= 21: 
    print ("True")
elif (age1 and age2) < 21: 
    print ("False")


# IN (Keyword) ----------
my_toppings = ["pepperoni", "cheese", "ham", "pineapple"]
if 'pepperoni' in my_toppings: 
    print ("True")
else:
    print ("False")  

# Exercises

# TRY IT YOURSELF

# 5-1. Conditional Tests: Write a series of conditional tests. Print a statement describing each test and your prediction for the results of each test. Your code should look something like this:

# Look closely at your results, and make sure you understand why each line evaluates to True or False.
# Create at least 10 tests. Have at least 5 tests evaluate to True and another 5 tests evaluate to False.

# 5-2. More Conditional Tests: You don’t have to limit the number of tests you create to 10. If you want to try more comparisons, write more tests and add them to conditional_tests.py. Have at least one True and one False result for each of the following:

# -- Tests for equality and inequality with strings
# -- Tests using the lower() method
# -- Numerical tests involving equality and inequality, greater than and less than, greater than or equal to, and less than or equal to
# -- Tests using the and keyword and the or keyword
# -- Test whether an item is in a list
# -- Test whether an item is not in a list

# if statements
# NOTE: all indented lines after an if statement will be executed if the test passes

# IF ELSE STATEMENTS ----------

age = 18

if age < 4:
    print ("Free")
elif 4 <= age <= 18: 
    print ("25")
else:
    print ("40")    

# NOTE: Python NEVER runs tests BEYOND the first passed test in an if-elif-else chain.  

# TRY IT YOURSELF

# 5-3. Alien Colors #1: Imagine an alien was just shot down in a game. Create a variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.

# Write an if statement to test whether the alien’s color is green. If it is, print a message that the player just earned 5 points.
# Write one version of this program that passes the if test and another that fails. (The version that fails will have no output.)

# 5-4. Alien Colors #2: Choose a color for an alien as you did in Exercise 5-3, and write an if-else chain.

# If the alien’s color is green, print a statement that the player just earned 5 points for shooting the alien.
# If the alien’s color isn’t green, print a statement that the player just earned 10 points.
# Write one version of this program that runs the if block and another that runs the else block.

# 5-5. Alien Colors #3: Turn your if-else chain from Exercise 5-4 into an if-elif-else chain.

# If the alien is green, print a message that the player earned 5 points.
# If the alien is yellow, print a message that the player earned 10 points.
# If the alien is red, print a message that the player earned 15 points.
# Write three versions of this program, making sure each message is printed for the appropriate color alien.

# 5-6. Stages of Life: Write an if-elif-else chain that determines a person’s stage of life. Set a value for the variable age, and then:

# If the person is less than 2 years old, print a message that the person is a baby.
# If the person is at least 2 years old but less than 4, print a message that the person is a toddler.
# If the person is at least 4 years old but less than 13, print a message that the person is a kid.
# If the person is at least 13 years old but less than 20, print a message that the person is a teenager.
# If the person is at least 20 years old but less than 65, print a message that the person is an adult.
# If the person is age 65 or older, print a message that the person is an elder.

# 5-7. Favorite Fruit: Make a list of your favorite fruits, and then write a series of independent if statements that check for certain fruits in your list.

# Make a list of your three favorite fruits and call it favorite_fruits.
# Write five if statements. Each should check whether a certain kind of fruit is in your list. If the fruit is in your list, the if block should print a statement, such as You really like bananas!

# FOR LOOPS ----------

my_toppings = ["mushrooms", "green peppers", "extra cheese"]
for my_topping in my_toppings: 
    print (f"Adding {my_topping}.")

print ("\nFinished making your pizza!")   

# CHECKING THAT A LIST IS NOT EMPTY
my_toppings = []
if my_toppings: 
    for my_topping in my_toppings: 
        print (f"Adding {requested_topping}.")
    print ("\nFinished making your pizza!")
else:
    print ("Are you sure you want a plain pizza?")    