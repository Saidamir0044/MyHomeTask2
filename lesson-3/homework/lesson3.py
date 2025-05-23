
# 1. Create and Access List Elements
fruits = ['apple', 'banana', 'cherry', 'date', 'fig']
print("Third fruit:", fruits[2])

# 2. Concatenate Two Lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
concatenated = list1 + list2
print("Concatenated list:", concatenated)

# 3. Extract Elements from a List
numbers = [10, 20, 30, 40, 50]
first = numbers[0]
middle = numbers[len(numbers)//2]
last = numbers[-1]
extracted = [first, middle, last]
print("Extracted elements:", extracted)

# 4. Convert List to Tuple
movies = ['Inception', 'Matrix', 'Titanic', 'Avatar', 'Gladiator']
movies_tuple = tuple(movies)
print("Movies as tuple:", movies_tuple)

# 5. Check Element in a List
cities = ['New York', 'London', 'Paris', 'Tokyo']
print("Is Paris in the list?", "Paris" in cities)

# 6. Duplicate a List Without Using Loops
nums = [1, 2, 3]
duplicated = nums * 2
print("Duplicated list:", duplicated)

# 7. Swap First and Last Elements of a List
sample_list = [10, 20, 30, 40]
sample_list[0], sample_list[-1] = sample_list[-1], sample_list[0]
print("Swapped list:", sample_list)

# 8. Slice a Tuple
numbers_tuple = tuple(range(1, 11))
print("Sliced tuple (index 3 to 7):", numbers_tuple[3:8])

# 9. Count Occurrences in a List
colors = ['red', 'blue', 'green', 'blue', 'yellow', 'blue']
blue_count = colors.count('blue')
print("Number of times blue appears:", blue_count)

# 10. Find the Index of an Element in a Tuple
animals = ('cat', 'dog', 'lion', 'tiger')
lion_index = animals.index('lion')
print("Index of 'lion':", lion_index)

# 11. Merge Two Tuples
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
merged_tuple = tuple1 + tuple2
print("Merged tuple:", merged_tuple)

# 12. Find the Length of a List and Tuple
sample_list = [10, 20, 30, 40]
sample_tuple = (5, 15, 25, 35, 45)
print("Length of list:", len(sample_list))
print("Length of tuple:", len(sample_tuple))

# 13. Convert Tuple to List
num_tuple = (11, 22, 33, 44, 55)
num_list = list(num_tuple)
print("Tuple converted to list:", num_list)

# 14. Find Maximum and Minimum in a Tuple
num_tuple = (8, 3, 15, 2, 29, 6)
print("Maximum:", max(num_tuple))
print("Minimum:", min(num_tuple))

# 15. Reverse a Tuple
words = ('hello', 'world', 'python', 'tuple')
reversed_tuple = words[::-1]
print("Reversed tuple:", reversed_tuple)
