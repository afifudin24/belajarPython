def hitungLuasLingkaran():
    try:
        jarijari = input("Masukkan Jari - jari : ")
        luas = 3.14 * (int(jarijari) ** 2)
        return f"Luas lingkaran: {luas:.2f}"
    except ValueError:
        return "Input harus berupa angka!"

print(hitungLuasLingkaran())
