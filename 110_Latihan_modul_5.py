def swap(b, p, q):
    tmp = b[p]
    b[p] = b[q]
    b[q] = tmp

def cariPosisiTerkecil(a, dari, ke):
    terkecil = dari
    for i in range(dari+1, ke):
        if a[i] < a[terkecil]:
            terkecil = i
    return terkecil

def bubbleSort(a):
    n = len(a)
    perbandingan = 0
    pertukaran = 0
    for i in range(n-1):
        for j in range(n-i-1):
            perbandingan+=1
            if a[j] > a[j+1]:
                pertukaran+=1
                swap(a, j, j+1)
    print("saya melakukan perbandingan", perbandingan, " kali dan perulangan ", pertukaran, " kali ")

def selectionSort(a1):
    n1 = len(a1)
    perbandingan = 0
    pertukaran = 0
    for i in range(n1-1):
        IndexTerkecil = cariPosisiTerkecil(a1, i, n1)
        perbandingan+=1
        if IndexTerkecil != 1:
            swap(a1, i, IndexTerkecil)
            pertukaran+=1
    print("saya melakukan perbandingan", perbandingan, " kali dan perulangan ", pertukaran, " kali ")

def insertionSort(a):
    n = len(a)
    for i in range(1, n):
        nilai = a[i]
        pos = i
        while pos > 0 and nilai < a[pos - 1]:
            a[pos] = a[pos -1]
            pos = pos - 1
        a[pos] = nilai

## list yang saya pakai untuk test jumlah perbandingan [10, 51, 2, 18, 4, 31, 13, 5, 23, 64, 29]

## Dengan menambahkan print di dalam perulangan maka akan terlihat berapa kali fungsi
## melakukan perbandingan dan perulangan.
