
# Bab 16: Exception Handling

try:
    angka1 = int(input("Masukkan angka pertama: "))
    angka2 = int(input("Masukkan angka kedua: "))

    hasil = angka1 / angka2

    print("Hasil pembagian:", hasil)

except ValueError:
    print("Error: Masukkan angka yang valid!")

except ZeroDivisionError:
    print("Error: Angka tidak boleh dibagi dengan nol!")

finally:
    print("Program selesai.")
