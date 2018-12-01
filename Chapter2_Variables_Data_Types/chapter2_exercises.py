# Store Simple Message
message = "You're a shitty friend"
print (message)

tom = "Thomas"
print ("Hello, " + tom + "! You're gr8" )

first_name = "anna"
last_name = "pawl"
full_name = first_name.title() + " " + last_name.title()
print("Hello, " + full_name + "!")

car = "MazDa"
model = "miata"
print ("I own a " + car.title() + " " + model.title())


# NAME CASES
# Store a person's name in a variable and change it to lowercase, uppercase, and titlecase
name =  "BERNARD buttoN Cricket"
print (name.lower())
print (name.upper())
print (name.title())

name = "boo jenkins"
print(name.title())
print(name.upper())

name = "Kim"
message = "Hi " + name + "!"
print(message)
print(name.upper())
print(name.lower())
print(name.title())


# PRINT MULTI-LINE STRING
print("Languages include: \n\tPython\n\tJavaScript\n\tC+")

print ("""Albert Einstein once said,
\'A person who never made a mistake
 never tried anything new.\'""")

print ("'A person who never made a mistake, \nnever tried anything new' \n\t -Albert Einstein")

quotee = "Beverly"
quote = "\nRoses are red, \nViolets are blue,\nYou're an absolutely horrible person,\nI'm going to sue."
print (quotee + " once said: " + quote)

poem = "Roses are red\n\tViolets are blue\n\tYou're kind of shitty\n\tBut still I love you"
print("He once wrote:\n\t" + poem )


# BASIC MATH
# Write addition, subtraction, multiplication, and division operations that each result in the number 8
print (5 + 3)
print (10 - 2)
print (2 * 4)
print (int(16 / 2))

# WORK WITH DIFFERENT TYPES
fave_num = 11
print ("My favorite number is " + str(fave_num) + "!")

number_of_pets = 5
print ("He has " + str(number_of_pets) + " pets!")

height = 7
print ("He was " + str(height) + "ft tall!")

# Write a Happy Birthday Message!
name = "gary"
age = 65
message = "Happy " + str(age) + "th Birthday " + name.title() + "!"
print(message)
