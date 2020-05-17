# Sibling dictionary
anna = {}
anna["age"] = 27
anna["location"] = "New York"
anna["hair_color"] = "Brown"
anna['eye_color'] = "Hazel"
anna["height"] = "5'6"
print(anna)
print(anna["location"])
print(anna['eye_color'])

Favorite_Numbers = {}
Favorite_Numbers['Joey'] = 12
Favorite_Numbers['Anna'] = 11
Favorite_Numbers['Kat'] = 7

for key in Favorite_Numbers:
    print(key + "'s favorite number is " + str(Favorite_Numbers[key]))


alphabet = {"a": "apple", "b": "balloon", "c": "car"}
for key, value in alphabet.items():
    print("Key:" + key)
    print("Value:" + value)

for letter in alphabet:
    print(letter.upper() + " is for " + alphabet[letter].capitalize())

for object in alphabet.values():
    print(object)

Landmarks = {
    "Grand Canyon": "Arizona",
    "Golden Gate Bridge": "San Francisco",
    "Niagra Falls": "New York",
    "White House": "Washington D.C"}

for landmark in Landmarks:
    print(landmark + "is located in " + Landmarks[landmark])

print("These are my favorite landmarks:")
for landmark in Landmarks:
    print(landmark)

print("These states have cool landmarks:")
for location in Landmarks.values():
    print(location)


siblings = {
    "anna": 27,
    "joey": 24,
    "kat": 18
}

housemates = {
    "anna": 27,
    "joey": 24,
    "nancy": 65,
    "gary": 65
}

for sibling in siblings:
    if sibling in housemates:
        print(sibling + " is also my housmate")

for sibling in siblings:
    if sibling not in housemates:
        print(sibling.capitalize() + " doesn't live with me")


siblings = {
    "anna": 27,
    "joey": 24,
    "kat": 18
}

friends = {
    "betty": 29,
    "gretta": 24,
    "dobby": 19
}

for sibling in siblings:
    if siblings[sibling] in friends.values():
        print(sibling.capitalize() +
              " is same age as my friend, ")


# joey and gretta are the same age
Winnie = {
    "Name": "Winnie",
    "Breed": "Bichon Frise",
    "Color": "White"}
Boo = {
    "Name": "Boo",
    "Breed": "Lhasa Apso",
    "Color": "Black"}
Bella = {
    "Name": "Bella",
    "Breed": "Shih Tsu",
    "Color": "Tan"}

Pets = []
Pets.append(Winnie)
Pets.append(Boo)
Pets.append(Bella)
print(Pets)

for pet in Pets:
    print(pet["Breed"])

for pet in Pets:
    print(pet["Color"])


my_pets = {"Winnie": Winnie, "Bella": Bella, "Boo": Boo}
for pet in my_pets:
    print(my_pets[pet])
    print(my_pets[pet]["Breed"])
    print(my_pets[pet]["Color"])
