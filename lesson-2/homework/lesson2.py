
# 1. Age Calculator
name = input("Ismingizni kiriting: ")
birth_year = int(input("Tug‘ilgan yilingizni kiriting: "))
current_year = 2025
age = current_year - birth_year
print(f"{name}, sizning yoshingiz: {age} yosh")

# 2. Extract Car Names (from 'LMaasleitbtui' -> 'Lambauti')
txt1 = 'LMaasleitbtui'
car1 = txt1[0] + txt1[2] + txt1[5] + txt1[6] + txt1[9] + txt1[11]
print("Extracted car name 1:", car1)

# 3. Extract Car Names (from 'MsaatmiazD' -> 'Mazda')
txt2 = 'MsaatmiazD'
car2 = txt2[0] + txt2[6] + txt2[7] + txt2[8] + txt2[9]
print("Extracted car name 2:", car2)

# 4. Extract Residence Area
txt3 = "I'am John. I am from London"
area = txt3.split("from")[-1].strip()
print("Residence area:", area)

# 5. Reverse String
user_input = input("So‘z kiriting: ")
print("Teskari:", user_input[::-1])

# 6. Count Vowels
vowels = "aeiouAEIOU"
text = input("Matn kiriting: ")
count = sum(1 for char in text if char in vowels)
print("Unli harflar soni:", count)

# 7. Find Maximum Value
nums = input("Sonlarni kiriting (vergul bilan): ")
num_list = [int(x) for x in nums.split(',')]
print("Eng katta son:", max(num_list))

# 8. Check Palindrome
word = input("So‘z kiriting: ")
if word == word[::-1]:
    print("Bu so‘z palindrom.")
else:
    print("Bu so‘z palindrom emas.")

# 9. Extract Email Domain
email = input("Email manzil kiriting: ")
domain = email.split('@')[-1]
print("Email domeni:", domain)

# 10. Generate Random Password
import random
import string
length = int(input("Parol uzunligini kiriting: "))
all_chars = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(all_chars) for _ in range(length))
print("Tasodifiy parol:", password)
