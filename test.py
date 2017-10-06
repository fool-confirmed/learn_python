'''
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# for loop
for i in a:
    if i < 5:
        print(i, end = ' ')
print()

# filter function
b = filter(lambda x: x < 5, a)
print(list(b))

# expression
c = (i for i in a if i < 5)
print(list(c))

# one line
print(list(i for i in a if i < 5))
'''

'''
n = int(input("enter a number: "))
if n % 2 == 0:
    print("it is an even number")
    if n % 4 == 0:
        print("it is 4x")
        
else:
    print("it is an odd number")
'''

'''
myList = []

for i in range(5):
    name, age = input("enter a name "), input("enter an age ")
    print("You entered {} and {}.".format(name, age))

    myList.append((i, name, age))

    for item in myList:
        print("{}: {}, {}".format(item[0], item[1], item[2]))
        
'''
