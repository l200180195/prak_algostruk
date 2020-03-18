class Mhs(object):
    def __init__(self, nama, nim, kota, uangsaku):
        self.nama = nama
        self.nim = nim
        self.kotaTinggal = kota
        self.uangSaku = uangsaku

m0 = Mhs("Abraham", 107, "Sukoharjo", 240000)
m1 = Mhs("Bella", 113, "Sragen", 230000)
m2 = Mhs("Chyn", 145, "Surakarta", 250000)
m3 = Mhs("Dude", 180, "Surakarta", 235000)
m4 = Mhs("Eve", 104, "Boyolali", 240000)
m5 = Mhs("Fin", 131, "Salatiga", 250000)
m6 = Mhs("Gilang", 123, "Klaten", 245000)
m7 = Mhs("Hana", 105, "Wonogiri", 245000)
m8 = Mhs("Isna", 213, "Klaten", 245000)
m9 = Mhs("Joni", 164, "Karanganyar", 270000)
m10 = Mhs("Killbill", 129, "Purwodadi", 265000)

Daftar = [m0,m1,m2,m3,m4,m5,m6,m7,m8,m9,m10]

def binSeMass(kumpulan, target):
    temp = []
    low = 0
    high = len(kumpulan)-1
    while low <= high :
        mid = (high+low)//2
        if kumpulan[mid] == target:
            midKiri = mid-1
            while kumpulan[midKiri] == target:
                temp.append(midKiri)
                midKiri = midKiri-1
            temp.append(mid)
            midKanan = mid+1
            while kumpulan[midKanan] == target:
                temp.append(midKanan)
                midKanan = midKanan+1
            return temp
        elif target < kumpulan[mid]:
            high = mid-1
        else:
            low = mid+1
    return False

kumpulan = [2, 4, 5, 6, 6, 6, 8, 9, 9, 10, 11, 12, 13, 13, 14]
print(binSeMass(kumpulan, 6))
