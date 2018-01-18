# Lists
the_count = [1, 2, 3, 4, 5]
shopping_list = ["Noodles", "Eggrolls", "Milk", "rice", "soda", "chips"]

print(shopping_list[0])
print(shopping_list[2])

print(len(shopping_list))

# Going through a list
for item in shopping_list:
    print(item)

for num in the_count:
    print(num * 2)

len(shopping_list) # Gives me the length of the list
range(3) # Gives a list of the numbers 0 through 2
range(len(shopping_list)) # A list of EVERY index in a list

for num in range(len(shopping_list)):
    item = shopping_list[num]
    print("The item at index %d is %s" % (num, item))

# Turn things into a lost
str1 = "Hello CLass!"
listOne = list(str1)
print(listOne)
listOne[11] = '.'
print(listOne)