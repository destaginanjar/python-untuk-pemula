
# Bab 15: Abstraction (Abstraksi)

from abc import ABC, abstractmethod


# Class abstrak
class Kendaraan(ABC):

    @abstractmethod
    def berjalan(self):
        pass


# Class turunan Mobil
class Mobil(Kendaraan):
    def berjalan(self):
        print("Mobil berjalan menggunakan empat roda.")


# Class turunan Motor
class Motor(Kendaraan):
    def berjalan(self):
        print("Motor berjalan menggunakan dua roda.")


# Membuat objek
mobil1 = Mobil()
motor1 = Motor()

# Menjalankan method
mobil1.berjalan()
motor1.berjalan()
