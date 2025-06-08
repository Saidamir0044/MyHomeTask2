# Ex1
try:
    num = int(input('Son kiriting: '))
    result = num % 0
    print("Natija:", result)
except ZeroDivisionError:
    print("Xatolik: Nolga bo‘lish mumkin emas!")

# Ex2
user_input = input("Iltimos, butun son kiriting: ")

try:
    # Kiritilgan qiymatni butun songa o‘girishga harakat qilamiz
    num = int(user_input)
    print("Siz kiritgan son:", num)
except ValueError:
    # Agar xato bo‘lsa, uni ataylab ko‘taramiz
    raise ValueError("Xatolik: Siz butun son kiritmadingiz!")

# Ex3
filename = input("Ochmoqchi bo‘lgan fayl nomini kiriting: ")

try:
    with open(filename, 'r') as file:
        content = file.read()
        print("Fayl mazmuni:")
        print(content)
except FileNotFoundError:
    print(f"Xatolik: '{filename}' nomli fayl topilmadi.")
# Ex4
num1 = input("1-sonni kiriting: ")
num2 = input("2-sonni kiriting: ")

try:
    num1 = float(num1)
    num2 = float(num2)

    print(f"Kiritilgan sonlar: {num1} va {num2}")
except ValueError:
    raise TypeError("Xatolik: Faqat raqamli qiymat kiriting (butun yoki haqiqiy son).")

# Ex5
filename = input("Ochmoqchi bo‘lgan fayl nomini kiriting: ")

try:
    with open(filename, 'r') as file:
        content = file.read()
        print("Fayl mazmuni:")
        print(content)
except PermissionError:
    print(f"Xatolik: '{filename}' faylini o‘qish uchun ruxsat yo‘q.")

# Ex6
my_list = [10, 20, 30, 40, 50]

try:
    index = int(input("Qaysi indeksdagi elementni ko‘rmoqchisiz (0–4): "))
    print(f"Tanlangan element: {my_list[index]}")
except IndexError:
    print("Xatolik: Siz mavjud bo‘lmagan indeksni kiritdingiz.")
except ValueError:
    print("Xatolik: Iltimos, faqat butun son kiriting.")

# Ex7
try:
    number = int(input("Iltimos, biror son kiriting: "))
    print(f"Siz kiritgan son: {number}")
except KeyboardInterrupt:
    print("\nXatolik: Kiritish bekor qilindi (KeyboardInterrupt).")
except ValueError:
    print("Xatolik: Iltimos, faqat butun son kiriting.")

# Ex8
try:
    a = float(input("Birinchi sonni kiriting: "))
    b = float(input("Ikkinchi sonni kiriting (bo‘luvchi): "))
    result = a / b
    print(f"Natija: {result}")
except ArithmeticError:
    print("Xatolik: Arifmetik xato yuz berdi (masalan, nolga bo‘lish).")
except ValueError:
    print("Xatolik: Iltimos, faqat son kiriting.")

# Ex9
filename = input("Ochmoqchi bo‘lgan fayl nomini kiriting: ")

try:
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
        print("Fayl mazmuni:")
        print(content)
except UnicodeDecodeError:
    print(f"Xatolik: '{filename}' faylini UTF-8 formatida o‘qib bo‘lmadi. Kodlash muammosi mavjud.")
except FileNotFoundError:
    print(f"Xatolik: '{filename}' nomli fayl topilmadi.")

# Ex10
my_list = [1, 2, 3, 4, 5]

try:
    # Ro‘yxatda mavjud bo‘lmagan metodga murojaat qilamiz
    my_list.push(6)
except AttributeError:
    print("Xatolik: 'list' obyektida mavjud bo‘lmagan atribut yoki metod chaqirildi.")

import os
import random
import string
from collections import Counter, deque
import glob

FILENAME = "example.txt"

def read_entire_file():
    with open(FILENAME, "r") as file:
        print(file.read())

def read_first_n_lines(n):
    with open(FILENAME, "r") as file:
        for _ in range(n):
            print(file.readline().strip())

def append_text_and_display(text):
    with open(FILENAME, "a") as file:
        file.write(f"\n{text}")
    read_entire_file()

def read_last_n_lines(n):
    with open(FILENAME, "r") as file:
        last_lines = deque(file, n)
        for line in last_lines:
            print(line.strip())

def store_lines_into_list():
    with open(FILENAME, "r") as file:
        return file.readlines()

def store_lines_into_variable():
    with open(FILENAME, "r") as file:
        return ''.join(file.readlines())

def store_lines_into_array():
    with open(FILENAME, "r") as file:
        return [line.strip() for line in file]

def find_longest_words():
    with open(FILENAME, "r") as file:
        words = file.read().split()
        max_len = max(len(word) for word in words)
        longest = [word for word in words if len(word) == max_len]
        print(longest)

def count_lines():
    with open(FILENAME, "r") as file:
        print(f"Total lines: {sum(1 for _ in file)}")

def count_word_frequency():
    with open(FILENAME, "r") as file:
        words = file.read().replace(",", " ").split()
        freq = Counter(words)
        print(freq)

def get_file_size():
    print(f"Size: {os.path.getsize(FILENAME)} bytes")

def write_list_to_file():
    data = ["Line 1", "Line 2", "Line 3"]
    with open("output.txt", "w") as file:
        for item in data:
            file.write(f"{item}\n")

def copy_file():
    with open(FILENAME, "r") as src, open("copy.txt", "w") as dst:
        dst.write(src.read())

def combine_lines(file1, file2, output_file):
    with open(file1) as f1, open(file2) as f2, open(output_file, "w") as out:
        for l1, l2 in zip(f1, f2):
            out.write(l1.strip() + " " + l2)

def read_random_line():
    with open(FILENAME) as file:
        lines = file.readlines()
        print(random.choice(lines).strip())

def check_file_closed():
    file = open(FILENAME, "r")
    print("Closed?", file.closed)
    file.close()
    print("Closed?", file.closed)

def remove_newlines():
    with open(FILENAME, "r") as file:
        print(file.read().replace("\n", ""))

def count_words_comma_separated():
    with open(FILENAME, "r") as file:
        text = file.read().replace(",", " ")
        words = text.split()
        print(f"Word count: {len(words)}")

def extract_characters_from_all_files():
    chars = []
    for filename in glob.glob("*.txt"):
        with open(filename, "r") as file:
            chars.extend(list(file.read()))
    print(chars)

def generate_a_to_z_files():
    for letter in string.ascii_uppercase:
        with open(f"{letter}.txt", "w") as file:
            file.write(f"This is file {letter}.txt\n")

def create_alphabet_file(letters_per_line=5):
    alphabet = string.ascii_lowercase
    with open("alphabet.txt", "w") as file:
        for i in range(0, len(alphabet), letters_per_line):
            file.write(alphabet[i:i+letters_per_line] + "\n")

# === Demo/Testing Section ===
if __name__ == "__main__":
    print("\n1. Entire File Content:")
    read_entire_file()

    print("\n2. First 3 Lines:")
    read_first_n_lines(3)

    print("\n3. Append Text and Display:")
    append_text_and_display("New appended line.")

    print("\n4. Last 3 Lines:")
    read_last_n_lines(3)

    print("\n5. Store Lines into List:")
    print(store_lines_into_list())

    print("\n6. Store Lines into Variable:")
    print(store_lines_into_variable())

    print("\n7. Store Lines into Array:")
    print(store_lines_into_array())

    print("\n8. Longest Words:")
    find_longest_words()

    print("\n9. Line Count:")
    count_lines()

    print("\n10. Word Frequency:")
    count_word_frequency()

    print("\n11. File Size:")
    get_file_size()

    print("\n12. Write List to File:")
    write_list_to_file()

    print("\n13. Copy File Content:")
    copy_file()

    print("\n14. Combine Lines From Two Files:")
    combine_lines("example.txt", "output.txt", "combined.txt")

    print("\n15. Read Random Line:")
    read_random_line()

    print("\n16. File Closed Check:")
    check_file_closed()

    print("\n17. Remove Newlines:")
    remove_newlines()

    print("\n18. Word Count With Commas:")
    count_words_comma_separated()

    print("\n19. Extract Characters From All .txt Files:")
    extract_characters_from_all_files()

    print("\n20. Generate A.txt to Z.txt:")
    generate_a_to_z_files()

    print("\n21. Create Alphabet File with 5 Letters per Line:")
    create_alphabet_file(5)





