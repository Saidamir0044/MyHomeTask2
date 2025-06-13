from datetime import date
# 1. Define Task Class:
# Create a Task class with attributes such as task title, description, due date, and status.

class Task:
    def __init__(self, title, description, due_date, status):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status
    
    def __str__(self):
        return(f"Task: {self.title}\n"
               f"Description: {self.description}\n"
               f"Due Date: {self.due_date}\n"
               f"Status: {self.status}")
    
# 2.Define ToDoList Class:
# Create a ToDoList class that manages a list of tasks.
from datetime import date

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, title):
        self.tasks = [task for task in self.tasks if task.title != title]

    def update_status(self, title, new_status):
        for task in self.tasks:
            if task.title == title:
                task.status = new_status
                return True
        return False

    def show_tasks(self):
        if not self.tasks:
            print("Vazifalar ro'yxati bo‘sh.")
        for task in self.tasks:
            print(task)
            print("-" * 30)


# 3.Create Main Program:
# Develop a simple CLI to interact with the ToDoList.

from datetime import datetime, date

class Task:
    def __init__(self, title, description, due_date, status="Pending"):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def __str__(self):
        return (f"Task: {self.title}\n"
                f"Description: {self.description}\n"
                f"Due Date: {self.due_date.strftime('%Y-%m-%d')}\n"
                f"Status: {self.status}")

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, title):
        self.tasks = [task for task in self.tasks if task.title != title]

    def update_status(self, title, new_status):
        for task in self.tasks:
            if task.title == title:
                task.status = new_status
                return True
        return False

    def show_tasks(self):
        if not self.tasks:
            print(" Hech qanday vazifa mavjud emas.")
        for task in self.tasks:
            print(task)
            print("-" * 40)

# Main CLI dastur
def main():
    todo = ToDoList()

    while True:
        print("\n--- ToDo List Dasturi ---")
        print("1. Yangi vazifa qo‘shish")
        print("2. Vazifani o‘chirish")
        print("3. Vazifa holatini yangilash")
        print("4. Barcha vazifalarni ko‘rish")
        print("5. Chiqish")

        tanlov = input("Tanlovingizni kiriting (1-5): ")

        if tanlov == "1":
            title = input("Vazifa sarlavhasi: ")
            description = input("Tavsif: ")
            due = input("Tugash sanasi (YYYY-MM-DD): ")
            try:
                due_date = datetime.strptime(due, "%Y-%m-%d").date()
                task = Task(title, description, due_date)
                todo.add_task(task)
                print(" Vazifa muvaffaqiyatli qo‘shildi.")
            except ValueError:
                print(" Sana formati noto‘g‘ri. Iltimos YYYY-MM-DD ko‘rinishida kiriting.")

        elif tanlov == "2":
            title = input("O‘chiriladigan vazifaning sarlavhasini kiriting: ")
            todo.remove_task(title)
            print("🗑 Vazifa o‘chirildi (agar mavjud bo‘lsa).")

        elif tanlov == "3":
            title = input("Holati yangilanadigan vazifaning sarlavhasi: ")
            new_status = input("Yangi holat (Pending / In Progress / Completed): ")
            updated = todo.update_status(title, new_status)
            if updated:
                print("Holat yangilandi.")
            else:
                print(" Vazifa topilmadi.")

        elif tanlov == "4":
            print("\n Vazifalar ro‘yxati:")
            todo.show_tasks()

        elif tanlov == "5":
            print(" Dasturdan chiqildi.")
            break
        else:
            print(" Noto‘g‘ri tanlov. Iltimos 1 dan 5 gacha bo‘lgan sonni kiriting.")

if __name__ == "__main__":
    main()

# 4.Test the Application:
# Create instances of tasks and test the functionality of your ToDoList.

from datetime import date

# Task klassi
class Task:
    def __init__(self, title, description, due_date, status="Pending"):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def __str__(self):
        return (f"Task: {self.title}\n"
                f"Description: {self.description}\n"
                f"Due Date: {self.due_date}\n"
                f"Status: {self.status}")

# ToDoList klassi
class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, title):
        self.tasks = [task for task in self.tasks if task.title != title]

    def update_status(self, title, new_status):
        for task in self.tasks:
            if task.title == title:
                task.status = new_status
                return True
        return False

    def show_tasks(self):
        if not self.tasks:
            print("📭 Hech qanday vazifa yo‘q.")
        for task in self.tasks:
            print(task)
            print("-" * 40)



todo = ToDoList()


task1 = Task("Python darsi", "Funksiyalarni o‘rganish", date(2025, 6, 10))
task2 = Task("Uy vazifasi", "Matematika mashqlari", date(2025, 6, 11))
task3 = Task("Sport", "30 daqiqa yugurish", date(2025, 6, 9))


todo.add_task(task1)
todo.add_task(task2)
todo.add_task(task3)


print(" Vazifalar ro‘yxati:")
todo.show_tasks()


todo.update_status("Python darsi", "Completed")

todo.remove_task("Sport")

print("\n Yangilangan vazifalar ro‘yxati:")
todo.show_tasks()
## Homework 2. Simple Blog System
# 1.Define Post Class:
# Create a Post class with attributes like title, content, and author.

class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def __str__(self):
        return(f"Title: {self.title}\n"
                f"Author: {self.author}\n"
                f"Content:{self.content}")
    
# 2.Define Blog Class:
# Create a Blog class that manages a list of posts.
# Include methods to add a post, list all posts, and display posts by a specific author.

class Blog: # type: ignore
    def __init__(self):
        self.posts = []
    
    def add_post(self, post):
        self.posts.append(post)

    def list_posts(self):
        if not self.posts:
            print("Sizda postlar yo'q")
        for post in self.posts:
            print(post)
            print("-" * 30)

    def display_posts_by_author(self, author_name):
        found = False
        for post in self.posts:
            if post.author.lower() == author_name.lower():
                print(post)
                print("-" * 40)
                found = True
        if not found:
            print(f"'{author_name}' tomonidan yozilgan hech qanday post topilmadi.")

# 3.Create Main Program:
# Develop a CLI to interact with the Blog system.
# Include options to add posts, list all posts, and display posts by a specific author.

def main():
    blog = Blog()

    while True:
        print("\n--- Blog menyusi ---")
        print("1. Post qo‘shish")
        print("2. Barcha postlarni ko‘rish")
        print("3. Muallif bo‘yicha postlarni ko‘rish")
        print("4. Chiqish")

        choice = input("Tanlovingizni kiriting (1-4): ")

        if choice == '1':
            title = input("Post sarlavhasi: ")
            content = input("Post matni: ")
            author = input("Muallif: ")
            new_post = Post(title, content, author)
            blog.add_post(new_post)
            print("Post muvaffaqiyatli qo‘shildi.")

        elif choice == '2':
            print("\n📋 Barcha postlar:")
            blog.list_posts()

        elif choice == '3':
            author_name = input("Muallif ismini kiriting: ")
            print(f"\n'{author_name}' tomonidan yozilgan postlar:")
            blog.display_posts_by_author(author_name)

        elif choice == '4':
            print("Dastur yakunlandi.")
            break

        else:
            print(" Noto‘g‘ri tanlov. Iltimos, 1 dan 4 gacha tanlang.")


# 4.Enhance Blog System:
# Add functionality to delete a post, edit a post, and display the latest posts.

class Blog:
    def __init__(self):
        self.posts = []
    
    def add_post(self, post):
        self.posts.append(post)

    def list_posts(self):
        if not self.posts:
            print("Sizda postlar yo'q")
        for post in self.posts:
            print(post)
            print("-" * 30)

    def display_posts_by_author(self, author_name):
        found = False
        for post in self.posts:
            if post.author.lower() == author_name.lower():
                print(post)
                print("-" * 40)
                found = True
        if not found:
            print(f"'{author_name}' tomonidan yozilgan hech qanday post topilmadi.")

    def delete_post(self, title):
        for i, post in enumerate(self.posts):
            if post.title.lower() == title.lower():
                del self.posts[i]
                print(f"'{title}' nomli post o‘chirildi.")
                return
        print(f"'{title}' nomli post topilmadi.")

    def edit_post(self, title):
        for post in self.posts:
            if post.title.lower() == title.lower():
                print("Yangi ma’lumotlarni kiriting (bo‘sh qoldirish — o‘zgartirmaslik):")
                new_title = input(f"Yangi sarlavha [{post.title}]: ") or post.title
                new_content = input(f"Yangi matn [{post.content}]: ") or post.content
                new_author = input(f"Yangi muallif [{post.author}]: ") or post.author
                post.title = new_title
                post.content = new_content
                post.author = new_author
                print(" Post muvaffaqiyatli tahrirlandi.")
                return
        print(f"'{title}' nomli post topilmadi.")

    def display_latest_posts(self, n=3):
        if not self.posts:
            print("Hech qanday post mavjud emas.")
            return
        print(f" Oxirgi {n} ta post:")
        for post in self.posts[-n:]:
            print(post)
            print("-" * 30)
# 4. Test the Application:
# Create instances of posts and test the functionality of your Blog system.

# I did in my pc. all is runned

## Homework 3. Simple Banking System
class Account:
    def __init__(self, acc_number, holder_name, balance=0):
        self.acc_number = acc_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} added to account {self.acc_number}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{amount} withdrawn from account {self.acc_number}. New balance: {self.balance}")
        else:
            print("Insufficient balance. Withdrawal denied.")

    def display(self):
        print(f"Account Number: {self.acc_number}")
        print(f"Account Holder: {self.holder_name}")
        print(f"Balance: {self.balance}")
class Bank:
    def __init__(self):
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)
        print(f"Account {account.acc_number} created successfully.")

    def find_account(self, acc_number):
        for acc in self.accounts:
            if acc.acc_number == acc_number:
                return acc
        return None

    def check_balance(self, acc_number):
        acc = self.find_account(acc_number)
        if acc:
            print(f"Balance for account {acc_number}: {acc.balance}")
        else:
            print("Account not found.")

    def deposit_money(self, acc_number, amount):
        acc = self.find_account(acc_number)
        if acc:
            acc.deposit(amount)
        else:
            print("Account not found.")

    def withdraw_money(self, acc_number, amount):
        acc = self.find_account(acc_number)
        if acc:
            acc.withdraw(amount)
        else:
            print("Account not found.")

    def transfer_money(self, from_acc_number, to_acc_number, amount):
        from_acc = self.find_account(from_acc_number)
        to_acc = self.find_account(to_acc_number)
        if from_acc and to_acc:
            if from_acc.balance >= amount:
                from_acc.withdraw(amount)
                to_acc.deposit(amount)
                print(f"{amount} transferred from {from_acc_number} to {to_acc_number}.")
            else:
                print("Transfer failed. Insufficient funds.")
        else:
            print("One or both accounts not found.")

    def display_account_details(self, acc_number):
        acc = self.find_account(acc_number)
        if acc:
            acc.display()
        else:
            print("Account not found.")
def main():
    bank = Bank()

    while True:
        print("\n--- Banking System Menu ---")
        print("1. Add Account")
        print("2. Check Balance")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Transfer Money")
        print("6. Display Account Details")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            acc_number = input("Enter account number: ")
            holder_name = input("Enter account holder name: ")
            balance = float(input("Enter initial balance: "))
            acc = Account(acc_number, holder_name, balance)
            bank.add_account(acc)

        elif choice == '2':
            acc_number = input("Enter account number: ")
            bank.check_balance(acc_number)

        elif choice == '3':
            acc_number = input("Enter account number: ")
            amount = float(input("Enter amount to deposit: "))
            bank.deposit_money(acc_number, amount)

        elif choice == '4':
            acc_number = input("Enter account number: ")
            amount = float(input("Enter amount to withdraw: "))
            bank.withdraw_money(acc_number, amount)

        elif choice == '5':
            from_acc = input("Enter sender account number: ")
            to_acc = input("Enter receiver account number: ")
            amount = float(input("Enter amount to transfer: "))
            bank.transfer_money(from_acc, to_acc, amount)

        elif choice == '6':
            acc_number = input("Enter account number: ")
            bank.display_account_details(acc_number)

        elif choice == '7':
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 7.")
if __name__ == "__main__":
    main()





