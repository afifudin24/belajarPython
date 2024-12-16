def cariKataTerbanyak(string):
    #mengubah teks menjadi huruf kecil dan memisahkan kata kata
    list_kata = string.lower().split()
    #membuat kamus untuk menghitung frekuensi kata
    frekuensi_kata = {}
    for kata in list_kata:
        if (kata in frekuensi_kata):
            frekuensi_kata[kata] += 1
        else:
            frekuensi_kata[kata] = 1
    #mencari kata dengan frekuensi tertinggi
    kata_terbanyak = max(frekuensi_kata, key=frekuensi_kata.get)
    return kata_terbanyak, frekuensi_kata[kata_terbanyak], frekuensi_kata

string = str(input("Masukkan Kalimat : "))
kata, frekuensi, frekuensi_kata = cariKataTerbanyak(string)
print(f"Kata terbanyak adalah '{kata}' dengan frekuensi {frekuensi} dan keseluruhan {frekuensi_kata}.")
