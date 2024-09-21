# Mengimpor seluruh module pertemuan3_math_ops
import pertemuan3_math_ops

# Menggunakan fungsi dari pertemuan3_math_ops dengan cara memanggil nama modulnya
hasil_tambah = pertemuan3_math_ops.tambah(5, 3)
print(f"Hasil penjumlahan: {hasil_tambah}")

# Mengimpor hanya fungsi tambah dan bagi dari module pertemuan3_math_ops
# Untuk menghindari konflik nama fungsi yang sama, kita bisa menggunakan 'as' untuk memberi alias
from pertemuan3_math_ops import tambah as sum_op, bagi as div_op

# Menggunakan fungsi yang di-import dengan alias
hasil_bagi = div_op(10, 2)
print(f"Hasil pembagian: {hasil_bagi}")

# Menggunakan fungsi yang di-import dengan alias untuk penjumlahan
hasil_penjumlahan = sum_op(7, 2)
print(f"Hasil penjumlahan dengan alias: {hasil_penjumlahan}")

# Penjelasan alur program:
# 1. Pada bagian pertama, kita mengimpor seluruh module pertemuan3_math_ops menggunakan `import pertemuan3_math_ops`.
#    Semua fungsi di dalam module tersebut bisa digunakan dengan format `pertemuan3_math_ops.nama_fungsi()`.
# 2. Pada bagian kedua, kita menggunakan `from ... import ...` untuk hanya mengimpor
#    fungsi tertentu, yaitu `tambah` dan `bagi`, dan memberikan alias menggunakan `as`.
#    Ini berguna jika ada kemungkinan nama fungsi yang sama di berbagai module.