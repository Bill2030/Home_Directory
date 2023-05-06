# tuple = collection which is ordered and unchangeable used to group related data
# The difference between lists and tuple is that lists uses square brackets and its
# Mutable or changeable while Tuple uses closing brackets and unchangeable.
# The only available methods in tuple is count and index
student = ("Bro", "male",21)
print(student.count("Bro"))
print(student.index("male"))

for x in student:
    print(x)

if "Bro" in student:
    print("Bro is here")
