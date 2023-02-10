"""
This file corresponds to the first graded lab of 2XC3.
Feel free to modify and/or add functions to this file.

In contains traditional implementations for:
1) Quick sort
2) Merge sort
3) Heap sort

Author: Vincent Maccio
"""

import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime


# ************ Quick Sort ************
def quicksort(L):
    copy = quicksort_copy(L)
    for i in range(len(L)):
        L[i] = copy[i]


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

def dual_quicksort(L):
    copy = dual_quicksort_copy(L)
    for i in range(len(L)):
        L[i] = copy[i]


def dual_quicksort_copy(L):
    if len(L) < 2:
        return L
    pivot_one = min(L[0], L[1])
    pivot_two = max(L[0], L[1])
    left, right, middle = [], [], []
    for num in L[2:]:
        if num < pivot_one:
            left.append(num)
        elif num > pivot_two:
            right.append(num)
        else:
            middle.append(num)
    return dual_quicksort_copy(left) + [pivot_one] + dual_quicksort_copy(middle) + [pivot_two] + dual_quicksort_copy(right)


def triple_quicksort(L):
    copy = triple_quicksort_copy(L)
    for i in range(len(L)):
        L[i] = copy[i]


def triple_quicksort_copy(L):
    if len(L) < 2:
        return L

    pivot_one = min(L[0], L[1])
    pivot_three = max(L[0], L[1])
    pivot_two = L[-1]

    if pivot_two < pivot_one:
        pivot_one, pivot_two = pivot_two, pivot_one
    elif pivot_two > pivot_three:
        pivot_three, pivot_two = pivot_three, pivot_one

    left, right, middle_left, middle_right = [], [], [], []
    for num in L[3:]:
        if num < pivot_one:
            left.append(num)
        elif num > pivot_three:
            right.append(num)
        elif num < pivot_two:
            middle_left.append(num)
        else:
            middle_right.append(num)
    return triple_quicksort_copy(left) + [pivot_one] + triple_quicksort_copy(middle_left) + [pivot_two] + triple_quicksort_copy(middle_right) + [pivot_three] + triple_quicksort_copy(right)


def quadruple_quicksort(L):
    copy = quadruple_quicksort_copy(L)
    for i in range(len(L)):
        L[i] = copy[i]


def quadruple_quicksort_copy(L):
    if len(L) < 2:
        return L

    pivot_one = min(L[0], L[1])
    pivot_two = L[-1]
    pivot_three = L[-2]
    pivot_four = max(L[0], L[1])

    if pivot_two > pivot_three:
        pivot_two, pivot_three = pivot_three, pivot_two

    if pivot_two < pivot_one:
        pivot_one, pivot_two = pivot_two, pivot_one

    if pivot_three > pivot_four:
        pivot_three, pivot_four = pivot_four, pivot_three

    left, right, middle_left, middle_right, middle = [], [], [], [], []

    for num in L[4:]:
        if num < pivot_one:
            left.append(num)
        elif num > pivot_four:
            right.append(num)
        elif num < pivot_two:
            middle_left.append(num)
        elif num > pivot_three:
            middle_right.append(num)
        else:
            middle.append(num)

    return quadruple_quicksort_copy(left) + [pivot_one] + quadruple_quicksort_copy(middle_left) + [pivot_two] + quadruple_quicksort_copy(middle) + [pivot_three] + quadruple_quicksort_copy(middle_right) + [pivot_four] + quadruple_quicksort_copy(right)


def exercise6():
    sortingAlgorithms = [quicksort, dual_quicksort, triple_quicksort, quadruple_quicksort]
    algString = ['Quick Sort', 'Dual Quick Sort', 'Triple Quick Sort', "Quadruple Quick Sort"]

    for s in sortingAlgorithms:
        arrayLength = list(range(10, 10000, 100))  # where we have total of 10000/100 = 100 data points on our x-axis
        time_history = []  # reseting out time_history for each sortng algorithm

        for i in arrayLength:
            # Numbers in our list can be in range of 0 to max(arrayLength)
            mini = 0
            maxi = max(arrayLength)
            # samples to try and take an average
            numberSamples = 20
            # Samples is a vector of size (number of samples); where each row is a array of size 'i' (our current arrayLength)
            samples = np.random.randint(mini, maxi, (numberSamples, i))

            # Doing an avarage on 20 samples and appending the average time took to our time_history
            now = datetime.now()
            out = [s(sample) for sample in samples]
            later = datetime.now()
            time_history.append(((later - now).total_seconds()) / numberSamples)

        # Plotting the data considering x-axis is our n (number of iputs) and y the time for each n to be sorted
        x = arrayLength
        y = time_history
        plt.scatter(x, y)
        plt.plot(x, y)
        plt.title('Graph of %s' % algString[sortingAlgorithms.index(s)])
        plt.xlabel('Length of our array', color='#1C2833')
        plt.ylabel('Time spent to sort (Seconds)', color='#1C2833')
        plt.grid()
        plt.show()


def exercise6TimePercentage(algorithm, algorithm_to_compare):
    array_length = list(range(10, 10000, 10))
    time_increases = []

    for i in array_length:
        mini = 0
        maxi = max(array_length)

        number_samples = 20
        samples = np.random.randint(mini, maxi, (number_samples, i))
        samples_two = samples.copy()

        now = datetime.now()
        out = [algorithm(sample) for sample in samples]
        later = datetime.now()
        quicksort_time = (later - now).total_seconds() / number_samples

        now = datetime.now()
        out = [algorithm_to_compare(sample) for sample in samples_two]
        later = datetime.now()
        dual_quicksort_time = (later - now).total_seconds() / number_samples

        percentage_increase = ((dual_quicksort_time - quicksort_time) / quicksort_time) * 100
        time_increases.append(percentage_increase)

    x = array_length
    y = time_increases
    plt.scatter(x, y)
    plt.plot(x, y)
    plt.title(f'Graph of Time Advantage of {getQuickSortName(algorithm_to_compare)} over {getQuickSortName(algorithm)}')
    plt.xlabel('Length of our array', color='#1C2833')
    plt.ylabel('Time Advantage (Percentage)', color='#1C2833')
    plt.grid()
    plt.show()


def getQuickSortName(quick_sort):
    if quick_sort == quicksort:
        return 'Quick Sort'
    elif quick_sort == dual_quicksort:
        return 'Dual Quick Sort'
    elif quick_sort == triple_quicksort:
        return 'Triple Quick Sort'
    elif quick_sort == quadruple_quicksort:
        return "Quadruple Quick Sort"
    elif not quick_sort.__name__.contains('quicksort'):
        raise Exception('Not a quicksort algorithm')
    else:
        return "Unknown Quick Sort"

# *************************************


# ************ Merge Sort *************

def mergesort(L):
    if len(L) <= 1:
        return
    mid = len(L) // 2
    left, right = L[:mid], L[mid:]

    mergesort(left)
    mergesort(right)
    print("\tLeft: ", left)
    print("\tRight: ", right)
    temp = merge(left, right)
    print("\tTemp: ", temp)

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


def bottom_up_mergesort(L):
    n = len(L)
    window = 1
    while window <= n:
        for i in range(0, n, window*2):
            start = i
            mid = i + window
            end = min(i + window*2, n)
            in_place_merge(L, start, mid, end)

        window *= 2


def in_place_merge(L, start, mid, end):
    left = L[start:mid]
    right = L[mid:end]

    i = j = 0
    k = start

    while i < len(left) or j < len(right):
        if i >= len(left):
            L[k] = right[j]
            j += 1
        elif j >= len(right):
            L[k] = left[i]
            i += 1
        else:
            if left[i] <= right[j]:
                L[k] = left[i]
                i += 1
            else:
                L[k] = right[j]
                j += 1
        k += 1


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


