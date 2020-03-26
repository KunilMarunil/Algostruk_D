def swap(b, p, q):
    tmp = b[p]
    b[p] = b[q]
    b[q] = tmp

#No 1
class MhsTIF(object):
    def __init__(self, nama, NIM, kota, us):
        self.nama = nama
        self.NIM = NIM
        self.kotaTinggal = kota
        self.uangSaku = us

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

def sortNim(x):
    n = len(x)
    for i in range (n -1) :
        for j in range (n-i-1) :
            if x[j].NIM > x[j+1].NIM :
                swap(x,j,j+1)

#No 2
A = [1, 3, 5, 7, 8, 12, 89, 100]
B = [2, 4, 6, 9, 10, 31, 65, 32, 123, 333, 0]
C = A + B

def sort(d):
    n = len (d)
    for i in range (n -1) :
        for j in range (n-i-1) :
            if d[j] > d[j+1] :
                swap(d,j,j+1)

#No 3
def cariPosisiTerkecil(a, dari, ke):
    terkecil = dari
    for i in range(dari+1, ke):
        if a[i] < a[terkecil]:
            terkecil = i
    return terkecil

def bubbleSort(a):
    n = len(a)
    for i in range(n-1):
        for j in range(n-i-1):
            if a[j] > a[j+1]:
                swap(a, j, j+1)

def selectionSort(a1):
    n1 = len(a1)
    for i in range(n1-1):
        IndexTerkecil = cariPosisiTerkecil(a1, i, n1)
        if IndexTerkecil != 1:
            swap(a1, i, IndexTerkecil)

def insertionSort(a):
    n = len(a)
    for i in range(1, n):
        nilai = a[i]
        pos = i
        while pos > 0 and nilai < a[pos - 1]:
            a[pos] = a[pos -1]
            pos = pos - 1
        a[pos] = nilai

from time import time as detak
from random import shuffle as kocok
k=[]
for i in range(1, 6001):
    k.append(i)
kocok(k)
u_bub = k[:]
u_sel = k[:]
u_ins = k[:]

aw = detak();bubbleSort(u_bub);ak = detak();print('bubble: %g detik' %(ak-aw));
aw = detak();selectionSort(u_sel);ak = detak();print('selection: %g detik' %(ak-aw));
aw = detak();insertionSort(u_ins);ak = detak();print('insertion: %g detik' %(ak-aw));
