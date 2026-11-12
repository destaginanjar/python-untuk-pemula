
# Bab 3: Lists dan Dictionaries

# Membuat List
buah = ["Apel", "Jeruk", "Mangga", "Pisang"]

print("=== LIST ===")
print("Daftar buah:", buah)
print("Buah pertama:", buah[0])
print("Buah kedua:", buah[1])

# Menambahkan data
buah.append("Anggur")
print("Setelah ditambah:", buah)

# Menghapus data
buah.remove("Jeruk")
print("Setelah dihapus:", buah)

# Perulangan List
print("\nDaftar buah:")
for item in buah:
    print(item)

# Membuat Dictionary
print("\n=== DICTIONARY ===")

siswa = {
    "nama": "Aiman",
    "kelas": "XI RPL",
    "jurusan": "Rekayasa Perangkat Lunak"
}

print("Data siswa:", siswa)
print("Nama:", siswa["nama"])
print("Kelas:", siswa["kelas"])

# Mengubah data
siswa["kelas"] = "XI RPL-B"

# Menambahkan data
siswa["sekolah"] = "SMK"

print("\nData siswa setelah diperbarui:")
for key, value in siswa.items():
    print(key, ":", value)
