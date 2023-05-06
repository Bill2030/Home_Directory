# set = Collection which is unordered and unindexed. No duplicate values.
# Sets are normally closed using curly braces {}

utensils = {"fork", "Knife", "Spoon"}
dishes = {"bowl", "plate", "cup", "knife"}
#print(utensils) # Once printed you will realize that its unordered.
#print(utensils.union(dishes)) # joining of two sets use union
#print(utensils.difference(dishes)) # Will print what one set has and the other doesnt
print(utensils.intersection(dishes)) # This will return something they have in common
