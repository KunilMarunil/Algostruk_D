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
c3 = MhsTIF('Chandra', 18, 'Surakarta', 230000)
c4 = MhsTIF('Eka', 4, 'Boyolali', 240000)
c5 = MhsTIF('Fandi', 31, 'Salatiga', 250000)
c6 = MhsTIF('Deni', 13, 'Klaten', 245000)
c7 = MhsTIF('Galuh', 5, 'Wonogiri', 245000)
c8 = MhsTIF('Janto', 23, 'Klaten', 245000)
c9 = MhsTIF('Hasan', 64, 'Karanganyar', 270000)
c10 = MhsTIF('Khalid', 29, 'Sragen', 265000)

Daftar = [c0, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]

#Nomor 1
def cariTempattinggal(a):
    a1 = []
    a2 = 0
    for i in Daftar:
        if i.kotaTinggal == str(a):
            a1.append(a2)
        a2 += 1
    return a1

#Nomor 2
def cariTerkecil(list):
    terkecil = c0.ambilUangSaku()
    for i in Daftar:
        if i.ambilUangSaku() < terkecil:
            terkecil = i.ambilUangSaku()
    return terkecil

#Nomor 3
def cariTerkecilBanyak(list):
    terkecil = c0.ambilUangSaku()
    b1 = []
    for i in Daftar:
        if i.ambilUangSaku() < terkecil:
            b1.append((i.nama, i.NIM, i.kotaTinggal, i.uangSaku))
    return b1

#Nomor 4
def kurangDari(list):
    target = 250000
    for i in Daftar:
        if i.ambilUangSaku() < target:
            print(i.ambilNama())

#Nomor 5
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def pushAw(self, data_baru):
        node_baru = Node(data_baru)
        node_baru.next = self.head
        self.head = node_baru
    def pushAk(self, data):
        if(self.head == None):
            self.head = Node(data)
        else:
            current = self.head
            while (current.next != None):
                current = current.next
            current.next = Node(data)
        return self.head
    def insert(self, data, pos):
        node = Node(data)
        if not self.head:
            self.head = node
        elif posisi == 0:
            node.next = self.head
            self.head = node
        else:
            prev = None
            current = self.head
            current_pos = 0
            while(current_pos < pos) and current.next:
               prev = current
               current = current.next
               current_pos +=1
            prev.next = node
            node.next = current
        return self.head
    def search(self, v):
        current = self.head
        while current != None:
            if current.data == v:
                return "True"
            current = current.next
        return "False"
    def display(self):
        current = self.head
        while current != None:
            print(current.data)
            current = current.next

#Nomor 6
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

#Nomor 7
ListA = [2, 3, 5, 6, 6, 6, 8, 9, 9, 10, 11, 12, 13, 13, 14]
def binSeDua(kumpulan, target):
    low = 0
    high = len(kumpulan) -1
    g = []
    while low <= high:
        if kumpulan[low] == target:
            g.append(low)
            low += 1
        else:
            low += 1
    return g

#Nomor 8
## log2(100) = 6.6438 mendekati 7
## log2(1000) = 9.9657 mendekati 10
## Dikarenakan program itu menerapkan log 2 disetiap pencariannya.
