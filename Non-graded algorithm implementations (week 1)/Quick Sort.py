def quickSort(array, head, tail):
    # an implementation of quicksort algorithm
    
    if head >= tail:
        return
    else:
        pivot = partition(array, head, tail)
        quickSort(array, head, pivot)
        quickSort(array, pivot+1, tail)        
                        
def partition(array, head, tail):
    pivot = array[head]
    i = head + 1
    for j in range(head+1, tail):
        if array[j] < pivot:
            swap(array, i, j)
            i += 1
    swap(array, i-1, head)       
    return i-1

def swap(A, x, y ):
  A[x],A[y]=A[y],A[x]                                                                      