def max_heapify(arr, j):
    l = left(j)
    r = right(j)
    if l < len(arr) and arr[l] > arr[j]:
        largest = l
    else:
        largest = j
    if r < len(arr) and arr[r] > arr[largest]:
        largest = r
    if largest != j:
        arr[j], arr[largest] = arr[largest], arr[j]
        max_heapify(arr, largest)
def left(j):
    return 2 * j + 1
def right(j):
    return 2 * j + 2
def max_heap(arr):
    n = int((len(arr)//2)-1)
    for j in range(n, -1, -1):
        max_heapify(arr, j)
def main():
    arr = [50, 40, 50, 10, 15, 40]
    max_heap(arr)
    print(arr)
if __name__=='__main__':
     main()
x = 'X'
p = "X"
def printX():
    w = []
    x = [2, 4, 6]
    for i in x:
        w.append(i * 2)
        return w