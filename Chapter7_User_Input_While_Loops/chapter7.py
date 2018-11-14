# USER INPUT & WHILE LOOPS

# input() function
# Pauses program and waits for user's input
# When input received, info stored in a variable for later

# message = input("Tell me something, and I'll repeat if back to you:")
# print(message)

# name = input("Please enter your name:")
# print ("Hi," + name.title() + "!" )

# MULTI-LINE PROMPTS
# You can store prompt in a variable and pass that variable to input() function to build several lines

# prompt  = "I'm going to personalize a greeting for you!"
# prompt += "\nWhat's your name?"
#
# name = input(prompt)
# print ("You're a rockstar, " + name.title() + "!")

# NUMERICAL INPUTS
# Python interprets everything in input as a string
# age = input("How tall are you:")
# print(age)


# WHILE LOOPS
# While Loops run as long as certain condition true
# Count from 1-5
current_num = 1
while current_num <= 5:
    print(current_num)
    current_num += 1

# Letting users CHOOSE WHEN TO QUIT
# Define a quit value
# Program will run until quit value entered
prompt = "Tell me somthin', I'll say it back:"
prompt = "\nEnter 'quit' to end program."
message = ""
while message != 'quit':
    message = input(prompt))
    print(message)


# Using a Flag
