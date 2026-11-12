
# Bab 14: Polymorphism

# Class Kucing
class Kucing:
    def bersuara(self):
        print("Kucing: Meong!")


# Class Anjing
class Anjing:
    def bersuara(self):
        print("Anjing: Guk guk!")


# Class Burung
class Burung:
    def bersuara(self):
        print("Burung: Cuit cuit!")


# Membuat objek
hewan = [Kucing(), Anjing(), Burung()]

# Menjalankan method yang sama
for suara in hewan:
    suara.bersuara()
