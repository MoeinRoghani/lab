"""
This file corresponds to the first graded lab of 2XC3.
Feel free to modify and/or add functions to this file.

In contains traditional implementations for:
1) Quick sort
2) Merge sort
3) Heap sort

Author: Vincent Maccio
"""

# ************ Quick Sort ************
def quicksort(L):
    copy = quicksort_copy(L)
    for i in range(len(L)):
        L[i] = copy[i]
    #return(L)

def quicksort_copy(L):
    if len(L) < 2:
        return L
    pivot = L[0]
    left, right = [], []
    for num in L[1:]:
        if num < pivot:
            left.append(num)
        else:
            right.append(num)
    return quicksort_copy(left) + [pivot] + quicksort_copy(right)

# *************************************


# ************ Merge Sort *************

def mergesort(L):
    if len(L) <= 1:
        return
    mid = len(L) // 2
    left, right = L[:mid], L[mid:]

    mergesort(left)
    mergesort(right)
    temp = merge(left, right)

    for i in range(len(temp)):
        L[i] = temp[i]


def merge(left, right):
    L = []
    i = j = 0

    while i < len(left) or j < len(right):
        if i >= len(left):
            L.append(right[j])
            j += 1
        elif j >= len(right):
            L.append(left[i])
            i += 1
        else:
            if left[i] <= right[j]:
                L.append(left[i])
                i += 1
            else:
                L.append(right[j])
                j += 1
    return L

# *************************************

# ************* Heap Sort *************

def heapsort(L):
    heap = Heap(L)
    for _ in range(len(L)):
        heap.extract_max()

class Heap:
    length = 0
    data = []

    def __init__(self, L):
        self.data = L
        self.length = len(L)
        self.build_heap()

    def build_heap(self):
        for i in range(self.length // 2 - 1, -1, -1):
            self.heapify(i)

    def heapify(self, i):
        largest_known = i
        if self.left(i) < self.length and self.data[self.left(i)] > self.data[i]:
            largest_known = self.left(i)
        if self.right(i) < self.length and self.data[self.right(i)] > self.data[largest_known]:
            largest_known = self.right(i)
        if largest_known != i:
            self.data[i], self.data[largest_known] = self.data[largest_known], self.data[i]
            self.heapify(largest_known)

    def insert(self, value):
        if len(self.data) == self.length:
            self.data.append(value)
        else:
            self.data[self.length] = value
        self.length += 1
        self.bubble_up(self.length - 1)

    def insert_values(self, L):
        for num in L:
            self.insert(num)

    def bubble_up(self, i):
        while i > 0 and self.data[i] > self.data[self.parent(i)]:
            self.data[i], self.data[self.parent(i)] = self.data[self.parent(i)], self.data[i]
            i = self.parent(i)

    def extract_max(self):
        self.data[0], self.data[self.length - 1] = self.data[self.length - 1], self.data[0]
        max_value = self.data[self.length - 1]
        self.length -= 1
        self.heapify(0)
        return max_value

    def left(self, i):
        return 2 * (i + 1) - 1

    def right(self, i):
        return 2 * (i + 1)

    def parent(self, i):
        return (i + 1) // 2 - 1

    def __str__(self):
        height = math.ceil(math.log(self.length + 1, 2))
        whitespace = 2 ** height
        s = ""
        for i in range(height):
            for j in range(2 ** i - 1, min(2 ** (i + 1) - 1, self.length)):
                s += " " * whitespace
                s += str(self.data[j]) + " "
            s += "\n"
            whitespace = whitespace // 2
        return s

# *************************************



#-------------------------------------------------------------Experiment 4-------------------------------------------------------------
    
import matplotlib.pyplot as plt
import autograd.numpy as np   
from datetime import datetime


sortingAlgorithms = [quicksort, mergesort, heapsort]
algString = ['quicksort', 'mergesort', 'heapsort']

for s in sortingAlgorithms:
    arrayLength = list(range(10, 10000, 100)) #where we have total of 10000/100 = 100 data points on our x-axis
    time_history = [] #reseting out time_history for each sortng algorithm

    for i in arrayLength:
        #Numbers in our list can be in range of 0 to max(arrayLength) 
        mini = 0 
        maxi = max(arrayLength) 
        #samples to try and take an average
        numberSamples = 20
        #Samples is a vector of size (number of samples); where each row is a array of size 'i' (our current arrayLength)
        samples = np.random.randint(mini,maxi, (numberSamples, i))

        #Doing an avarage on 20 samples and appending the average time took to our time_history
        now = datetime.now()
        out = [s(sample) for sample in samples]
        later = datetime.now()
        time_history.append(((later - now).total_seconds())/numberSamples)

    # Plotting the data considering x-axis is our n (number of iputs) and y the time for each n to be sorted
    x = arrayLength 
    y = time_history
    plt.scatter(x, y)
    plt.plot(x, y)
    plt.title('Graph of %s' %algString[sortingAlgorithms.index(s)])
    plt.xlabel('Length of our array', color='#1C2833')
    plt.ylabel('Time spent to sort (Seconds)', color='#1C2833')
    plt.grid()
    plt.show()




#-------------------------------------------------------------Experiment 5-------------------------------------------------------------

import random


# Create a random list length "length" containing whole numbers between 0 and max_value inclusive
def create_random_list(length, max_value):
    return [random.randint(0, max_value) for _ in range(length)]


# Creates a near sorted list by creating a random list, sorting it, then doing a random number of swaps
def create_near_sorted_list(length, max_value, swaps):
    L = create_random_list(length, max_value)
    L.sort()
    for _ in range(swaps):
        r1 = random.randint(0, length - 1)
        r2 = random.randint(0, length - 1)
        swap(L, r1, r2)
    return L


# I have created this function to make the sorting algorithm code read easier
def swap(L, i, j):
    L[i], L[j] = L[j], L[i]



sortingAlgorithms = [quicksort, mergesort, heapsort]
algString = ['quicksort', 'mergesort', 'heapsort']

for s in sortingAlgorithms:

        time_history = []
        length = 1000
        numberOfTests = 20
        swaps = list(range(1, 500, 10))
        for l in swaps:
            now = datetime.now()
            average_samples = 10
            for i in range(0,average_samples):
                sample = create_near_sorted_list(length, length, l)  
                out = s(sample)
            later = datetime.now()
            time_history.append(((later - now).total_seconds())/average_samples)

        x = swaps 
        y = time_history
        plt.scatter(x, y)
        plt.plot(x, y)
        plt.title('Graph of %s' %algString[sortingAlgorithms.index(s)])
        plt.xlabel('Number of swaps', color='#1C2833')
        plt.ylabel('Time spent to sort (Seconds)', color='#1C2833')
        plt.grid()
        plt.show()




#-------------------------------------------------------------Experiment 8-------------------------------------------------------------

# ******************* Insertion sort code *******************
# This is the optimization/improvement we saw in lecture
def insertion_sort2(L):
    for i in range(1, len(L)):
        insert2(L, i)


def insert2(L, i):
    value = L[i]
    while i > 0:
        if L[i - 1] > value:
            L[i] = L[i - 1]
            i -= 1
        else:
            L[i] = value
            return
    L[0] = value

sortingAlgorithms = [insertion_sort2, quicksort, mergesort]
algString = ['insertion_sort2', 'quicksort', 'mergesort']

for s in sortingAlgorithms:
    arrayLength = list(range(3, 50, 1)) #where we have total of 47 data points on our x-axis
    time_history = [] #reseting out time_history for each sortng algorithm

    for i in arrayLength:
        #Numbers in our list can be in range of 0 to max(arrayLength) 
        mini = 0 
        maxi = max(arrayLength) 
        #samples to try and take an average
        numberSamples = 100
        #Samples is a vector of size (number of samples); where each row is a array of size 'i' (our current arrayLength)
        samples = np.random.randint(mini,maxi, (numberSamples, i))

        #Doing an avarage on 100 samples and appending the average time took to our time_history
        now = datetime.now()
        out = [s(sample) for sample in samples]
        later = datetime.now()
        time_history.append(((later - now).total_seconds())/numberSamples)

    # Plotting the data considering x-axis is our n (number of iputs) and y the time for each n to be sorted
    x = arrayLength 
    y = time_history
    plt.scatter(x, y)
    plt.plot(x, y)
    plt.title('Graph of %s' %algString[sortingAlgorithms.index(s)])
    plt.xlabel('Length of our array', color='#1C2833')
    plt.ylabel('Time spent to sort (Seconds)', color='#1C2833')
    plt.grid()
    plt.show()