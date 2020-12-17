#Program Bank Sampah
# Raid Mahdy
#IK1E
#Politeknik Negeri Semarang

#username=admin
#password=admin
import getpass

i=n=0

def header():
    print("====Bank Sampah Warga Tembalang====")
    print("===================================")
    print("=>Merupakan konsep pengumpulan sampah kering dan dipilah serta memiliki manajemen"
          "\n  layaknya perbankan tapi yang ditabung bukan uang melainkan sampah.")
    print("====================================")
    print()
def menu():
    print("Selamat Datang di Program Bank Sampah")
    print("====Menu====")
    print("[1].Admin")
    print("[2].Nasabah")
    print("[0].exit")
def sampah():
    print("===========Jenis Sampah kering=============")
    print(" Jenis Sampah                   Harga/kg/btl")
    print("----------------------------------------------")
    print(" 1.Sampah berbahan plastik      Rp.3000")
    print(" 2.Sampah berbahan kertas       Rp.1000")
    print(" 3.Sampah besi dan logam        Rp.20.000")
    print(" 4.Sampah elektronik            Rp.30.000")
    print(" 5.Sampah botol kaca            Rp.1000")
    print(" 6.Sampah aluminium dan kaleng  Rp.10.000")
def data():
    print("========Data Bank Sampah=======")
    print("--------------------------------")
    print("No   Nama Nasabah     Berat/kg       Jenis     Saldo")
    print("--------------------------------")
    for n in range(i):
        print(n+1," ",nasabah1[n],"      ",jlh1[n], "      ",jenis[n],"   ",total1[n])
        print("")
    

    

nasabah1=[]
jlh1=[]
jenis=[]
total1=[]

header()
while True :
    i+=1
    menu()
    pilih=input("")
    if pilih=='1':
        user = input("Username: ")
        sandi = getpass.getpass("Password: ")
        
        if sandi == 'admin' and user == 'admin':
            print ("Anda Telah Login")
            print()
            data()
        else:
            print ("Username atau Password Anda Salah")
            print()
    elif pilih=='2':
        nasabah=input("Nama Nasabah:")
        nasabah1.append(nasabah)
        print()
        print("=====Selamat Datang,",nasabah,"=====")
        print("Silahkan Pilih Jenis Sampah Kering")
        sampah()
        smph=input()
        
        
    
        if smph=="1":            
            jenis.append("Plastik")
            jlh=int(input("Berapa berat sampah Plastik/kg="))
            jlh1.append(jlh)
            total=jlh*3000
            total1.append(total)


            print (jlh," kg sampah Plastik= Rp", total)
            print("========================================")
            
        elif smph=="2":
            jenis.append("Kertas")

            jlh1.append(jlh)
            total1.append(total)
            jlh=int(input("Berapa berat sampah Kertas/kg="))

            total=jlh*1000
            print (jlh," kg sampah Kertas= Rp", total)
            print("========================================")

            
        elif smph=="3":
            jenis.append("Besi & Logam")
            total1.append(total)
            jlh1.append(jlh)
            jlh=int(input("Berapa berat sampah Besi & Logam/kg="))
            total=jlh*20000
            print (jlh," kg sampah Kertas= Rp", total)
            print("========================================")

        elif smph=="4":
            jenis.append("elektronik")
            total1.append(total)
            jlh1.append(jlh)
            jlh=int(input("Berapa berat sampah elektronik/kg="))
            total=jlh*30000
            print (jlh," kg sampah elektronik= Rp", total)
            print("========================================")

        elif smph=="5":
            jenis.append("botol kaca")
            jlh1.append(jlh)
            total1.append(total)
            jlh=int(input("Berapa buah sampah botol kaca/btl="))
            total=jlh5*1000
            print (jlh5," kg sampah botol kaca= Rp", total)
            print("========================================")

        elif smph=="6":
            jenis.append("aluminium dan kaleng")
            jlh1.append(jlh)
            total.append(total)
            jlh=int(input("Berapa berat sampah aluminium dan kaleng/kg="))
            jenis=("aluminium dan kaleng")
            total=jlh*10000
            print (jlh," kg sampah aluminium dan kaleng = Rp", total)
            print("========================================")

        else:
            print("Pilihan tidak tersedia")
        
    else:
        print("Pilihan tidak tersedia")
        break

