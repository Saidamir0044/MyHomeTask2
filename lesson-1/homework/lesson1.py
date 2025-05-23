
import math

# 1. Kvadratning perimetri va yuzasi
side = float(input("Kvadratning tomonini kiriting: "))
perimeter = 4 * side
area = side ** 2
print(f"Kvadratning perimetri: {perimeter}")
print(f"Kvadratning yuzasi: {area}")

# 2. Aylananing diametridan uzunligi (uzunligi = π * d)
diameter = float(input("Aylananing diametrini kiriting: "))
circle_length = math.pi * diameter
print(f"Aylananing uzunligi: {circle_length:.2f}")

# 3. Ikki sonning o‘rta arifmetigi
a = float(input("Birinchi sonni kiriting (a): "))
b = float(input("Ikkinchi sonni kiriting (b): "))
mean = (a + b) / 2
print(f"{a} va {b} sonlarining o‘rtacha qiymati: {mean}")

# 4. Ikki sonning yig‘indisi, ko‘paytmasi va har birining kvadrati
sum_ab = a + b
product_ab = a * b
square_a = a ** 2
square_b = b ** 2

print(f"Yig‘indi: {sum_ab}")
print(f"Ko‘paytma: {product_ab}")
print(f"a ning kvadrati: {square_a}")
print(f"b ning kvadrati: {square_b}")

