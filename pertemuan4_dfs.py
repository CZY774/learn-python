# Fungsi untuk menambahkan edge ke dalam graf
def tambah_edge(graf, awal, tujuan):
    if awal not in graf:
        graf[awal] = []
    if tujuan not in graf:
        graf[tujuan] = []
    graf[awal].append(tujuan)
    graf[tujuan].append(awal)  # Karena graf tidak berarah

# Fungsi rekursif untuk melakukan DFS
def dfs_rekursif(graf, node, dikunjungi):
    # Tandai node saat ini sebagai dikunjungi
    dikunjungi[node] = True
    print(node, end=' ')
    # Kunjungi semua tetangga yang belum dikunjungi
    for tetangga in graf[node]:
        if tetangga not in dikunjungi or not dikunjungi[tetangga]:
            dfs_rekursif(graf, tetangga, dikunjungi)

# Fungsi utama untuk memulai DFS
def dfs(graf, mulai):
    # Inisialisasi semua node sebagai belum dikunjungi
    dikunjungi = {node: False for node in graf}
    
    # Panggil fungsi rekursif DFS
    dfs_rekursif(graf, mulai, dikunjungi)

# Program utama
if __name__ == "__main__":
    # Buat graf dalam bentuk dictionary
    graf = {
        0: [1, 3, 2],
        1: [0, 3],
        3: [0, 1, 4, 5, 2],
        2: [0, 3, 5, 6],
        4: [3, 8, 7, 5],
        5: [3, 2, 4, 6, 7],
        6: [2, 5, 7, 8],
        7: [4, 5, 6, 8],
        8: [4, 6, 7]
    }

    print("Hasil DFS dimulai dari node 0:")
    dfs(graf, 0)
