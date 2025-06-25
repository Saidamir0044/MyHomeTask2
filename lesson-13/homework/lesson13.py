# Age Calculator: Ask the user to enter their birthdate. 
# Calculate and print their age in years, months, and days.

# Ex1
import datetime

date_str = input("Tug'ilgan sanangizni kiriting (dd-mm-yyyy formatda): ")

birth_date = datetime.datetime.strptime(date_str, "%d-%m-%Y").date()

today = datetime.date.today()

years = today.year - birth_date.year
months = today.month - birth_date.month
days = today.day - birth_date.day

if days < 0:
    months -= 1
    previous_month = (today.month - 1) if today.month > 1 else 12
    previous_year = today.year if today.month > 1 else today.year - 1
    days += (datetime.date(previous_year, previous_month + 1, 1) - datetime.date(previous_year, previous_month, 1)).days

if months < 0:
    years -= 1
    months += 12

# Natijani chiqaramiz
print(f"Sizning yoshingiz: {years} yil, {months} oy, {days} kun.")




# Days Until Next Birthday: Similar to the first exercise, but this time, 
# calculate and print the number of days remaining until the user's next birthday.

# Ex2

import datetime

date_str = input("Tug'ilgan sanangizni kiriting (dd-mm-yyyy formatda): ")
birth_date = datetime.datetime.strptime(date_str, "%d-%m-%Y").date()

today = datetime.date.today()

this_year_birthday = datetime.date(today.year, birth_date.month, birth_date.day)

if this_year_birthday < today:
    next_birthday = datetime.date(today.year + 1, birth_date.month, birth_date.day)
else:
    next_birthday = this_year_birthday

days_remaining = (next_birthday - today).days

print(f"Sizning navbatdagi tug‘ilgan kuningizgacha {days_remaining} kun qoldi.")



# Meeting Scheduler: Ask the user to enter the current date and time, 
# as well as the duration of a meeting in hours and minutes. 
# Calculate and print the date and time when the meeting will end.

# Ex3
import datetime

date_str = input("Uchrashuv boshlanish vaqtini kiriting (dd-mm-yyyy: HH-MM formatida): ")
meet_str = input("Uchrashuv davomiyligini kiriting (HH:MM formatida): ")

start_time = datetime.datetime.strptime(date_str, "%d-%m-%Y: %H-%M")

duration = datetime.datetime.strptime(meet_str, "%H:%M")
duration_hours = duration.hour
duration_minutes = duration.minute

meeting_end = start_time + datetime.timedelta(hours=duration_hours, minutes=duration_minutes)

print("Uchrashuv tugash vaqti:", meeting_end.strftime("%d-%m-%Y %H:%M"))



# Timezone Converter: Create a program that allows the user to enter a date and 
# time along with their current timezone, and then convert and print the date and 
# time in another timezone of their choice.

# Ex4

import datetime
import pytz

date_str = input("Sanani kiriting (dd-mm-yyyy HH:MM formatda): ")
from_timezone = input("Joriy vaqt zonangizni kiriting (masalan, Asia/Tashkent): ")
to_timezone = input("Qaysi vaqt zonasiga o‘tkazmoqchisiz? (masalan, US/Eastern): ")

local_dt = datetime.datetime.strptime(date_str, "%d-%m-%Y %H:%M")

from_tz = pytz.timezone(from_timezone)
local_dt = from_tz.localize(local_dt)

to_tz = pytz.timezone(to_timezone)
converted_dt = local_dt.astimezone(to_tz)

print("Konvertatsiya qilingan vaqt:", converted_dt.strftime("%d-%m-%Y %H:%M (%Z)"))



# Countdown Timer: Implement a countdown timer. Ask the user to input a future date and time,
#  and then continuously print the time remaining until that point in regular intervals (e.g., every second).

# Ex5
import datetime, time 


date_str = input("Vaqtni kiriting (dd-mm-yyyy HH:MM:SS formatda): ")
future_time = datetime.datetime.strptime(date_str, "%d-%m-%Y %H:%M:%S")

while True:
    current_time = datetime.datetime.now()
    remaining_time = future_time - current_time

    if remaining_time.total_seconds() <= 0:
        print("Countdown tugadi!")
        break

    days = remaining_time.days
    hours, remainder = divmod(remaining_time.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    print(f"Qolgan vaqt: {days} kun, {hours:02} soat, {minutes:02} minut, {seconds:02} sekund", end='\r')

    time.sleep(1)

# Email Validator: Write a program that validates email addresses. 
# Ask the user to input an email address,
#  and check if it follows a valid email format.

# Ex6
import re

pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

while True:
    mail_add = input("E-mailingizni kiriting: ")
    if re.match(pattern, mail_add):
        print(" Email manzili to‘g‘ri.")
        break
    else:
        print(" Noto‘g‘ri email manzili. Iltimos, qayta kiriting.")

# Phone Number Formatter: Create a program that takes a phone number as input and formats it according to 
# a standard format. For example, convert "1234567890" to "(123) 456-7890".

# Ex7
import re


phone = input("Telefon raqamingizni kiriting (faqat raqamlar, masalan: 1234567890): ")

cleaned = re.sub(r'\D', '', phone) 

if len(cleaned) == 10:
    formatted = f"({cleaned[:3]}) {cleaned[3:6]}-{cleaned[6:]}"
    print("Formatlangan raqam:", formatted)
else:
    print(" Telefon raqami noto‘g‘ri. Iltimos, 10 ta raqam kiriting.")


# Password Strength Checker: Implement a password strength checker. Ask the user to input a password and 
# check if it meets certain criteria (e.g., minimum length, contains at least one uppercase letter, 
# one lowercase letter, and one digit).

# Ex8

import re


password = input("Parolingizni kiriting: ")


length_ok = len(password) >= 8
uppercase_ok = re.search(r'[A-Z]', password) is not None
lowercase_ok = re.search(r'[a-z]', password) is not None
digit_ok = re.search(r'\d', password) is not None


if length_ok and uppercase_ok and lowercase_ok and digit_ok:
    print(" Kuchli parol!")
else:
    print(" Parol quyidagi shartlarga javob berishi kerak:")
    if not length_ok:
        print("- Kamida 8 ta belgi bo‘lishi kerak")
    if not uppercase_ok:
        print("- Kamida 1 ta katta harf bo‘lishi kerak (A–Z)")
    if not lowercase_ok:
        print("- Kamida 1 ta kichik harf bo‘lishi kerak (a–z)")
    if not digit_ok:
        print("- Kamida 1 ta raqam bo‘lishi kerak (0–9)")

# Word Finder: Develop a program that finds all occurrences of a specific word in a given text.
#  Ask the user to input a word, and then search for and print all occurrences of that word in a sample text.

# Ex9

import re


# Misol matn (siz buni fayldan yoki foydalanuvchidan ham olishingiz mumkin)
sample_text = """
Python is a powerful programming language. Python is easy to learn. 
Many developers love Python because of its simplicity and readability.
"""

# Foydalanuvchidan qidirilayotgan so‘zni olish
word = input("Qidiriladigan so‘zni kiriting: ")

# So‘zlarni indexlar bilan qidirish (katta-kichik harflarni farqlamaydi)
matches = [(m.start(), m.end()) for m in re.finditer(rf'\b{re.escape(word)}\b', sample_text, flags=re.IGNORECASE)]

# Natijani chiqarish
if matches:
    print(f" '{word}' so‘zi {len(matches)} marta topildi:")
    for i, (start, end) in enumerate(matches, 1):
        print(f"{i}. Pozitsiya: {start} - {end}, So‘z: '{sample_text[start:end]}'")
else:
    print(f"'{word}' so‘zi matnda topilmadi.")

# Date Extractor: Write a program that extracts dates from a given text. Ask the user to input a text,
#  and then identify and print all the dates present in the text.

import re

# Matn olish
text = input("Matnni kiriting (ichida sanalar bo'lishi mumkin): ")

# Sana formatlari uchun regex andozalar
date_patterns = [
    r'\b\d{2}-\d{2}-\d{4}\b',     # dd-mm-yyyy
    r'\b\d{2}/\d{2}/\d{4}\b',     # dd/mm/yyyy
    r'\b\d{4}-\d{2}-\d{2}\b',     # yyyy-mm-dd
    r'\b\d{2}\.\d{2}\.\d{4}\b'    # dd.mm.yyyy
]

# Barcha mos keluvchi sanalarni to‘plash
found_dates = []
for pattern in date_patterns:
    found_dates.extend(re.findall(pattern, text))

# Natijani chiqarish
if found_dates:
    print(f" Matndan topilgan sanalar ({len(found_dates)} ta):")
    for i, date in enumerate(found_dates, 1):
        print(f"{i}. {date}")
else:
    print(" Hech qanday sana topilmadi.")
