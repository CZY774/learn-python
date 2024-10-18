class Dosen:
    """
    Class Dosen merepresentasikan seorang dosen dalam sistem akademik.
    
    Class ini menyimpan informasi dasar tentang dosen seperti nama, NIP, 
    dan bidang keahlian, serta menyediakan metode untuk mengelola 
    mata kuliah yang diampu oleh dosen tersebut.

    Attributes:
        nama (str): Nama lengkap dosen
        nip (str): Nomor Induk Pegawai
        bidang (str): Bidang keahlian dosen
        matkul (list): List untuk menyimpan mata kuliah yang diampu
    """

    def __init__(self, nama, nip, bidang):
        """
        Menginisialisasi instance baru dari class Dosen.

        Args:
            nama (str): Nama lengkap dosen
            nip (str): Nomor Induk Pegawai
            bidang (str): Bidang keahlian dosen
        """
        self.nama = nama          # Menyimpan nama dosen
        self.nip = nip            # Menyimpan NIP (Nomor Induk Pegawai)
        self.bidang = bidang      # Menyimpan bidang keahlian
        self.matkul = []          # List kosong untuk menyimpan mata kuliah yang diampu

    def tambah_matkul(self, mata_kuliah):
        """
        Menambahkan mata kuliah baru ke daftar mata kuliah yang diampu.

        Args:
            mata_kuliah (str): Nama mata kuliah yang akan ditambahkan

        Returns:
            None
        """
        if mata_kuliah not in self.matkul:
            self.matkul.append(mata_kuliah)
            print(f"Mata kuliah {mata_kuliah} berhasil ditambahkan")
        else:
            print(f"Mata kuliah {mata_kuliah} sudah ada")

    def lihat_matkul(self):
        """
        Menampilkan semua mata kuliah yang diampu oleh dosen.

        Returns:
            str: String yang berisi daftar mata kuliah atau pesan jika belum ada mata kuliah
        """
        if not self.matkul:
            return "Belum ada mata kuliah yang diampu"
        
        return f"Mata kuliah yang diampu {self.nama}:\n" + \
               "\n".join([f"- {mk}" for mk in self.matkul])

    def info(self):
        """
        Menampilkan informasi lengkap tentang dosen.

        Returns:
            str: String yang berisi informasi dasar dosen
        """
        return f"Nama: {self.nama}\nNIP: {self.nip}\nBidang: {self.bidang}"