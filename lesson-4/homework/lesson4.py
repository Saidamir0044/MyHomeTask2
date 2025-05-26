# Ex1
my_dict = {'apple': 10, 'banana': 5, 'orange': 8, 'kiwi': 12}

ascending = dict(sorted(my_dict.items(), key=lambda item:item[1]))
print('Ascending order:', ascending)

descending = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
print("Descending order:", descending)

# Ex2
my_dict = {0: 10, 1: 20}

my_dict.update({2: 30})
print(my_dict)

# Ex3
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

birlashgan = {}
birlashgan.update(dic1)
birlashgan.update(dic2)
birlashgan.update(dic3)
print(birlashgan)

# Ex4
n = int(input("Enter a number (n): "))
squares_dict = {x: x*x for x in range(1, n+1)}
print("Generated dictionary:", squares_dict)

# Ex5
squares_dict = {x: x*x for x in range(1, 16)}
print("Generated dictionary:", squares_dict)

# Ex6
my_set = {1,2,3,4}
print(my_set)

# Ex7
my_set = {1,2,3,4}
for i in my_set:
    print(i)
  
# Ex8
my_set = {1,2,3,4}
my_set.update({3,4,5,6})
print(my_set)

my_set.add(7)
print(my_set)

# Ex9
my_set = {1,2,3,4}
my_set.remove(2)
print(my_set)
my_set.difference_update({4,3})
print(my_set)

# Ex10
my_set = {1, 2, 3, 4, 5}
item_to_remove = 3

if item_to_remove in my_set:
    my_set.remove(item_to_remove)

print(my_set)

