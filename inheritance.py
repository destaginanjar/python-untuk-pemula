
# Bab 13: Inheritance (Pewarisan)

# Class induk
class Hewan:
    def __init__(self, nama):
        self.nama = nama

    def makan(self):
        print(self.nama, "sedang makan.")


# Class anak
class Kucing(Hewan):
    def bersuara(self):
        print(self.nama, "mengeluarkan suara: Meong!")


# Membuat objek dari class Kucing
kucing1 = Kucing("Milo")

# Menggunakan method dari class induk
kucing1.makan()

# Menggunakan method dari class anak
kucing1.bersuara()
