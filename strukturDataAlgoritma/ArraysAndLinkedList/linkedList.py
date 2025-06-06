class Node:
    def __init__(self, data):
        self.data = data  # Data yang disimpan di node
        self.next = None  # Pointer ke node berikutnya, awalnya None

class LinkedList:
    def __init__(self):
        self.head = None  # Awalnya, Linked List kosong (tidak ada head)

    # ----------------------------------------------------
    # Operasi Dasar Linked List
    # ----------------------------------------------------

    # Menambahkan elemen di awal (prepend)
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head  # Node baru menunjuk ke head lama
        self.head = new_node      # Node baru menjadi head
        print(f"Menambahkan {data} di awal. List: {self.to_list()}")

    # Menambahkan elemen di akhir (append)
    def append(self, data):
        new_node = Node(data)
        if not self.head:  # Jika list kosong, node baru jadi head
            self.head = new_node
            print(f"Menambahkan {data} di akhir. List: {self.to_list()}")
            return

        last_node = self.head
        while last_node.next:  # Traverse sampai menemukan node terakhir
            last_node = last_node.next
        last_node.next = new_node # Node terakhir menunjuk ke node baru
        print(f"Menambahkan {data} di akhir. List: {self.to_list()}")

    # Mencetak seluruh elemen list (untuk visualisasi)
    def to_list(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return " -> ".join(map(str, elements)) if elements else "List Kosong"

    # Menghapus elemen berdasarkan data
    def delete_node(self, key):
        current = self.head

        # Jika head adalah node yang akan dihapus
        if current and current.data == key:
            self.head = current.next
            current = None
            print(f"Menghapus {key}. List: {self.to_list()}")
            return

        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        if current is None: # Jika key tidak ditemukan
            print(f"Elemen {key} tidak ditemukan untuk dihapus.")
            return

        # Melepaskan node dari list
        prev.next = current.next
        current = None
        print(f"Menghapus {key}. List: {self.to_list()}")

    # Mencari elemen
    def search(self, key):
        current = self.head
        while current:
            if current.data == key:
                print(f"Elemen {key} ditemukan dalam list.")
                return True
            current = current.next
        print(f"Elemen {key} tidak ditemukan dalam list.")
        return False

    # Mendapatkan panjang list
    def get_length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

# Contoh penggunaan Linked List
print("--- Demonstrasi Linked List ---")
my_linked_list = LinkedList()

my_linked_list.append(10)
my_linked_list.append(20)
my_linked_list.prepend(5)
my_linked_list.append(30)

print(f"Panjang Linked List: {my_linked_list.get_length()}")

my_linked_list.search(20)
my_linked_list.search(15)

my_linked_list.delete_node(20)
my_linked_list.delete_node(5)
my_linked_list.delete_node(100) # Elemen tidak ada

my_linked_list.append(40)
print(f"List akhir: {my_linked_list.to_list()}")
