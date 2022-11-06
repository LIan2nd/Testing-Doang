#Tugas Nomor 3
print("""Selamat Datang.
Silahkan gunakan program ini untuk menghitung Berat Badan Remaja dan Dewasa yang Ideal

Selamat Mencobaa ^-^
""")
print("Note: [karena Saya masih pemula, saat mengetik 'tidak' mohon perhatikan case]")

#Variabel
respon = "Ya","ya"
end = "Terimakasihh Banyakk. Semoga Bermanfaat dan Jangan lupa Berolahragaa!! >\\\<"
soundEffect_hhe = "Jeng Jeng Jengg !!!"

#Inputan
while(respon == "Ya","ya"):
    print("""
""")
    T = int(input("Silahkan masukkan tinggi badanmu (cm) = "))

    #Rumus untuk Berat Badan Pria
    RumusP = T-100
    RumusP2 = RumusP*0.10
    Pria = RumusP-RumusP2

    #Rumus untuk Berat Badan Wanita
    RumusW = T-100
    RumusW2 = RumusW*0.15
    Wanita = RumusW-RumusW2

    #Output
    print(soundEffect_hhe)
    print("Berat Badan Idealmu (Jika Kamu Pria) adalah : ",Pria,"kg")
    print("Berat Badan Idealmu (Jika Kamu Wanita) adalah : ",Wanita,"kg")
    respon = input("""
Lanjut menghitung? (Ya/tidak) = """)
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
print("sumberRumus: https://hellosehat.com/nutrisi/cara-menghitung-berat-badan-ideal/?amp=1")
print("""
""")

#Credit. hhe
print("""ALFIANN NUR USYAID
Teknik Informatika | 0110222132 | TI 07""")