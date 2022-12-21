file_text = open("demofile2.txt.", "r")

# baca isi file
puisi = file_text.read()

# cetak isi file
print(puisi)

# tutup file
file_text.close()