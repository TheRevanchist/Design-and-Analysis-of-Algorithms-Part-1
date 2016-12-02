def mergeSort(lst):
    # input: a list of numbers
    # output: the sorted list of those numbers
    
    if len(lst) < 2:
        return lst, 0
    
    else:        
        middle = len(lst)/2
        
        # recursively sort the sublists
        left, a = mergeSort(lst[:middle])
        right, b = mergeSort(lst[middle:])
        
        # combine the two sublists
        res, c = mergeAndCount(left, right)
        return res, (a + b + c)
        

def mergeAndCount(left, right):
    # input: two sorted sublists which needs to be merged
    # output: new sorted lists which contains the two sublists and the number of inversions
    
    i = 0
    j = 0
    inversions = 0
    mergedList = []
    l1 = len(left)
    l2 = len(right)
    
    while i < l1 and j < l2:
        if left[i] < right[j]:
            mergedList.append(left[i])
            i += 1
        else:
            mergedList.append(right[j])
            j += 1
            inversions += l1 - i
    
    mergedList += left[i:]
    mergedList += right[j:]                
    return mergedList, inversions   
    
def countInversions(lst):
    # input: the list of numbers
    # output: the number of inversions
    return mergeSort(lst)[1]        
    
lista = "D:/Workbench/Online Courses/Design and Analysis of Algorithms, Part 1/Programming Assignment 1/text.txt" 
'''content = []
with open(lista) as f:
    content = f.readlines()'''

f = open(lista, 'r')
array = []
for line in f: array.append(int(line))
      
inv = countInversions(array)



