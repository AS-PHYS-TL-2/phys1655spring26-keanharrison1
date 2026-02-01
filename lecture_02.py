
# Date: Thursday, Jan 15, 2025

# Notes / Programs
print ("hello world")
print ("hello", "world") # why does this print hello world and not helloworld? 
# print() separates arguments by DEFAULT
print ("hello", "world", sep = "")

# defining a new function
def my_function():
    print ("my name is X") # 'blocks' within function can be anything
    print ("my dog is Y")
my_function() # this calls the function. Without calling, the above will not be printed. 

def greet():
    print ("hello")
print ("goodbye") # prints goodbye first because python reads top-to-bottom, and greet() is only called below, after the print function of "goodbye" is called
greet()


input ("What is your name?") # asks for user prompt
print (input("What is your name?")) # prints input question AND user prompt

# Important operator signs
# = assignment (Whatever you have on the RIGHT will be assigned to the value on the LEFT)
# == equality comparison (T / F)

# Use type() to determine the data type of an object

# int --> integers
# float --> decimals
# bool --> T/F
# str --> text/strings

print ("------------------")

# How to assign objects 
radius = 2 # binding variable RADIUS to value 1
print (radius)
area = 3.14 * (radius**2) # ** is exponent so this would be 3.14 times 1 (radius) ^2
print (area)

radius = radius + 1
print (radius)
print (area)
