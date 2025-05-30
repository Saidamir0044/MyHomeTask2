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




