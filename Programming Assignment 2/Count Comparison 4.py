# An implementation of quicksort algorithm using a random element 
# as pivot. In addition, it prints the total number of comparisons
# This part of the assignment isn't graded

import random
# the global variable which counts the comparisons
count = 0

def quickSort(array, head, tail):
    # an implementation of quicksort algorithm
    # inputs: 
    #    array - an unsorted array of numbers
    #    head - the index of the first element in array, 0
    #    tail - the index of the last element in array, -1
    
    if head >= tail:
        return
    else:
        pivot = partition(array, head, tail)
        quickSort(array, head, pivot)
        quickSort(array, pivot+1, tail)        
                        
def partition(array, head, tail):
    # the implementation of the partition method
    # inputs: same as in the previous method
    # output: the index of pivot 
        
    global count
    a = random.randint(head, tail)
    swap(array, head, a)
    pivot = array[head]
    i = head + 1
    count += tail - head - 1
    for j in range(head+1, tail):
        if array[j] < pivot:
            swap(array, i, j)
            i += 1
    swap(array, i-1, head)       
    return i-1

def swap(A, x, y ):
  # a helper method which swaps two elements in an array  
  
  A[x],A[y]=A[y],A[x]                                                                        

# read the file                        
lista = "D:/Workbench/Online Courses/Design and Analysis of Algorithms, Part 1/Programming Assignment 2/text.txt" 
f = open(lista, 'r')
array = []
for line in f: array.append(int(line)) 

# sort it and print the number of comparisons
quickSort(array, 0, len(array))  
print count                                                                                                                                  