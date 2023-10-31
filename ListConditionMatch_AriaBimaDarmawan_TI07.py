kendaraan1 = [1140,"Mustang GT","1200cc","Biru"]
print(kendaraan1)

kendaraan1.append("500 juta")
kendaraan1.append("4 roda")
print(kendaraan1)

kendaraan1.insert(2,"Ford Shelby")
kendaraan1.insert(2,"Sport")
print(kendaraan1)

pesan ="""Selamat datang di program menghitung luas bangun datar
menu:
1. Menghitung luas persegi
2. Menghitung luas lingkaran
3. Menghitung luas segitiga
masukkan angka:
"""
pilihan = input(pesan)

match pilihan:
    case "1":
        print("menghitung luas persegi")
        sisi = int(input("masukan sisi: "))
        luas = sisi * sisi 
        print("luas dari persegi dengan sisi", sisi, "adalah", luas)
    case "2":
        print("menghitung luas lingkaran")
        jari = int(input("masukan jari-jari:"))
        luas = 3.14 * jari * jari 
        print("luas dari lingkaran dengan jari", jari, "adalah", luas)
    case "3":
        print("menghitung luas segitiga")
        alas = int(input("masukan alas:"))
        tinggi = int(input("masukan tinggi:"))
        luas = 1/2 * alas * tinggi
        print("luas dari segitiga dengan alas", alas, "dan juga tinggi", tinggi, "adalah", luas)
    case _:
        print("Maaf tidak ada pilihan seperti itu")
