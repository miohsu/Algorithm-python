class MaxHeap(object):
    def __init__(self, lst=[], max=10000):
        self.heapList = lst
        self.currentSize = len(lst)
        self.maximum = max

    def shiftUp(self, i):
        while (i - 1) // 2 >= 0:
            if self.heapList[(i - 1) // 2] < self.heapList[i]:
                self.heapList[i], self.heapList[(i - 1) // 2] = self.heapList[(i - 1) // 2], self.heapList[i]
                i = (i - 1) // 2
            else:
                break

    def shiftDown(self, i, end):
        while i * 2 < end:
            j = i * 2 + 1
            if j + 1 <= end:
                if self.heapList[j] < self.heapList[j + 1]:
                    j += 1

            if self.heapList[i] < self.heapList[j]:
                self.heapList[i], self.heapList[j] = self.heapList[j], self.heapList[i]
                i = j
            else:
                break

    def toHeap(self):
        i = (self.currentSize - 1) // 2 - 1
        while i >= 0:
            self.shiftDown(i, self.currentSize - 1)
            i -= 1

    def heapSort(self):
        i = self.currentSize - 1
        while i > 0:
            self.heapList[0], self.heapList[i] = self.heapList[i], self.heapList[0]
            i -= 1
            self.shiftDown(0, i)


if __name__ == '__main__':
    heap = MaxHeap([1, 2, 3, 4, 5, 7, 6, 8, 9, 0, 10])
    heap.toHeap()
    print(heap.heapList)
    heap.heapSort()
    print(heap.heapList)
