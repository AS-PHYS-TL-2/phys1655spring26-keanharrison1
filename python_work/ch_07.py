

number = input ("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print (f"The number {number} is even.")
else: 
    print (f"The number {number} is odd.")


# While loops
current_number = 1          # start counting from 1
while current_number <= 5:  # while loop keeps running as long as the value of 
                            # current_number is less than or equal to 5
    print (current_number)  # prints value of current_number and adds 1 to that value
    current_number += 1

# Because 1 is less than 5, Python prints 1 and then adds 1, making the current number 2.
# Because 2 is less than 5, Python prints 2 and then adds 1, making current_number 3.

# program that says hi 3 times

i = 3

if i != 0:
    print ("hi")
    i = i - 1
    print (i)
if i != 0:
    print ("hi")
    i = i - 1
    print (i)

# While allows you to ASK A QUESTION OVER AND OVER AGAIN
i = 3
while i != 0:
    print ("hi")
    print (f"counter i: {i}")
    i = i - 1

# new keyword: break

number = int(input("Enter a positive integer: "))
while True: 
    if number > 0:
        break

# asks for positive integer
# enters infinite loop because we didn't write a program for the possibility of the integer being negative
