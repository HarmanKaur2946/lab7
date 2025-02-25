# 1
Create a tuple
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)

# 2
Create a tuple with different data types
mixed_tuple = (1, "Hello", 3.14, True)
print(mixed_tuple)

# 3
Create a tuple with numbers and print one item
num_tuple = (10, 20, 30, 40, 50)
print(num_tuple[2])  # Prints the third item

# 4
Unpack a tuple into several variables
a, b, c, d, e = num_tuple
print(a, b, c, d, e)

# 5
Add an item in a tuple (Tuples are immutable, so we create a new one)
new_tuple = num_tuple + (60,)
print(new_tuple)

# 6
Convert a tuple to a string
char_tuple = ('P', 'y', 't', 'h', 'o', 'n')
string = ''.join(char_tuple)
print(string)

# 7 
Get the 4th element and 4th element from last of a tuple
print(num_tuple[3], num_tuple[-4])

# 8
Create a clone (copy) of a tuple
clone_tuple = num_tuple[:]
print(clone_tuple)

# 9
Find repeated items in a tuple
repeated_tuple = (1, 2, 3, 2, 4, 5, 2, 6)
print(repeated_tuple.count(2))  # Count occurrences of 2

# 10
Check whether an element exists in a tuple
print(3 in num_tuple)  # True if 3 is in the tuple

# 11
Convert a list to a tuple
my_list = [100, 200, 300]
converted_tuple = tuple(my_list)
print(converted_tuple)

# 12
Remove an item from a tuple (Tuples are immutable, so we create a new one)
temp_list = list(num_tuple)  
temp_list.remove(30)  
modified_tuple = tuple(temp_list)
print(modified_tuple)

# 13
Slice a tuple
print(num_tuple[1:4])  # Prints elements from index 1 to 3

# 14
Find the index of an item in a tuple
print(num_tuple.index(40))  # Finds index of 40

# 15
Find the length of a tuple
print(len(num_tuple))  # Prints the length of the tuple
