from pertemuan6_ClassDosen import Dosen  # Mengimpor class Dosen dari file dosen.py

class Mahasiswa:
    """
    Class Mahasiswa merepresentasikan seorang mahasiswa dalam sistem akademik.
    
    Class ini menyimpan informasi dasar tentang mahasiswa seperti nama, NIM, 
    dan jurusan, serta menyediakan metode untuk mengelola nilai-nilai 
    mata kuliah mahasiswa tersebut.

    Attributes:
        nama (str): Nama lengkap mahasiswa
        nim (str): Nomor Induk Mahasiswa
        jurusan (str): Jurusan atau program studi mahasiswa
        nilai (dict): Dictionary untuk menyimpan nilai mata kuliah
    """

    def __init__(self, nama, nim, jurusan):
        """
        Menginisialisasi instance baru dari class Mahasiswa.

        Args:
            nama (str): Nama lengkap mahasiswa
            nim (str): Nomor Induk Mahasiswa
            jurusan (str): Jurusan atau program studi mahasiswa
        """
        self.nama = nama        # Menyimpan nama mahasiswa
        self.nim = nim          # Menyimpan NIM (Nomor Induk Mahasiswa)
        self.jurusan = jurusan  # Menyimpan jurusan mahasiswa
        self.nilai = {}         # Dictionary kosong untuk menyimpan nilai mata kuliah

    def tambah_nilai(self, mata_kuliah, nilai):
        """
        Menambahkan atau memperbarui nilai untuk suatu mata kuliah.

        Args:
            mata_kuliah (str): Nama mata kuliah
            nilai (int/float): Nilai untuk mata kuliah tersebut

        Returns:
            None
        """
        self.nilai[mata_kuliah] = nilai
        print(f"Nilai {mata_kuliah} berhasil ditambahkan")

    def lihat_nilai(self):
        """
        Menampilkan semua nilai yang dimiliki mahasiswa.

        Returns:
            str: String yang berisi daftar nilai mahasiswa atau pesan jika belum ada nilai
        """
        if not self.nilai:
            return "Belum ada nilai yang diinput"
        
        return f"Nilai {self.nama} ({self.nim}):\n" + \
               "\n".join([f"{mk}: {nilai}" for mk, nilai in self.nilai.items()])

    def info(self):
        """
        Menampilkan informasi lengkap tentang mahasiswa.

        Returns:
            str: String yang berisi informasi dasar mahasiswa
        """
        return f"Nama: {self.nama}\nNIM: {self.nim}\nJurusan: {self.jurusan}"


# Contoh penggunaan class Mahasiswa dan Dosen
if __name__ == "__main__":
    # Membuat objek dosen
    dosen_ai = Dosen("Dr. Ahmad Wijaya", "98765", "Kecerdasan Buatan")
    
    # Menambahkan mata kuliah yang diampu dosen
    dosen_ai.tambah_matkul("Kecerdasan Buatan")
    print(dosen_ai.info())
    print(dosen_ai.lihat_matkul())
    print("\n" + "="*20 + "\n")  # Pembatas
    
    # Membuat objek mahasiswa
    mhs1 = Mahasiswa("Budi Santoso", "12345", "Teknik Informatika")
    
    # Menampilkan informasi mahasiswa
    print(mhs1.info())
    print("\n" + "="*20 + "\n")  # Pembatas
    
    # Menambahkan nilai untuk mata kuliah yang diampu dosen AI
    mhs1.tambah_nilai("Kecerdasan Buatan", 85)
    
    # Melihat nilai
    print(mhs1.lihat_nilai())