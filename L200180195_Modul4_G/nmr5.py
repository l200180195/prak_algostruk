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

def cariLinkedList(head, target):
    temp = head
    while temp.data != None:
        if temp.data == target:
            return temp
    return -1
