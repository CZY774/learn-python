"""
Pengenalan Tipe Data dan Fungsi di Python

Deskripsi:
    Modul ini mendemonstrasikan penggunaan berbagai tipe data di Python
    (numerik, string, list, tuple, dictionary, set) serta penggunaan
    fungsi dan parameter. Modul ini juga menunjukkan cara memberikan
    komentar dan docstring.

Alur Program:
    1. Mendemonstrasikan tipe data numerik
    2. Mendemonstrasikan tipe data string
    3. Mendemonstrasikan tipe data list
    4. Mendemonstrasikan tipe data tuple
    5. Mendemonstrasikan tipe data dictionary
    6. Mendemonstrasikan tipe data set
    7. Mendemonstrasikan penggunaan fungsi dan parameter
    
Perbedaan dengan C/C++:
    - Python menggunakan indentasi untuk blok kode, bukan kurung kurawal {}
    - Tipe data tidak perlu dideklarasikan secara eksplisit
    - Python memiliki tipe data dinamis
    - List di Python mirip dengan array di C/C++, tapi lebih fleksibel
    - Dictionary di Python mirip dengan struct atau map di C++
    - Set adalah tipe data unik di Python yang tidak ada di C/C++
"""

# Tipe data numerik
angka_bulat = 10  # Integer
angka_desimal = 3.14  # Float

print("Tipe data numerik:")
print(f"Integer: {angka_bulat}")
print(f"Float: {angka_desimal}")

# Tipe data string
nama = "Budi"  # String
alamat = 'Jalan Merdeka No. 17'  # String bisa menggunakan tanda petik tunggal atau ganda

print("\nTipe data string:")
print(f"Nama: {nama}")
print(f"Alamat: {alamat}")

# Tipe data list
buah = ["apel", "jeruk", "mangga"]  # List bisa diubah (mutable)

print("\nTipe data list:")
print(f"Daftar buah: {buah}")
print(f"Buah pertama: {buah[0]}")  # Mengakses elemen list dengan indeks

# Tipe data tuple
koordinat = (3, 4)  # Tuple tidak bisa diubah (immutable)

print("\nTipe data tuple:")
print(f"Koordinat: {koordinat}")
print(f"Nilai x: {koordinat[0]}, Nilai y: {koordinat[1]}")

# Tipe data dictionary
mahasiswa = {
    "nama": "Ani",
    "umur": 20,
    "jurusan": "Teknik Informatika"
}  # Dictionary menyimpan pasangan key-value

print("\nTipe data dictionary:")
print(f"Data mahasiswa: {mahasiswa}")
print(f"Nama: {mahasiswa['nama']}")  # Mengakses value dengan key

# Tipe data set
warna = {"merah", "hijau", "biru"}  # Set menyimpan nilai unik tanpa urutan

print("\nTipe data set:")
print(f"Warna: {warna}")
warna.add("kuning")  # Menambahkan elemen ke set
print(f"Warna setelah ditambah: {warna}")

# Fungsi dan parameter
def sapa(nama, pesan="Selamat datang"):
    """
    Fungsi untuk menyapa seseorang.
    
    Args:
        nama (str): Nama orang yang disapa
        pesan (str, optional): Pesan sapaan. Default: "Selamat datang"
    
    Returns:
        str: Sapaan lengkap
    """
    return f"{pesan}, {nama}!"

# Memanggil fungsi
print("\nPenggunaan fungsi:")
print(sapa("Dini"))  # Menggunakan parameter default
print(sapa("Eko", "Halo"))  # Mengubah parameter kedua

# Contoh komentar satu baris

"""
Ini adalah contoh komentar multi-baris atau docstring.
Docstring biasanya digunakan untuk menjelaskan fungsi, kelas, atau modul.
"""