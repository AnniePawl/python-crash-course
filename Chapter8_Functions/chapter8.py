#Functions

# Simplest Function Structure
# Define it, call it at the bottom
def greet_user():
    """Display  a simple greeting."""
    print("hi!")

greet_user()

# Passing Information to a Function
# Adding username allows function to accept any value of username each time you call it.
def invitation (name):
    print("Hey, " + name.title()+ "You're a super star!")

invitation("Jess")\
