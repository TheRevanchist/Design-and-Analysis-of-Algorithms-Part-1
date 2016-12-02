import heap

def maintainMedian(stream):
    out = [stream.pop(0)]
    heap_lo, heap_hi = [out[0]], []
    while stream:
        num = stream.pop(0)
        if num >= heap_lo[0]:
            heap.heap_insert(heap_hi, num, 'min')
        else:
            heap.heap_insert(heap_lo, num, 'max')    
        if len(heap_lo) > len(heap_hi) + 1:
            heap.heap_insert(heap_hi, heap.heap_extract(heap_lo, 'max'), 'min')
        if len(heap_hi) > len(heap_lo) + 1:
            heap.heap_insert(heap_lo, heap.heap_extract(heap_hi, 'min'), 'max')
        if len(heap_lo) >= len(heap_hi):
            out.append(heap_lo[0])
        else:
            out.append(heap_hi[0])
    return out
    
def main():
    stream = []
    lista = "D:/Workbench/Online Courses/Design and Analysis of Algorithms, Part 1/Programming Assignment 6/Median.txt"
    with open(lista) as file_in:
        for line in file_in:
            num = int(line.strip())
            stream.append(num)
    medians = maintainMedian(stream)
    return sum(medians) % 10000


if __name__ == '__main__':
    print main()                            
    