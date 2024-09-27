from collections import deque

# Fungsi untuk melakukan BFS
def bfs(graf, mulai):
    # Buat antrian untuk BFS
    antrian = deque()
    
    # Inisialisasi semua node sebagai belum dikunjungi
    dikunjungi = [False] * len(graf)
    
    # Tandai node awal sebagai dikunjungi dan masukkan ke antrian
    dikunjungi[mulai] = True
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
            if not dikunjungi[tetangga]:
                dikunjungi[tetangga] = True
                antrian.append(tetangga)

# Fungsi untuk menambahkan edge ke graf
def tambah_edge(graf, awal, tujuan):
    graf[awal].append(tujuan)
    graf[tujuan].append(awal)  # Karena graf tidak berarah

# Program utama
if __name__ == "__main__":
    # Jumlah vertex dalam graf
    jumlah_vertex = 5
    
    # Representasi graf menggunakan list of lists
    graf = [[] for _ in range(jumlah_vertex)]
    
    # Tambahkan edge ke graf
    tambah_edge(graf, 0, 1)
    tambah_edge(graf, 0, 2)
    tambah_edge(graf, 1, 3)
    tambah_edge(graf, 1, 4)
    tambah_edge(graf, 2, 4)
    
    # Lakukan traversal BFS mulai dari vertex 0
    print("BFS dimulai dari vertex 0:")
    bfs(graf, 0)
