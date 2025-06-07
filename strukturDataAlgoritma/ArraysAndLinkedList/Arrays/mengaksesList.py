my_list = ["a", "b", "c", "d", "e"]

# Mengakses elemen pertama (indeks 0)
print(f"Elemen pertama: {my_list[0]}") # Output: a

# Mengakses elemen ketiga (indeks 2)
print(f"Elemen ketiga: {my_list[2]}") # Output: c

# Mengakses elemen terakhir (indeks negatif)
print(f"Elemen terakhir: {my_list[-1]}") # Output: e

# Mengakses elemen kedua terakhir
print(f"Elemen kedua terakhir: {my_list[-2]}") # Output: d

# Hati-hati: Mengakses indeks yang di luar jangkauan akan menghasilkan indexError
try:
    print(my_list[5])
except IndexError as e:
    print(f"Error: {e}") # Output: list index out of range
