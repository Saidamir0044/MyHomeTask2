# 1. Circle Class
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


# 2. Person Class
class Person:
    def __init__(self, name, country, date_of_birth):  # 'YYYY-MM-DD'
        self.name = name
        self.country = country
        self.date_of_birth = datetime.strptime(date_of_birth, '%Y-%m-%d')

    def get_age(self):
        today = datetime.today()
        age = today.year - self.date_of_birth.year
        if (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day):
            age -= 1
        return age


# 3. Calculator Class
class Calculator:
    def add(self, x, y): return x + y
    def subtract(self, x, y): return x - y
    def multiply(self, x, y): return x * y
    def divide(self, x, y): return x / y if y != 0 else "Cannot divide by zero"


# 4. Shape and Subclasses
class Shape:
    def area(self): pass
    def perimeter(self): pass

class CircleShape(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))


# 5. Binary Search Tree
class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = self.right = None

class BST:
    def insert(self, root, key):
        if not root:
            return BSTNode(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
        return root

    def search(self, root, key):
        if not root or root.key == key:
            return root
        elif key < root.key:
            return self.search(root.left, key)
        return self.search(root.right, key)


# 6. Stack
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if not self.stack:
            return "Stack is empty"
        return self.stack.pop()

    def display(self):
        print("Stack:", self.stack)


# 7. Linked List
class LLNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        node = LLNode(data)
        if not self.head:
            self.head = node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = node

    def delete(self, key):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            return
        prev = None
        while cur and cur.data != key:
            prev, cur = cur, cur.next
        if cur:
            prev.next = cur.next

    def display(self):
        cur = self.head
        while cur:
            print(cur.data, end=" -> ")
            cur = cur.next
        print("None")


# 8. Shopping Cart
class ShoppingCart:
    def __init__(self):
        self.items = {}  # item: (price, quantity)

    def add_item(self, item, price, quantity=1):
        if item in self.items:
            old_price, old_qty = self.items[item]
            self.items[item] = (price, old_qty + quantity)
        else:
            self.items[item] = (price, quantity)

    def remove_item(self, item):
        if item in self.items:
            del self.items[item]

    def total_price(self):
        return sum(price * qty for price, qty in self.items.values())


# 9. Stack with Display (already merged with 6)


# 10. Queue
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if not self.queue:
            return "Queue is empty"
        return self.queue.pop(0)

    def display(self):
        print("Queue:", self.queue)


# 11. Bank Class
class BankAccount:
    def __init__(self, account_number, holder, balance=0):
        self.account_number = account_number
        self.holder = holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        self.balance -= amount
        return self.balance

    def get_balance(self):
        return self.balance

class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, holder):
        if account_number in self.accounts:
            return "Account already exists"
        self.accounts[account_number] = BankAccount(account_number, holder)

    def get_account(self, account_number):
        return self.accounts.get(account_number, "Account not found")
