"""

Max-Heapify(A,i)
    l = Left(i)
    r = Right(i)
    if l <= A.heap-size and A[l] > A[i]
        largest = l
    else largest = i
    if r <= A.heap-size and A[r] > A[largest]
        largest = r
    if largest <> i
        exchange A[i] with A[largest]
        Max-Heapify(A.largest)
        
"""
def parent(i):
    return (i - 1)//2

def left(i):
    return 2 * i + 1

def right(i):
    return 2 * i + 2

class heap:
    def __init__(self, tab):
        self.length = len(tab)
        self.v = tab
        self.heapsize = 0
    def show(self):
        print("length =", self.length)
        print("heapsize =", self.heapsize)
        print("valeurs =", self.v)
    def MaxHeapify(self, i):
        l = left(i)
        r = right(i)
        if l < self.heapsize and self.v[l] > self.v[i]:
            largest = l
        else:
            largest = i
        if r < self.heapsize and self.v[r] > self.v[largest]:
            largest = r
        if largest != i:
            self.v[i], self.v[largest] = self.v[largest], self.v[i]
            self.MaxHeapify(largest)
    def BuildMaxHeap(self):
        self.heapsize = self.length
        for i in range((self.length - 1)//2, -1, -1):
            self.MaxHeapify(i)
    def Heapsort(self):
        self.BuildMaxHeap()
        for i in range(self.length -1, 0, -1):
            self.v[i], self.v[0] = self.v[0], self.v[i]
            self.heapsize -= 1
            self.MaxHeapify(0)

A = heap([16,4,10,14,7,9,3,2,8,1])
print(A.length)
A.heapsize = A.length
A.MaxHeapify(1)
A.show()