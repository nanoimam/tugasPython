print("def menghitung volume tabung")

nilai_a = int(input("Masukan Nilai 1 : "))
nilai_b = int(input("Masukan Nilai 2 : "))
volume = ((nilai_a/2)*(nilai_a/2))*3.14*nilai_b

print("maka hasil volume = > " + str(volume))

print("lambda menghitung segitiga sama sisi")

sisi = int(input("Masukan panjang sisi segitiga :"))
keliling = sisi*3

print("Keliling dari segitiga sama sisi adalah : " + str(keliling))

print("class kalkulator")

angkaa = int(input("Masukan Angka 1 : "))
angkab = int(input("Masukan Angka 2 : "))

perhitungan = input("Masukan Operator Hitung : ")
if (perhitungan == f"+"):
    hasil = angkaa + angkab
elif (perhitungan == f"-"):
    hasil = angkaa - angkab
    print(hasil)
elif (perhitungan == f"*"):
    hasil = angkaa * angkab
    print(hasil)
elif (perhitungan == f"/"):
    hasil = angkaa / angkab
    print(hasil)
