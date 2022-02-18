n = int(input("Masukkan data : "))

nilai = []
jum = 0
i = 0
a = 1

while a != 9999:
    a += 1
    print("Masukkan data ke", a )
    a = int(input("Masukkan angka : "))
    nilai.append(a)
    jum += nilai[i]
    rata2 = jum / n

print("Rata-rata  = %0.2f" % rata2)

