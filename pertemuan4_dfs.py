# Fungsi untuk menambahkan edge ke dalam graf
def tambah_edge(graf, awal, tujuan):
    graf[awal].append(tujuan)
    graf[tujuan].append(awal)  # Karena graf tidak berarah

# Fungsi rekursif untuk melakukan DFS
def dfs_rekursif(graf, node, dikunjungi):
    # Tandai node saat ini sebagai dikunjungi
    dikunjungi[node] = True
    print(node, end=' ')

    # Kunjungi semua tetangga yang belum dikunjungi
    for tetangga in graf[node]:
        if not dikunjungi[tetangga]:
            dfs_rekursif(graf, tetangga, dikunjungi)

# Fungsi utama untuk memulai DFS
def dfs(graf, mulai):
    # Inisialisasi semua node sebagai belum dikunjungi
    dikunjungi = [False] * len(graf)
    
    # Panggil fungsi rekursif DFS
    dfs_rekursif(graf, mulai, dikunjungi)

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

    print("Hasil DFS dimulai dari node 0:")
    dfs(graf, 0)
