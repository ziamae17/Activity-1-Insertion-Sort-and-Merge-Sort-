"""
Abella, Kezzia Mae Y.

Insertion Sort(Algorithm):
Step 1: Get a list of unsorted numbers.
Step 2: Set a marker for the sorted section after the first number in the list.
Step 3: Repeat steps 4 through 6 until the unsorted section is empty.
Step 4: Select the first unsorted number.
Step 5: Swap this number to the left until it arrives at the correct sorted position.
Step 6: Advance the marker to the right one position.
Step 7: Stop.

Merge Sort(Algorithm):
Step 1: Divide the unsorted list into n sublists, until each list has only 1 element (a list of 1 element is considered sorted).
Step 2: Repeatedly merge sublists to produce new sorted sublists until there is only 1 sublist remaining. This will be the sorted list.
Step 3: Stop.
"""


import time
import random
import matplotlib.pyplot as plt


def insertionSort(myList):

    start_time = time.time()

    for index in range(1, len(myList)):
        value = myList[index]
        position = index

        """
        As long as we haven't reached the beginning and our list
        contains an element larger than the one we're trying to insert - move
        that element to the left.
        """
        
        while position > 0 and myList[position - 1] > value:
            myList[position] = myList[position -1]
            position = position - 1

        """
        We have either reached the beginning of the list or we have found
        an element of the sorted list that is smaller than the element
        we're attempt to insert at index currentPosition - 1.
        Either way - we insert the element at currentPosition
        """
        myList[position] = value

    newtime = time.time()- start_time
    runtime.append(newtime)
    print("Insertion sort execution time: %s seconds" % (newtime))
    

def mergeSort(myList):
    if len(myList) > 1:
        middle = len(myList) // 2
        left = myList[:middle]
        right = myList[middle:]

        """ Recursive call on each half """
        mergeSort(left)
        mergeSort(right)

        """ Two iterators for traversing the two halves """
        x = 0
        y = 0
        
        """ Iterator for the main list """
        z = 0
        
        while x < len(left) and y < len(right):
            if left[x] < right[y]:
              """ The value from the left half has been used """
              myList[z] = left[x]
              """ Move the iterator forward """
              x += 1
            else:
                myList[z] = right[y]
                y += 1
            """ Move to the next slot """
            z += 1

        """ For all the remaining values """
        while x < len(left):
            myList[z] = left[x]
            x += 1
            z += 1

        while y < len(right):
            myList[z]=right[y]
            y += 1
            z += 1


myList = []
items = [10,50,100,300,500,700,1000,10000]
runtime = []
mergeRuntime = [] 

for i in items:    
    for x in range(0,i):
        z = random.randint(0,i)
        myList.append(z)

    insertionSort(myList)
    start_time = time.time()
    mergeSort(myList)
    newtime = time.time()- start_time
    mergeRuntime.append(newtime)
    print("Insertion sort execution time: %s seconds" % (newtime))
    print(myList)

    
plt.plot(items, runtime, label = "Insertion sort")
plt.plot(items, mergeRuntime, label = "Merge sort")
plt.xlabel("Number of Integers")
plt.ylabel("Runtime")
plt.title("Runtime Differences between Insertion sort and Merge sort")
plt.legend()
plt.show()


