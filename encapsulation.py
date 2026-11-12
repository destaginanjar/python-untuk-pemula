
# Bab 12: Encapsulation

class Siswa:
    def __init__(self, nama, nilai):
        self.nama = nama
        self.__nilai = nilai

    def tampilkan_data(self):
        print("Nama:", self.nama)
        print("Nilai:", self.__nilai)

    def ubah_nilai(self, nilai_baru):
        if 0 <= nilai_baru <= 100:
            self.__nilai = nilai_baru
            print("Nilai berhasil diperbarui!")
        else:
            print("Nilai harus antara 0 sampai 100.")


# Membuat objek siswa
siswa1 = Siswa("Desta", 85)

# Menampilkan data awal
siswa1.tampilkan_data()

# Mengubah nilai siswa
siswa1.ubah_nilai(95)

# Menampilkan data terbaru
siswa1.tampilkan_data()
