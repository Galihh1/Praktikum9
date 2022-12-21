f = open("demofile2.txt", "a")
f.write("Sekarang file memiliki lebih banyak konten!")
f.close()

#open dan baca file setelah menambahkan:
f = open("demofile2.txt","r")
print(f.read())