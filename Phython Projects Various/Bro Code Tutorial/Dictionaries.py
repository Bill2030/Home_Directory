# Dictionary = Changeable, unordered collection of unique key : Value pairs
# fast because they are hashing allows us to access the value quickly.

Capitals = { "USA": "Washington DC",
             "China": "Beijing",
             "India": "New Deli"
}
print(Capitals["India"]) # You access the values by using keys
# Dictionaries uses Get Method to identify the items
print(Capitals.get("Germany")) # This will bring none because Germany doesnt exist
print(Capitals.get("USA"))
print(Capitals.keys()) # This will print the keys only
print(Capitals.values()) # This will print the values only
print(Capitals.items())# This will print the entire dictionary

Capitals.update({"Germany": "Berlin"}) # used to add an item in the dictionary
Capitals.update({"USA": "Les Vegas"}) # Used if you want to change the value of specific key


for key,value in Capitals.items():
    print(key,value) # Used to iterate the entire dictionary
