#Nomor 1
class stack():
    def __init__ (self) :
        self.list = []
    def Empty (self) :
        return len(self.list) == 0
    def __len__ (self) :
        return len(self.list)
    def pop(self) :
        assert not self.Empty()
        return self.list.pop()
    def push(self, data) :
        self.list.append(data)

def Hexa(data):
    a = stack()
    hxlist = "0123456789ABCDEF"
    while data != 0:
        sisa = data%16
        data = data//16
        a.push(hxlist[sisa])
    st=""
    for i in range(len(a)):
        st = st + str(a.pop())
    return st

print(Hexa(12))

print("\n")

#Nomor 2
nilai = stack()
for i in range(16) :
    if i % 3 == 0 :
        nilai.push(i)
st = ''
for i in range(len(nilai)):
        st = st +""+ str(nilai.pop())
        print (st)

print("\n")

#Nomor 3
nilai = stack ()
for i in range(16):
    if i % 3 == 0:
        nilai.push(i)
    elif i % 4 == 0:
        nilai.pop()
st = ''
for i in range(len(nilai)):
        st = st+""+ str(nilai.pop())
        print (st)

print("\n")


#Nomor 4
class Queue(object):
    def __init__(self):
        self.qlist = []

    def isEmpty(self):
        return len(self) == 0

    def __len__(self):
        return len(self.qlist)

    def enqueue(self, data):
        self.qlist.append(data)

    def dequeue(self):
        assert not self.isEmpty(), "Antrian sedang kosong"
        return self.qlist.pop()

    def getFrontMost(self):
        assert not self.isEmpty(), "Antrian sedang kosong"
        return self.qlist[0]

    def getRearMost(self):
        assert not self.isEmpty(), "Antrian sedang kosong"
        return self.qlist[-1]


q = Queue()
q.enqueue(103)
q.enqueue(44)
q.enqueue(66)

print ("Item paling depan ", q.getFrontMost())
print ("Item paling belakang " , q.getRearMost())

#Nomor 5
class PriorityQueue(object) :
    
    def __init__(self):
        self.qlist = []
        
    def __len__(self) :
        return len(self.qlist)
    
    def is_Empty(self) :
        return len(self) == 0
    
    def enqueue(self, data, priority) :
        entry = _PriorityQEntry(data, priority)
        self.qlist.append(entry)
        
    def dequeue(self) :
        A = []
        for i in self.qlist:
            A.append(i)
        b = 0
        for i in range(1, len(self.qlist)) :
            if A[i].priority < A[b].priority :
                b = i
        hasil = self.qlist.pop(b)
        return hasil.item
    
class _PriorityQEntry() :
    def __init__ (self, data, priority) :
        self.item = data
        self.priority = priority

print("\n")

S = PriorityQueue()
S.enqueue("Kunil",2)
S.enqueue("Kambing",4)
S.enqueue("Babang Tamvan",0)
S.enqueue("Cucok",2)
S.enqueue("Lekong",5)

print (S.dequeue())
print (S.dequeue())
print (S.dequeue())
print (S.dequeue())
print (S.dequeue())
