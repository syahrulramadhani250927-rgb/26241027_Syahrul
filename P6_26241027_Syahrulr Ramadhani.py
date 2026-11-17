# Meminta input dua digit terakhir NIM 
a = int(input("Digit A: "))
b = int(input("Digit B: "))

# Membuat dua kondisi Boolean berdasarkan nilai digit >= 5
kondisi1 = a >= 5
kondisi2 = b >= 5

# Menampilkan hasil evaluasi Boolean dari kondisi1 dan kondisi2
print("Kondisi 1:", kondisi1)
print("Kondisi 2:", kondisi2)

# Menampilkan hasil operasi logika NOT, AND, OR, dan ^(XOR)
print("NOT:", not kondisi1)
print("AND:", kondisi1 and kondisi2)
print("OR:", kondisi1 or kondisi2)
print("XOR:", kondisi1 ^ kondisi2)

# Penjelasan mengapa OR dan XOR berbeda saat kedua kondisi bernilai True:
# Operator OR (Inclusive OR) bernilai True jika minimal salah satu kondisi True (termasuk saat keduanya True),
# sedangkan XOR (Exclusive OR) hanya bernilai True jika kedua kondisi berbeda nilai,
# sehingga hasilnya False ketika kedua kondisi sama-sama bernilai True.