# 1. Membuat list kosong
my_empty_list = []
print(f"List kosong: {my_empty_list}")

# 2. Membuat list dengan beberapa elemen (sipisahkan koma, siapit kurung siku [])
angka_genap = [2, 4, 6, 8, 10]
print(f"List angka genap: {angka_genap}")

nama_buah = ["Apel", "Jeruk", "Mangga"]
print(f"List nama buah: {nama_buah}")

# 3. List dengan tipe data campuran (heterogeneous)
campuran = ["Halo", 123, 3.14, True, [1, 2]]
print(f"List campuran: {campuran}")

# 4. Membuat list dari string (setiap karakter menjadi elemen)
list_dari_string = list("Python")
print(f"List dari string 'Python': {list_dari_string}")

# 5. Membuat list dari iterable lain (misalnya, tuple)
tuple_angka = (1, 2, 3)
list_dari_tuple = list(tuple_angka)
print(f"List dari tuple (1, 2, 3): {list_dari_tuple}")
