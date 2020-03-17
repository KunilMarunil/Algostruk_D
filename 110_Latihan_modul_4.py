class MhsTIF(object):
    def __init__(self, nama, NIM, kota, us):
        self.nama = nama
        self.NIM = NIM
        self.kotaTinggal = kota
        self.uangSaku = us
    def ambilNama(self):
        return self.nama
    def ambilNIM(self):
        return self.NIM
    def ambilUangSaku(self):
        return self.uangSaku

c0 = MhsTIF('Ika', 10, 'Sukoharjo', 240000)
c1 = MhsTIF('Budi', 51, 'Sragen', 230000)
c2 = MhsTIF('Ahmad',2, 'Surakarta', 250000)
c3 = MhsTIF('Chandra', 18, 'Surakarta', 235000)
c4 = MhsTIF('Eka', 4, 'Boyolali', 240000)
c5 = MhsTIF('Fandi', 31, 'Salatiga', 250000)
c6 = MhsTIF('Deni', 13, 'Klaten', 245000)
c7 = MhsTIF('Galuh', 5, 'Wonogiri', 245000)
c8 = MhsTIF('Janto', 23, 'Klaten', 245000)
c9 = MhsTIF('Hasan', 64, 'Karanganyar', 270000)
c10 = MhsTIF('Khalid', 29, 'Sragen', 265000)

Daftar = [c0, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]

def cariTerkecil(list):
    terkecil = c0.ambilUangSaku()
    for i in Daftar:
        if i.ambilUangSaku() < terkecil:
            terkecil = i.ambilUangSaku()
    return terkecil

def cariTerbesar(list):
    terbesar = c0.ambilUangSaku()
    for i in Daftar:
        if i.ambilUangSaku() > terbesar:
            terbesar = i.ambilUangSaku()
    return terbesar

def kurangDariGocap(list):
    target = 250000
    for i in Daftar:
        if i.ambilUangSaku() < target:
            print(i.ambilNama())

def lebihDariGocap(list):
    target = 250000
    for i in Daftar: 
        if i.ambilUangSaku() > target:
            print(i.ambilNama())

##Ini halaman selanjutnya
CeritanyaList = [2, 4, 5, 10, 13, 18, 23, 29, 31, 51, 64]

def binSe(kumpulan, target):
    low = 0
    high = len(kumpulan) -1
    while low <= high:
        mid = (low + high) // 2
        if kumpulan[mid] == target:
            return "Ada di " + str(mid)
            break
        elif target < kumpulan[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return False

