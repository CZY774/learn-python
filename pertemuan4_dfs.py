def dfs_v1(graf, mulai, tujuan):
    """
    DFS menggunakan rekursi untuk mencari jalur.
    
    Alur:
    1. Mulai dari node awal
    2. Jika node saat ini adalah tujuan, kembalikan jalur
    3. Untuk setiap tetangga yang belum dikunjungi:
       a. Lakukan DFS rekursif
       b. Jika jalur ditemukan, tambahkan node saat ini dan kembalikan
    4. Jika tidak ada jalur ditemukan, kembalikan None
    """
    def dfs_rekursif(node, jalur):
        if node == tujuan:
            return jalur
        
        for tetangga in graf[node]:
            if tetangga not in dikunjungi:
                dikunjungi.add(tetangga)
                hasil = dfs_rekursif(tetangga, jalur + [tetangga])
                if hasil:
                    return hasil
        
        return None

    dikunjungi = set([mulai])
    return dfs_rekursif(mulai, [mulai])

def dfs_v2(graf, mulai, tujuan):
    """
    DFS menggunakan stack untuk mencari kedalaman.
    
    Alur:
    1. Inisialisasi stack dengan node awal dan kedalaman 0
    2. Selama stack tidak kosong:
       a. Ambil node dan kedalaman dari stack
       b. Jika node adalah tujuan, kembalikan kedalaman
       c. Jelajahi tetangga yang belum dikunjungi
       d. Tambahkan tetangga ke stack dengan kedalaman + 1
    3. Jika tujuan tidak ditemukan, kembalikan -1
    """
    if mulai == tujuan:
        return 0

    stack = [(mulai, 0)]
    dikunjungi = set([mulai])

    while stack:
        node, kedalaman = stack.pop()

        for tetangga in graf[node]:
            if tetangga == tujuan:
                return kedalaman + 1
            if tetangga not in dikunjungi:
                dikunjungi.add(tetangga)
                stack.append((tetangga, kedalaman + 1))

    return -1

def dfs_v3(graf, mulai):
    """
    DFS untuk menemukan waktu penemuan dan waktu selesai setiap node.
    
    Alur:
    1. Inisialisasi waktu global dan dictionary untuk waktu penemuan dan selesai
    2. Untuk setiap node yang belum dikunjungi:
       a. Panggil fungsi dfs_visit
    3. Dalam dfs_visit:
       a. Catat waktu penemuan
       b. Jelajahi semua tetangga yang belum dikunjungi secara rekursif
       c. Catat waktu selesai
    4. Kembalikan dictionary waktu penemuan dan selesai
    """
    waktu = 0
    dikunjungi = set()
    waktu_d = {}  # waktu penemuan
    waktu_f = {}  # waktu selesai

    def dfs_visit(node):
        nonlocal waktu
        waktu += 1
        waktu_d[node] = waktu
        dikunjungi.add(node)

        for tetangga in graf[node]:
            if tetangga not in dikunjungi:
                dfs_visit(tetangga)

        waktu += 1
        waktu_f[node] = waktu

    for node in graf:
        if node not in dikunjungi:
            dfs_visit(node)

    return waktu_d, waktu_f

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

    print("DFS v1 (Mencari Jalur):", dfs_v1(graf, 'A', 'F'))
    print("DFS v2 (Kedalaman ke Tujuan):", dfs_v2(graf, 'A', 'F'))
    waktu_d, waktu_f = dfs_v3(graf, 'A')
    print("DFS v3 (Waktu Penemuan dan Selesai):")
    for node in graf:
        print(f"Node {node}: Ditemukan pada {waktu_d[node]}, Selesai pada {waktu_f[node]}")