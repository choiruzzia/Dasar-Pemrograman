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
    
    if choice=='1':
        sisi=int(input("Masukkan sisi bujur sangkar:"))
        print("Luas bujur sangkar adalah","=", luas_bujur_sangkar(sisi))
        print('')
        print('')
    elif choice=='2':
        panjang=int(input("Masukkan panjang sisi persegi panjang:"))
        lebar=int(input("Masukkan lebar sisi persegi panjang:"))
        print("Luas persegi adalah","=", luas_persegi_panjang(panjang,lebar))
        print('')
        print('')
    elif choice=='3':
        alas=int(input("Masukkan alas segitiga:"))
        tinggi=int(input("Masukkan tinggi segitiga:"))
        print("Luas segitiga adalah","=", luas_segitiga(alas,tinggi))
        print('')
        print('')
    elif choice=='4':
        jari=int(input("Masukkan jari-jari lingkaran:"))
        print("Luas lingkaran adalah","=", luas_lingkaran(jari))
        print('')
        print('')
    elif choice=='5':
        alas=int(input("Masukkan alas jajar genjang:"))
        tinggi=int(input("Masukkan tinggi jajar genjang:"))
        print("Luas jajar genjang adalah","=", luas_jajar_genjang(alas,tinggi))
        print('')
        print('')
    elif choice=='6':
        sisi=int(input("Masukkan sisi bujur sangkar:"))
        print("Keliling bujur sangkar adalah","=", keliling_bujur_sangkar(sisi))
        print('')
        print('')
    elif choice=='7':
        panjang=int(input("Masukkan panjang sisi persegi panjang:"))
        lebar=int(input("Masukkan lebar sisi persegi panjang:"))
        print("Keliling persegi adalah","=", keliling_persegi_panjang(panjang,lebar))
        print('')
        print('')
    elif choice=='8':
        alas=int(input("Masukkan alas segitiga:"))
        tinggi=int(input("Masukkan tinggi segitiga:"))
        sisi=int(input("Masukkan sisi segitiga:"))
        print("Keliling segitiga adalah","=", keliling_segitiga(alas,tinggi,sisi))
        print('')
        print('')
    elif choice=='9':
        jari=int(input("Masukkan jari-jari lingkaran:"))
        print("Keliling lingkaran adalah","=", keliling_lingkaran(jari))
        print('')
        print('')
    elif choice=='10':
        alas=int(input("Masukkan alas jajar genjang:"))
        miring=int(input("Masukkan sisi miring jajar genjang:"))
        print("Keliling jajar genjang adalah","=", keliling_jajar_genjang(alas,miring))
        print('')
        print('')
    elif choice=='0':
        print('')
        print('')
        break
    else:
        print("Pilihan yang Anda masukkan salah.")
        print('')
        print('')
