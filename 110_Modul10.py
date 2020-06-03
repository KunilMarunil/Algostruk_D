from timeit import timeit

def jumlahkan_cara_1(n):
    hasilnya = 0
    for i in range(n):
        hasilnya = hasilnya + 1
    return hasilnya

def jumlahkan_cara_2(n):
    return (n*(n+1))/2

def insertionSort(a):
    n = len(a)
    for i in range(1, n):
        nilai = a[i]
        pos = i
        while pos > 0 and nilai < a[pos - 1]:
            a[pos] = a[pos - 1]
            pos = pos - 1
            a[pos - 1]
            pos = pos - 1
        a[pos] = nilai
