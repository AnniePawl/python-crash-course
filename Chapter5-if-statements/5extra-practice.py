cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())


age_0 = 22
age_1 = 18

print(age_0 >= 21 or age_1 >= 21)

requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_toppings)


friends = ['rebi', 'nicky', 'grace']
if 'clara' in friends:
    print("Omg yay")
else:
    print("Omg where is she?")

# if conidtion_test
  # do something

age = 12
# if age < 21:
#     print("omg too young tho")
# else:
#     print("Kk come in ")

if age <= 5:
    print("Free Admission!")
elif age >= 10:
    print("5 bucks")
else:
    print("10 buckeroonies")


alien_color = 'Green'
if alien_color.lower() == 'green':
    print("5 points for green!")
elif alien_color.lower() == 'red':
    print("10 points for red")
elif alien_color.lower() == 'blue':
    print('15 points for blue')
else:
    print("Not Valid")


# Stages of Life
human = 25
if human <= 2:
    print("Toddler")
elif human > 2 and human <= 10:
    print("Kid")
elif human > 10 and human <= 20:
    print("Youngish")
elif human > 20 and human < 30:
    print("Grownish")


users = ['bella', 'bonny', 'becky', 'admin']
for user in users:
    if user == 'admin':
        print("Hi Admin! Want a special report?")
    else:
        print("Welcome back, " + user.title())

current_users = ['amy', 'andrea', 'ally', 'abby', 'bill']
new_users = ['brad', 'brendan', 'bill']

for user in new_users:
    if user in current_users:
        print("Hi," + user + ". You already exist!")
    else:
        print("New Username available!")

numbers = list(range(1, 11))
for number in numbers:
    if number == 1:
        print(str(number) + "st")
    elif number == 2:
        print(str(number) + "nd")
    elif number == 3:
        print(str(number) + "rd")
    else:
        print(str(number) + "th")


def siblings(siblings):
    return 'boo' not in siblings


print(siblings(['Anna', 'Joey', 'Kat']))


def hello_admin(username):
    if username == "":
        return "We need to find some users!"
    elif username == 'admin':
        return "Hello Admin, would you like a  status report?"
    else:
        return "Hello, " + username


print(hello_admin("admin"))
print(hello_admin("Anna"))
print(hello_admin(""))


def createUsername(current_usernames,  new_usernames):
    for new_username in new_usernames:
        if new_username in current_usernames:
            print(new_username + " is already taken, try again")
        else:
            print(new_username + " is available")


current_usernames = ['Anna', 'Joey', 'Kat', 'Nancy', 'Gary']
new_usernames = ['Nancy', 'Gary',  'Winnie', 'Boo']

print(createUsername(current_usernames, new_usernames))


def ordinal_numbers(numbers):
    for num in numbers:
        if num == 1:
            print(str(num) + "st")
        elif num == 2:
            print(str(num) + "nd")
        elif num == 3:
            print(str(num) + "rd")
        else:
            print(str(num) + "th")


print(ordinal_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9]))
