#Tugas Nomor 1
print("""Selamat Datang.
Silahkan gunakan program ini untuk mencari Luas dan Keliling dari Jajar Genjang

Selamat Mencobaa ^-^
""")
print("Note: [karena Saya masih pemula, saat mengetik 'tidak' mohon perhatikan case]")

#Variabel
respon = "Ya","ya"
end = "Terimakasihh Banyakk. Semoga Bermanfaat dan Tetaplah mencintai Matematika!! >\\\<"
soundEffect_hhe = """
Tadaaa!!!"""

#Inputan
while(respon == "Ya","ya"):
    print("""
""")
    A = int(input("Silahkan masukkan alas dari Jajar Genjang (cm) = "))
    SM = int(input("Silahkan masukkan sisi miring dari Jajar Genjang (cm) = "))
    T = int(input("Silahkan masukkan tinggi dari Jajar Genjang (cm) = "))

    #Rumus untuk mencari Luas
    rumusLuas = A*T

    #Rumus untuk mencari Keliling
    rumusKeliling = (2*A)+(2*SM)
    
    #output
    print(soundEffect_hhe)
    print("Luas dari Jajar Genjang tersebut adalah : ",rumusLuas,"cm²")
    print("Keliling dari Jajar Genjang tersebut adalah : ",rumusKeliling,"cm")
    respon = input("""
Lanjut mencari? (Ya/tidak) = """)
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
print("sumberRumus: https://katadata.co.id/safrezi/berita/618396732b896/rumus-luas-dan-keliling-jajar-genjang-beserta-contoh-soalnya")
print("""
""")

#Credit. hhe
print("""ALFIANN NUR USYAID
Teknik Informatika | 0110222132 | TI 07""")