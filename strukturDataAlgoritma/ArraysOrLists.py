# Membuat sebuah List (Array)
my_list = [10, 20, 30, 40, 50]
print(f"List awal: {my_list}")

# Mengakses elemen berdasarkan indeks
print(f"Elemen pada indeks 0: {my_list[0]}")  # Output: 10
print(f"Elemen pada indeks 2: {my_list[2]}")  # Output: 30
print(f"Elemen pada indeks terakhir (menggunakan indeks negatif): {my_list[-1]}") # Output: 50

# Mengubah elemen
my_list[1] = 25
print(f"List setelah mengubah elemen pada indeks 1: {my_list}") # Output: [10, 25, 30, 40, 50]

# Menambahkan elemen di akhir (append)
my_list.append(60)
print(f"List setelah menambahkan 60: {my_list}") # Output: [10, 25, 30, 40, 50, 60]

# Menambahkan elemen di posisi tertentu (insert)
my_list.insert(2, 28) # Masukkan 28 pada indeks 2
print(f"List setelah menyisipkan 28 pada indeks 2: {my_list}") # Output: [10, 25, 28, 30, 40, 50, 60]

# Menghapus elemen berdasarkan nilai (remove)
my_list.remove(40)
print(f"List setelah menghapus 40: {my_list}") # Output: [10, 25, 28, 30, 50, 60]

# Menghapus elemen berdasarkan indeks (pop)
popped_element = my_list.pop(1) # Menghapus elemen pada indeks 1 (yaitu 25)
print(f"List setelah menghapus elemen pada indeks 1: {my_list}") # Output: [10, 28, 30, 50, 60]
print(f"Elemen yang dihapus: {popped_element}") # Output: 25

# Mendapatkan ukuran List
print(f"Ukuran List saat ini: {len(my_list)}")

# Iterasi melalui List
print("Iterasi melalui List:")
for item in my_list:
    print(item)

# Slicing List (mengambil bagian dari list)
sub_list = my_list[1:4] # Dari indeks 1 sampai sebelum indeks 4
print(f"Sub-list dari indeks 1 sampai 3: {sub_list}") # Output: [28, 30, 50]
