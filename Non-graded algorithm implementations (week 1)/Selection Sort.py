def selectionSort(A):    
    # input: a list of unsorted numbers
    # output: the list of sorted numbers using selection-sort algorithm
    
    for i in range(len(A)):
        minimum = i
        for j in range(i+1, len(A)):
            if A[j] < A[minimum]:
                minimum = j
                
        temp = A[i]
        A[i] = A[minimum]
        A[minimum] = temp
    return A     
        
L = [5, 2, 4, 6, 1, 3]
print L
sortedL = selectionSort(L)
print sortedL                      