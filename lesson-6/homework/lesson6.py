# Ex2 Integer Squares Exercise
n = int(input('Son kirit:'))

for i in range(0,n):
    print(n*n)



# Ex1 Loop-Based Exercises
i = 1
while i <= 10:
    print(i)
    i += 1

# Ex2 Loop-Based Exercises
rows = 5

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print()

# Ex3 Loop-Based Exercises
num = int(input('Given number:'))
print(((1+num)/2)*num)
# Ex4 Loop-Based Exercises

i = 1
while i <= 20:
    if i%2==0:
        print(i) 
    i += 1
# Ex5 Loop-Based Exercises
numbers = [12, 75, 150, 180, 145, 525, 50]

for i in numbers:
    if i%25==0:
        print(i)
# Ex6 Loop-Based Exercises
n = int(input('Raqam kiriting:'))
count = len(str(abs(n)))
print(count)

# Ex7 Loop-Based Exercises
list1 = [10, 20, 30, 40, 50]
print(range(len(list1)-1, -1, -1))
# Ex8 Loop-Based Exercises
list1 = [10, 20, 30, 40, 50]

for i in range(len(list1)-1, -1, -1):
    print(list1[i])

# Ex9 Loop-Based Exercises
  for n in range(-10, 0):
    print(n)

# Ex10 Loop-Based Exercises
for n in range(0,5):
    print(n)
print('Done')
# Ex11 Loop-Based Exercises
for num in range(25, 51):
    if num > 1:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            print(num)

# Ex12 Loop-Based Exercises
n_terms = 10
a, b = 0, 1

for _ in range(n_terms):
    print(a)
    a, b = b, a + b
# Ex13 Loop-Based Exercises
num = int(input("Enter a number: "))
factorial = 1

if num < 0:
    print("Factorial does not exist for negative numbers.")
elif num == 0:
    print("The factorial of 0 is 1.")
else:
    for i in range(1, num + 1):
        factorial *= i
    print("The factorial of", num, "is", factorial)

# Ex4  Return Uncommon Elements of Lists
from collections import Counter

def uncommon_elements(list1, list2):
    c1 = Counter(list1)
    c2 = Counter(list2)
    
    # Elements unique to list1
    only_in_list1 = c1 - c2
    # Elements unique to list2
    only_in_list2 = c2 - c1
    
    # Combine results
    result = list(only_in_list1.elements()) + list(only_in_list2.elements())
    return result
