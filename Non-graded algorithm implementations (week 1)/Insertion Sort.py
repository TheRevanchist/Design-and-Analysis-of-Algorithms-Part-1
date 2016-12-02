def insertionSort(A):
    # input: a list of unsorted numbers
    # output: the list of sorted numbers using insertion-sort algorithm
    
    for j in range(1, len(A)):
        key = A[j]
        i = j
        while i > 0 and A[i-1] > key:
            A[i] = A[i-1]
            i -= 1
        A[i] = key 
        
    return A  
                
        
L = [5, 2, 4, 6, 1, 3]
print L
sortedL = insertionSort(L)
print sortedL

import random
randNums = random.sample(range(1, 10000000), 10000) 
sortedNums = insertionSort(randNums) 