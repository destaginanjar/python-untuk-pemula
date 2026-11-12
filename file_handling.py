# Bab 17: File Handling (Read & Write File)

with open("catatan.txt", "w") as file:
    file.write("Belajar Python Dasar\n")
    file.write("Materi File Handling\n")

print("Data berhasil ditulis ke file!")

with open("catatan.txt", "r") as file:
    isi = file.read()

print("\nIsi file:")
print(isi)
