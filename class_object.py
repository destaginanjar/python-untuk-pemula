
# Bab 8: Class dan Object

# Membuat Class
class Siswa:
    def __init__(self, nama, kelas, jurusan):
        self.nama = nama
        self.kelas = kelas
        self.jurusan = jurusan

    def tampilkan_data(self):
        print("Nama:", self.nama)
        print("Kelas:", self.kelas)
        print("Jurusan:", self.jurusan)

# Membuat Object
siswa1 = Siswa("Aiman", "XI RPL-B", "Rekayasa Perangkat Lunak")
siswa2 = Siswa("Budi", "XI RPL-A", "Rekayasa Perangkat Lunak")

# Menampilkan Data Object
print("=== DATA SISWA 1 ===")
siswa1.tampilkan_data()

print("\n=== DATA SISWA 2 ===")
siswa2.tampilkan_data()
