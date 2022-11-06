#Tugas Nomor 2
print("""Selamat Datang.
Silahkan gunakan program ini untuk mengkonversi Suhu Fahrenheit ke Suhu Celcius dan Reamur

Selamat Mencobaa ^-^
""")
print("Note: [karena Saya masih pemula, saat mengetik 'tidak' mohon perhatikan case]")

#Variabel
respon = "Ya","ya"
end = "Terimakasihh Banyakk. Semoga Bermanfaat dan Tetaplah Konsisten dalam belajar >\\\<"
konversiSukses = "Selamat, Konversi Sukses !"

#Inputan
while(respon == "Ya","ya"):
    print("""
""")
    F = int(input("Silahkan Masukkan Suhu Fahrenheit (derajat) = "))
    
    #Rumus Celcius
    RumusC = (F)-32
    Celcius = (5/9)*RumusC
    
    #Rumus Reamur
    RumusR = (F)-32
    Reamur = (4/9)*RumusR
    
    #Output
    print(konversiSukses)
    print("Suhu Celcius = ",Celcius,"Derajat")
    print("Suhu Reamur = ",Reamur,"Derajat")
    respon = input ("""
Ulangg, kahh??? (Ya/tidak) = """)
    if respon == "tidak":
        break
    else:
        print("Jika ingin selesai ketikkan 'tidak' dengan benar")

print("""
""")
print(end)
print("""
""")

#Source
print("sumberRumus: https://saintif.com/fahrenheit-ke-celcius/")
print("""
""")

#Credit. hhe
print("""ALFIANN NUR USYAID
Teknik Informatika | 0110222132 | TI 07""")