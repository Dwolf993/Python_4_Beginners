#Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.

elements = input("Please enter few valuesseparated by comma (,): ")
list = elements.split(",")
tuple = tuple(list)
print(list)
print(tuple)

