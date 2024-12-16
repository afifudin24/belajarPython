def cekBilanganPrima(bilangan):
    if bilangan < 2:
        return False
    if bilangan == 2:
        return True
    if bilangan % 2 == 0:
        return False
    for i in range(3, int(bilangan ** 0.5) + 1, 2):
        if bilangan % i == 0:
            return False
    return True

# Contoh penggunaan
bilangan = int(input("Masukkan bilangan: "))
if cekBilanganPrima(bilangan):
    print(f"{bilangan} adalah bilangan prima.")
else:
    print(f"{bilangan} bukan bilangan prima.")
