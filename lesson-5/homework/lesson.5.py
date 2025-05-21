# Ex1
year = int(input('Yilni kiriting: '))


if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print('Leap year')
else:
    print('Not leap year')
# Ex2
# With 
a = int(input())
b = int(input())

if a % 2 != 0:
    a += 1  # start from next even number if a is odd

if a <= b:
    evens = list(range(a, b+1, 2))
    print(evens)
else:
    print([])
  # Without
a = int(input())
b = int(input())

evens = list(range(a + (a % 2), b + 1, 2)) * (a <= b)
print(evens)

