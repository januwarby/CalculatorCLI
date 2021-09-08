# Bermain Dengan Python (Membuat Kalkulator Sederhana)

# Penjumlahan Dua Buah Angka
def tambah(x, y):
    return x + y

# Pengurangan Dua Buah Angka
def kurang(x, y):
    return x - y

# Perkalian Dua Buah Angka
def kali(x, y):
    return x * y

# Pembagian Dua Buah Angka
def bagi(x, y):
    return x / y


print("Pilih Perintah Operasi.")
print("1.Penjumlahan")
print("2.Pengurangan")
print("3.Perkalian")
print("4.Pembagian")

while True:
    # Pilih Perintah Operasi
    pilihan = input("Masukan Perintah(1/2/3/4): ")


    if pilihan in ('1', '2', '3', '4'):
        angka1 = float(input("Masukan Angka Pertama: "))
        angka2 = float(input("Masukan Angka Kedua: "))

        if pilihan == '1':
            print(angka1, "+", angka2, "=", tambah(angka1, angka2))

        elif pilihan == '2':
            print(angka1, "-", angka2, "=", kurang(angka1, angka2))

        elif pilihan == '3':
            print(angka1, "*", angka2, "=", kali(angka1, angka2))

        elif pilihan == '4':
            print(angka1, "/", angka2, "=", bagi(angka1, angka2))
        break
    else:
        print("Perintah Tidak Dikenali")
