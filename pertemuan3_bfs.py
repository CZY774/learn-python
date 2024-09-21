from collections import deque

def bfs_v1(graf, mulai, tujuan):
    """
    BFS menggunakan queue untuk mencari jalur.
    
    Alur:
    1. Inisialisasi queue dengan node awal
    2. Selama queue tidak kosong:
       a. Ambil node dari depan queue
       b. Jika node adalah tujuan, kembalikan jalur
       c. Jelajahi tetangga yang belum dikunjungi
       d. Tambahkan tetangga ke queue
    3. Jika tujuan tidak ditemukan, kembalikan None
    """
    antrian = deque([[mulai]])  # Inisialisasi antrian dengan jalur awal
    dikunjungi = set([mulai])   # Set untuk melacak node yang sudah dikunjungi

    while antrian:
        jalur = antrian.popleft()  # Ambil jalur pertama dari antrian
        node = jalur[-1]           # Ambil node terakhir dari jalur

        if node == tujuan:
            return jalur  # Kembalikan jalur jika tujuan ditemukan

        for tetangga in graf[node]:
            if tetangga not in dikunjungi:
                antrian.append(jalur + [tetangga])  # Tambahkan jalur baru ke antrian
                dikunjungi.add(tetangga)            # Tandai tetangga sebagai dikunjungi

    return None  # Kembalikan None jika tujuan tidak ditemukan

def bfs_v2(graf, mulai, tujuan):
    """
    BFS menggunakan dua queue untuk level-order traversal.
    
    Alur:
    1. Inisialisasi dua queue: saat ini dan berikutnya
    2. Mulai dengan node awal di queue saat ini
    3. Selama queue saat ini tidak kosong:
       a. Proses semua node di level saat ini
       b. Jika tujuan ditemukan, kembalikan level
       c. Tambahkan tetangga ke queue berikutnya
    4. Tukar queue saat ini dan berikutnya, tingkatkan level
    5. Jika tujuan tidak ditemukan, kembalikan -1
    """
    if mulai == tujuan:
        return 0  # Jika mulai adalah tujuan, kembalikan level 0

    level = 0
    dikunjungi = set([mulai])
    saat_ini = deque([mulai])
    berikutnya = deque()

    while saat_ini:
        level += 1
        while saat_ini:
            node = saat_ini.popleft()
            for tetangga in graf[node]:
                if tetangga == tujuan:
                    return level  # Kembalikan level jika tujuan ditemukan
                if tetangga not in dikunjungi:
                    dikunjungi.add(tetangga)
                    berikutnya.append(tetangga)
        
        saat_ini, berikutnya = berikutnya, saat_ini  # Tukar queue

    return -1  # Kembalikan -1 jika tujuan tidak ditemukan

def bfs_v3(graf, mulai):
    """
    BFS untuk menemukan jarak terpendek ke semua node.
    
    Alur:
    1. Inisialisasi queue dengan node awal dan dictionary jarak
    2. Selama queue tidak kosong:
       a. Ambil node dari queue
       b. Untuk setiap tetangga yang belum dikunjungi:
          - Hitung jarak
          - Tambahkan ke queue
          - Catat jarak di dictionary
    3. Kembalikan dictionary jarak
    """
    jarak = {mulai: 0}  # Dictionary untuk menyimpan jarak ke setiap node
    antrian = deque([mulai])

    while antrian:
        node = antrian.popleft()
        for tetangga in graf[node]:
            if tetangga not in jarak:
                jarak[tetangga] = jarak[node] + 1
                antrian.append(tetangga)

    return jarak

# Contoh penggunaan
if __name__ == "__main__":
    graf = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }

    print("BFS v1 (Mencari Jalur):", bfs_v1(graf, 'A', 'F'))
    print("BFS v2 (Level Traversal):", bfs_v2(graf, 'A', 'F'))
    print("BFS v3 (Jarak ke Semua Node):", bfs_v3(graf, 'A'))