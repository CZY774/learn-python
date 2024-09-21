"""
Input Output, Percabangan, dan Perulangan

Di Python, kita menggunakan fungsi print() untuk menampilkan output,
tidak seperti di C/C++ yang menggunakan printf() atau cout.
Untuk input, kita menggunakan fungsi input().

Docstring ini memberikan gambaran umum tentang isi modul.
"""

# 1. Input dan Output
print("1. Input dan Output")

# Input: Menggunakan fungsi input()
nama = input("Masukkan nama Anda: ")

# Output: Print biasa
print("Halo,", nama)

# Output: Print formatting
umur = 20
print(f"Nama saya {nama} dan umur saya {umur} tahun")

print("\n" + "=" * 30 + "\n")

# 2. Percabangan
print("2. Percabangan")

nilai = int(input("Masukkan nilai Anda: "))

# Percabangan if-elif-else
if nilai >= 80:
    print("Nilai Anda A")
elif nilai >= 70:
    print("Nilai Anda B")
elif nilai >= 60:
    print("Nilai Anda C")
else:
    print("Nilai Anda D")

print("\n" + "=" * 30 + "\n")

# 3. Perulangan
print("3. Perulangan")

# For loop
print("For loop:")
for i in range(5):
    print(f"Iterasi ke-{i+1}")

# For loop dengan string
print("\nFor loop dengan string:")
for karakter in nama:
    print(karakter)

# For loop dengan list
print("\nFor loop dengan list:")
buah = ["apel", "jeruk", "mangga"]
for item in buah:
    print(item)

# For loop dengan range
print("\nFor loop dengan range:")
for angka in range(1, 6):
    print(angka)

# While loop
print("\nWhile loop:")
counter = 0
while counter < 5:
    print(f"Counter: {counter}")
    counter += 1

# While-else loop
print("\nWhile-else loop:")
angka = 0
while angka < 3:
    print(f"Angka: {angka}")
    angka += 1
else:
    print("Loop selesai!")

"""
Alur Program:
1. Program dimulai dengan input dan output dasar.
2. Kemudian, program mendemonstrasikan percabangan dengan if-elif-else.
3. Terakhir, program menunjukkan berbagai jenis perulangan dalam Python.

Setiap bagian dipisahkan dengan garis pemisah untuk memudahkan pembacaan.
Komentar ditambahkan untuk menjelaskan setiap bagian dan fungsi kode.
"""