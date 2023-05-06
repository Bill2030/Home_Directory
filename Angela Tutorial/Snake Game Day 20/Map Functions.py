def square(n):
    return n * n
my_list = [2,3,4,5,6,7,8,9]
updated_list = map(square, my_list)
print(updated_list)
print(list(updated_list))

def myMapFunc(n): # Using map with list
    return n * 10
updated_list = map(myMapFunc, my_list)
print(updated_list)
print(list(updated_list))

def myMapFunc(n): #Using Map with Tuple
    return n.upper()
my_tuple = ("php", "java","python")
updated_list = map(myMapFunc, my_tuple)
print(list(updated_list))

def myMapFunc(n): # Using map with dictionary
    return n * 10
my_dict = {2,3,4,5,6,7,8,9}
final_items = map(myMapFunc, my_dict)
print(list(final_items))

def myMapFunc(list1, list2): # Multiple list inside a map funtion
    return list1 + list2
list1 = [2,3,4,5,6,7,8,9]
list2 = [4,8,12,16,20,24]
updated_list = map(myMapFunc, list1,list2)
print(list(updated_list))
