def luas_bujur_sangkar(x):
    return x*x
def luas_persegi_panjang(x,y):
    return x*y
def luas_segitiga(x,y):
    return (1/2)*x*y
def luas_lingkaran(x):
    return 3.14*x*x
def luas_jajar_genjang(x,y):
    return x*y
def keliling_bujur_sangkar(x):
    return 4*x
def keliling_persegi_panjang(x,y):
    return 2*(x+y)
def keliling_segitiga(x,y,z):
    return x+y+z
def keliling_lingkaran(x):
    return 2*3.14*x
def keliling_jajar_genjang(x,y):
    return 2*(x+y)

choice=1
while choice!=0:
    print("Pilih Rumus Bangun Datar.")
    print("1. Luas Bujur Sangkar")
    print("2. Luas Persegi Panjang")
    print("3. Luas Segitiga")
    print("4. Luas Lingkaran")
    print("5. Luas Jajar Genjang")
    print("6. Keliling Bujur Sangkar")
    print("7. Keliling Persegi Panjang")
    print("8. Keliling Segitiga")
    print("9. Keliling Lingkaran")
    print("10. Keliling Jajar Genjang")
    print("0. Exit")
    
    choice=input("Masukkan pilihan anda :")
    print('')
