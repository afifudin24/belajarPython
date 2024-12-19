def makanLumpia(array):
    list_angka = list(map(int, array.split()))
    print(list_angka)
    total = sum(list_angka)
    maksPerHari = 3
    jumlahHari = 0
    currentSum = 0
    for index, angka in enumerate(list_angka):
      while angka >= 3:
         jumlahHari += 1
         angka -= 3
      print(index)   
      if angka < 3:
           if index == 0 or index == 3:
                 if(angka != 0):
                     jumlahHari += 1        
           else:    
               currentSum += angka
               if currentSum >= 3:
                   jumlahHari += 1
    
        
    return jumlahHari
 
inputan = input("Masukkan 4 angka")
print(makanLumpia(inputan))

# solved