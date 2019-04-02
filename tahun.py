x = int(input("Tahun Kelahiran Anda : "))

usia = 2019 - x
golongan = ""

print("Usia Anda saat ini adalah %i tahun" %(usia))

if usia <= 12 :
    golongan = "Anak-Anak"
elif usia >= 13 and usia <= 24 :
    golongan = "Remaja"
elif usia >= 25 and usia <= 46 :
    golongan = "Orang Tua"
else :
    golongan = "Tidak Mungkin"

print("Anda termasuk golongan %s" %(golongan))