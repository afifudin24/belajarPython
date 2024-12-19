panjang_rebung = float(input("Masukkan Panjang Rebung"))
jumlah_teman = int(input("Masukkan Jumlah Teman"))
perbandingan = input("Masukkan perbandingan dengan batas per spasi")
list_perbandingan = list(map(int, perbandingan.split()))
totalrasio = sum(list_perbandingan)
bagianPerRasio = panjang_rebung // totalrasio

distribusi = []
for rasio in list_perbandingan:
    perbagian = (panjang_rebung // jumlah_teman) / rasio
    distribusi.append(perbagian)

totaldistribusi = sum(distribusi)
sisa = panjang_rebung - totaldistribusi
gabungkan = " ".join(map(str, distribusi))
print(sisa, gabungkan)    