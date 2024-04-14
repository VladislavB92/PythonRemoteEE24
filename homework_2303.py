# Task 1: String Length

user_input = input("Enter a string: ")
print("Length of the string:", len(user_input))

# Task 2: Uppercase Conversion

user_input = input("Enter a string: ")
print("Uppercase string:", user_input.upper())

# Task 3: Lowercase Conversion

user_input = input("Enter a string: ")
print("Lowercase string:", user_input.lower())

# Task 4: Capitalize

user_input = input("Enter a string: ")
print("Capitalized string:", user_input.capitalize())

# Task 5: Counting Substrings

user_string = input("Enter a string: ")
substring = input("Enter a substring: ")
print("Number of occurrences:", user_string.count(substring))

# Task 6: Checking Substring Existence

user_string = input("Enter a string: ")
substring = input("Enter a substring: ")
if user_string.find(substring) != -1:
	print("Substring exists.")
else:
	print("Substring does not exist.")

# Task 7: String Reversal

user_input = input("Enter a string: ")
print("Reversed string:", user_input[::-1])

# Task 8: Splitting Strings

user_input = input("Enter a sentence: ")
words = user_input.split()
print("Words in the sentence:", words)

# Task 9: Joining Strings

words = ['Hello', 'world', 'from', 'Python']
joined_string = ' '.join(words)
print("Joined string:", joined_string)

# Task 10: Stripping Whitespace

user_input = input("Enter a string with extra whitespace: ")
stripped_string = user_input.strip()
print("String with whitespace stripped:", stripped_string)

# --------

# Task 1: List Length

my_list = [1, 2, 3, 4, 5]
print("Length of the list:", len(my_list))

# Task 2: Appending Elements

my_list = []
my_list.append(1)
my_list.append(2)
my_list.append(3)
print("Updated list after appending elements:", my_list)

# Task 3: Counting Elements

my_list = [1, 2, 3, 4, 2, 5, 2]
count = my_list.count(2)
print("Number of occurrences of 2:", count)

# Task 4: Removing Elements

my_list = [1, 2, 3, 4, 5]
my_list.remove(3)
print("Updated list after removing 3:", my_list)

# Task 5: Extending Lists

list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
print("Extended list:", list1)

# Task 6: Index of Element

my_list = [1, 2, 3, 4, 5]
index = my_list.index(3)
print("Index of 3:", index)

# Task 7: Inserting Elements

my_list = [1, 2, 4, 5]
my_list.insert(2, 3)
print("Updated list after inserting 3 at index 2:", my_list)

# Task 8: Popping Elements

my_list = [1, 2, 3, 4, 5]
popped_element = my_list.pop(2)
print("Popped element at index 2:", popped_element)

# Task 9: Reversing List

my_list = [1, 2, 3, 4, 5]
my_list.reverse()
print("Reversed list:", my_list)

# Task 10: Sorting List

my_list = [3, 1, 4, 2, 5]
my_list.sort()
print("Sorted list in ascending order:", my_list)
