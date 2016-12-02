def mergeSort(lst):
    # input: a list of numbers
    # output: the sorted list of those numbers
    
    if len(lst) < 2:
        return lst
        
    middle = len(lst)/2
    
    # recursively sort the sublists
    left = mergeSort(lst[:middle])
    right = mergeSort(lst[middle:])
    
    # combine the two sublists
    return merge(left, right)
    

def merge(left, right):
    # input: two sorted sublists which needs to be merged
    # output: new sorted lists which contains the two sublists
    
    i = 0
    j = 0
    mergedList = []
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            mergedList.append(left[i])
            i += 1
        else:
            mergedList.append(right[j])
            j += 1
    
    mergedList += left[i:]
    mergedList += right[j:]                
    return mergedList           
 
L = [5, 2, 4, 6, 1, 3]
print L
sortedL = mergeSort(L)
print sortedL                                                       
    
import random
randNums = random.sample(range(1, 10000000), 100000)  

sortedNums = mergeSort(randNums)                