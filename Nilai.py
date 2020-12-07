import time
import os

data_nama = ["apd8"]
data_pw = ["1234"]
login = 0
b = 3

print(" ------------------------------- ")
print(" |Silahkan Login terlebih dahulu|")
print(" ------------------------------- ")
print("\n")
while login == 0:
    nama = input("Silahkan masukkan ID : ")
    pw = input("Silahkan masukkan password : ")
    for i in range(len(data_nama)):
        if nama == data_nama[i] and pw == data_pw[i]:
            login = 1
        else:
            login = 0
    if login == 1:
        break
    else:
        b -= 1
        print("Anda Salah")

    if b == 0:
        print("Sudah 3x, Sistem Kasir Otomatis Berhenti")
        exit()
        
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_menu():
    clear_screen()
    print("\n")
    print("_"*70)
    print("\t\tAPLIKASI MENENTUKAN NILAI INDEKS MAHASISWA")
    print("_"*70)
    print("[1] Nilai Mahasiswa")
    print("[2] Keluar")
    selected_menu = input("Pilih menu> ")

    if(selected_menu == "1"):
        nilai_mahasiwa()
    elif(selected_menu == "2"):
        print("Terima kasih telah menggunakan Aplikasi Menentukan Nilai Indeks Mahasiswa")
        time.sleep(5)
        exit()
    else:
        print("Kamu memilih menu yang salah!")
        back_to_menu()

def back_to_menu():
    print("\n")
    input("Tekan Enter untuk kembali...")
    time.sleep(3)
    show_menu()

def nilai_mahasiwa():
    clear_screen()
    print("="*30)
    print("\tData Mahasiswa")
    print("="*30)
    #menginput data Mahasiswa
    nama = input("Masukkan Nama Mahasiswa : ")
    kelas = input("Masukkan Kelas : ")
    nim = int(input("Masukkan NIM Mahasiswa : "))
    semester = int(input("Masukkan Semester : "))
            

    #Nilai Ujian Akhir
    print("\n")
    print("="*30)
    print("\tNilai Mahasiswa")
    print("="*30)

    EROR = True
    while(EROR):
        try:   
                tugas = int(input("Masukkan nilai Tugas : "))
                uts = int(input("Masukkan nilai UTS : "))
                uas = int(input("Masukkan nilai UAS : "))
                na = int(float(0.15*tugas) + (0.35*uts) + (0.50*uas))
                EROR = False
        except ValueError:
            print("Input anda salah, Masukkan Angka!")


    clear_screen()
    #Nilai Tugas
    if tugas >= 80:
        grade_tugas = "A"
    elif tugas >= 70:
        grade_tugas = "B"
    elif tugas >= 60:
        grade_tugas = "C"
    elif tugas >= 50:
        grade_tugas = "D"
    else:
        grade_tugas = "E"
    
    #Nilai UTS
    if uts >= 80:
        grade_uts = "A"
    elif uts >= 70:
        grade_uts = "B"
    elif uts >= 60:
        grade_uts = "C"
    elif uts >= 50:
        grade_uts = "D"
    else:
        grade_uts = "E"

    #Nilai UAS
    if uas >= 80:
        grade_uas = "A"
    elif uas >= 70:
        grade_uas = "B"
    elif uas >= 60:
        grade_uas = "C"
    elif uas >= 50:
        grade_uas = "D"
    else:
        grade_uas = "E"

    #Nilai Nilai Akhir
    if na >= 80:
        grade_na = "A"
    elif na >= 70:
        grade_na = "B"
    elif na >= 60:
        grade_na = "C"
    elif na >= 50:
        grade_na = "D"
    else:
        grade_na = "E"
    
    #Output
    
    print("\n")
    print("="*60)
    print("\t\tKartu Hasil Studi Mahasiswa")
    print("="*60)
    print ("Nama \t\t\t: %s" % nama)
    print ("NIM \t\t\t: %d" % nim)
    print ("Kelas \t\t\t: %s" % kelas)
    print ("Semester \t\t: %d" % semester) 
    print ("Nilai Tugas \t\t: %d" % tugas)
    print ("Grade Tugas \t\t: %s" % grade_tugas)
    print ("Nilai UTS \t\t: %d" % uts)
    print ("Grade UTS \t\t: %s" % grade_uts)
    print ("Nilai UAS \t\t: %d" % uas)
    print ("Grade UAS \t\t: %s" % grade_uas)
    print("------------------------------------")
    print ("Nilai Akhir               %d" % na)
    print("------------------------------------")
    print ("Grade Nilai Akhir \t: %s" % grade_na)
    
    if na >= 60:
        print ("Keterangan \t\t: LULUS")
    else :
        print ("Keterangan \t\t: TIDAK LULUS")
    back_to_menu()

if __name__ == "__main__":
    while True:
        show_menu()