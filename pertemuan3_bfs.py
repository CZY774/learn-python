from collections import deque

# Fungsi untuk melakukan BFS
def bfs(graf, mulai):
    # Buat antrian untuk BFS
    antrian = deque()
    
    # Inisialisasi set untuk melacak node yang sudah dikunjungi
    dikunjungi = set()
    
    # Tandai node awal sebagai dikunjungi dan masukkan ke antrian
    dikunjungi.add(mulai)
    antrian.append(mulai)
    
    print("Hasil BFS:", end=" ")
    
    # Lakukan BFS
    while antrian:
        # Keluarkan node dari depan antrian dan cetak
        node = antrian.popleft()
        print(node, end=" ")
        
        # Cek semua tetangga node yang dikeluarkan
        for tetangga in graf[node]:
            # Jika tetangga belum dikunjungi, tandai sebagai dikunjungi
            # dan masukkan ke antrian
            if tetangga not in dikunjungi:
                dikunjungi.add(tetangga)
                antrian.append(tetangga)

# Fungsi untuk menambahkan edge ke graf
def tambah_edge(graf, awal, tujuan):
    graf[awal].append(tujuan)
    graf[tujuan].append(awal)  # Karena graf tidak berarah

# Program utama
if __name__ == "__main__":
    # Buat graf dalam bentuk dictionary
    graf = {
        0: [1, 2],
        1: [0, 3, 4],
        2: [0, 5],
        3: [1],
        4: [1, 5],
        5: [2, 4]
    }
    
    # Lakukan traversal BFS mulai dari vertex 0
    print("BFS dimulai dari vertex 0:")
    bfs(graf, 0)
