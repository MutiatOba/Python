# collections

# # lists
#
# # array = list
#
# # first list = shopping list
# # [] = list
#
# shopping_list = ["milk", "bread", "eggs", "chocolate", "jam"]
# print(shopping_list)
# print(type(shopping_list))
#
# # accesing a particular part of the list
# print(shopping_list[0])
#
# # change an element in a list
# shopping_list[2] = "butter"
# print(shopping_list)
#
# #using list methods
#
# # add to the list with append()
#
# shopping_list.append("fish")
# print(shopping_list)
#
# # removing items with remove()
# shopping_list.remove("bread")
# print(shopping_list)
#
# # removing the last item from list without specifying what it is
# shopping_list.pop()
# print(shopping_list)
#
# # can I have a list of mixed datatypes? yes
# mixture = [1, 2, 4.5, "five", "six"]
# print(mixture)
#
# #slicing
#
# print(mixture[1:3])
#
# # reverse orfer of the slice
# print(mixture[-2::])
# print(mixture[-2])
#
# #step over
# print(mixture[::2])
#
# #tuple are immutable - it cant be changed
# tuple_example = ("bread", "eggs", "milk")
#
# print(tuple_example)

# dictionary

#another way to manage data, but they are a little bit more dynamic and complex

# key-value pair
#value = data mechanism you wish to store the data in (e.g. string, int, list, another dictionary)

student_1 = {
    "name": "Mutiat",
    "stream": "devops",
    "completed_lessons": 4,
    "completed_lesson_names": ["variable", "datatypes", "setup"]
}

#access the disctionary

print(student_1["stream"])

#access a part of the list in the disctionary
print(student_1["completed_lesson_names"][0])

#want to change a value in a dictionary
student_1["completed_lessons"] = 3
print(student_1["completed_lessons"])

#changing an element of a list within a dictionary
student_1["completed_lesson_names"].remove("datatypes")
print(student_1["completed_lesson_names"])

# dictionary methods

print(student_1.keys())
print(student_1.values())

# sets and frozen sets

#sets in python is a list that has no oder/indexing
car_parts = {"wheels", "doors", "exhaust"}
print(car_parts)
car_parts.add("windows")
print(car_parts)
car_parts.discard("doors")
print(car_parts)

#frozen sets - it is immutable

x= frozenset([1, 2, 3, 4])



