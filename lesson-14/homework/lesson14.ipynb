# Task1: JSON Parsing
# write a Python script that reads the students.jon JSON file and prints details of each student.

import json

students = [
    {"name": "Saidamir", "age": 23, "city": "Tashkent"},
    {"name": "Ali", "age": 21, "city": "Samarkand"},
    {"name": "Laylo", "age": 22, "city": "Bukhara"}
]

with open("students.json", "w") as file:
    json.dump(students, file, indent=4)

# Task2: Weather API
# Use this url : https://openweathermap.org/
# Use the requests library to fetch weather data for a specific city
# (ex. your hometown: Tashkent) and print relevant information (temperature, humidity, etc.).

import requests

API_KEY = "d7294576f1b442e190c362ab5c67c4ce"
city = "Tashkent"

# 🔧 TO‘G‘RI URL
url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"

response = requests.get(url)

if response.status_code == 200:
    try:
        data = response.json()
        print("✅ JSON olindi!")
        for forecast in data["list"][:3]:
            print(f"{forecast['dt_txt']} - {forecast['main']['temp']}°C - {forecast['weather'][0]['description']}")
    except ValueError:
        print("❌ JSON format emas!")
        print(response.text[:300])
else:
    print("❌ HTTP Xato:", response.status_code)
    print("Javob:", response.text[:300])

# Task3: JSON Modification
# Write a program that allows users to add new books, update existing book information, 
# and delete books from the books.json JSON file.

import json
import os

FILE_NAME = "books.json"

# Fayl mavjud bo'lmasa, bo'sh ro'yxat bilan yaratiladi
def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w") as f:
            json.dump([], f)

# Fayldan kitoblar ro'yxatini o'qish
def load_books():
    with open(FILE_NAME, "r") as f:
        return json.load(f)

# Kitoblar ro'yxatini faylga yozish
def save_books(books):
    with open(FILE_NAME, "w") as f:
        json.dump(books, f, indent=4)

# 📚 Yangi kitob qo‘shish
def add_book():
    books = load_books()
    new_id = max([book["id"] for book in books], default=0) + 1
    title = input("Kitob nomi: ")
    author = input("Muallifi: ")
    books.append({"id": new_id, "title": title, "author": author})
    save_books(books)
    print("✅ Kitob qo‘shildi!")

# ✏️ Kitobni yangilash
def update_book():
    books = load_books()
    book_id = int(input("Yangilamoqchi bo‘lgan kitob ID raqami: "))
    for book in books:
        if book["id"] == book_id:
            book["title"] = input("Yangi nom: ")
            book["author"] = input("Yangi muallif: ")
            save_books(books)
            print("✅ Kitob yangilandi!")
            return
    print("❌ Bunday ID bilan kitob topilmadi.")

# ❌ Kitobni o‘chirish
def delete_book():
    books = load_books()
    book_id = int(input("O‘chirmoqchi bo‘lgan kitob ID raqami: "))
    books = [book for book in books if book["id"] != book_id]
    save_books(books)
    print("✅ Kitob o‘chirildi!")

# 📋 Hamma kitoblarni ko‘rish
def list_books():
    books = load_books()
    if not books:
        print("📭 Hozircha kitoblar yo‘q.")
    else:
        for book in books:
            print(f"{book['id']}: {book['title']} - {book['author']}")

# 📌 Asosiy menyu
def menu():
    initialize_file()
    while True:
        print("\n📚 Kitoblar Boshqaruvi")
        print("1. Hamma kitoblarni ko‘rish")
        print("2. Yangi kitob qo‘shish")
        print("3. Kitobni yangilash")
        print("4. Kitobni o‘chirish")
        print("5. Chiqish")

        choice = input("Tanlang (1–5): ")
        if choice == "1":
            list_books()
        elif choice == "2":
            add_book()
        elif choice == "3":
            update_book()
        elif choice == "4":
            delete_book()
        elif choice == "5":
            print("🚪 Chiqildi.")
            break
        else:
            print("❌ Noto‘g‘ri tanlov.")

# 🔃 Dasturni ishga tushurish
if __name__ == "__main__":
    menu()



# Task: Movie Recommendation System
# Use this url http://www.omdbapi.com/ to fetch information about movies.
# Create a program that asks users for a movie genre and recommends a random movie from that genre.
import requests
import random

API_KEY = "adeeb098"  # O'zingiz ro'yxatdan o'tib olasiz
OMDB_URL = "http://www.omdbapi.com/"

# OMDb to'g'ridan-to'g'ri genre bo'yicha qidirish imkonini bermaydi,
# shuning uchun mashhur film nomlaridan foydalanamiz
seed_movies = [
    "Inception", "Titanic", "The Matrix", "The Godfather",
    "Pulp Fiction", "The Shawshank Redemption", "The Dark Knight",
    "Forrest Gump", "Gladiator", "Interstellar"
]

def get_random_movie_by_genre(genre):
    random.shuffle(seed_movies)  # har safar turlicha ketma-ketlik
    for title in seed_movies:
        params = {
            "apikey": API_KEY,
            "t": title
        }
        response = requests.get(OMDB_URL, params=params)
        if response.status_code == 200:
            data = response.json()
            if "Genre" in data and genre.lower() in data["Genre"].lower():
                return {
                    "Title": data["Title"],
                    "Year": data["Year"],
                    "Genre": data["Genre"],
                    "Plot": data.get("Plot", "No description.")
                }
    return None

# 🎬 Asosiy dastur
def main():
    genre = input("Qaysi janrdagi film kerak? (masalan: Action, Drama, Sci-Fi): ").strip()
    movie = get_random_movie_by_genre(genre)
    if movie:
        print("\n🎥 Sizga tavsiya etiladigan film:")
        print(f"📌 Nomi: {movie['Title']}")
        print(f"📅 Yili: {movie['Year']}")
        print(f"🎭 Janr: {movie['Genre']}")
        print(f"📖 Tavsif: {movie['Plot']}")
    else:
        print("❌ Afsuski, bu janrda film topilmadi.")

if __name__ == "__main__":
    main()
