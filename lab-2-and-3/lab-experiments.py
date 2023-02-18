# -------------------------------------------------------------Experiment 1-------------------------------------------------------------
import random
import timeit
import matplotlib.pyplot as plt

for i in range(s):
    total1 = 0
    for _ in range(n):
        L = create_random_list(i, m)

        start = timeit.default_timer()
        insertion_sort(L)
        end = timeit.default_timer()
        total1 += (end - start)

    result.append(total1 / n)

plt.plot(result)
plt.xlabel("List Size")
plt.ylabel("Average Performance Time (seconds)")
plt.show()


# -------------------------------------------------------------Experiment 2-------------------------------------------------------------
# ******************* Bubble sort code *******************

# Traditional Bubble sort
def bubble_sort(L):
    for i in range(len(L)):
        for j in range(len(L) - 1):
            if L[j] > L[j + 1]:
                swap(L, j, j + 1)


def bubble_sort2(L):
    for i in range(len(L)):
        value = L[0]
        for j in range(len(L) - 1):
            if value > L[j + 1]:
                L[j] = L[j + 1]
            else:
                L[j] = value
                value = L[j + 1]
        L[-1] = value


# ******************* Selection sort code *******************

# Traditional Selection sort
def selection_sort(L):
    for i in range(len(L)):
        min_index = find_min_index(L, i)
        swap(L, i, min_index)


def selection_sort2(L):
    for i in range(int(len(L) / 2)):
        min_index = find_min_index(L, i)
        swap(L, i, min_index)

        max_index = find_max_index(L, i)
        swap(L, (-i - 1), max_index)


# Find min before finding max. Hence, n index will be smallest at that iteration. Skip to the next index for max and
#  start at n + 2. Remember to not include sorted max section in list.
def find_max_index(L, n):
    max_index = n + 1
    for i in range(n + 2, len(L) - n):
        if L[i] > L[max_index]:
            max_index = i
    return max_index


def find_min_index(L, n):
    min_index = n
    for i in range(n + 1, len(L)):
        if L[i] < L[min_index]:
            min_index = i
    return min_index


for i in range(s):
    total1 = 0
    total2 = 0
    for _ in range(n):
        L = create_random_list(i, m)
        L2 = L.copy()

        start = timeit.default_timer()
        bubble_sort(L)
        end = timeit.default_timer()
        total1 += end - start

        start = timeit.default_timer()
        bubble_sort2(L2)
        end = timeit.default_timer()
        total2 += end - start

    result.append((1 - (total2 / n) / (total1 / n)) * 100)

plt.plot(result)
plt.xlabel("List Size")
plt.ylabel("Average Percentage Improvement")
plt.show()

# -------------------------------------------------------------Experiment 3-------------------------------------------------------------

n = 20  # runs
s = 10  # Swaps
m = 5000  # max list number

result1 = []
result2 = []
result3 = []
for i in range(s):
    total1 = 0
    total2 = 0
    total3 = 0
    for _ in range(n):  # Total runs
        L = create_near_sorted_list(5000, m, s)
        L2 = L.copy()
        L3 = L.copy()

        start = timeit.default_timer()
        bubble_sort(L)
        end = timeit.default_timer()
        total1 += (end - start)

        start = timeit.default_timer()
        insertion_sort(L2)
        end = timeit.default_timer()
        total2 += (end - start)

        start = timeit.default_timer()
        selection_sort(L3)
        end = timeit.default_timer()
        total3 += (end - start)

    result1.append(total1 / n)
    result2.append(total2 / n)
    result3.append(total3 / n)

x = range(s)
plt.plot(x, result1, label="BubbleSort")
plt.plot(x, result2, label="InsertionSort")
plt.plot(x, result3, label="SelectionSort")
plt.xlabel("Number of Swaps")
plt.ylabel("Average Time")
plt.show()

# -------------------------------------------------------------Experiment 4-------------------------------------------------------------

import matplotlib.pyplot as plt
import autograd.numpy as np
from datetime import datetime

sortingAlgorithms = [quicksort, mergesort, heapsort]
algString = ['quicksort', 'mergesort', 'heapsort']

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

# -------------------------------------------------------------Experiment 5-------------------------------------------------------------

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
        for i in range(0, average_samples):
            sample = create_near_sorted_list(length, length, l)
            out = s(sample)
        later = datetime.now()
        time_history.append(((later - now).total_seconds()) / average_samples)

    x = swaps
    y = time_history
    plt.scatter(x, y)
    plt.plot(x, y)
    plt.title('Graph of %s' % algString[sortingAlgorithms.index(s)])
    plt.xlabel('Number of swaps', color='#1C2833')
    plt.ylabel('Time spent to sort (Seconds)', color='#1C2833')
    plt.grid()
    plt.show()


# -------------------------------------------------------------Experiment 6-------------------------------------------------------------


# -------------------------------------------------------------Experiment 7-------------------------------------------------------------


# -------------------------------------------------------------Experiment 8-------------------------------------------------------------

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
algString = ['insertion sort', 'quicksort', 'mergesort']
arrayLength = list(range(3, 50, 1))  # where we have total of 47 data points on our x-axis
samples = []

# generating the list where each item of the list is a  vector of size (number of samples) for taking the average
for arrLength in arrayLength:
    # Numbers in our list can be in range of 0 to max(arrayLength)
    mini = 0
    maxi = max(arrayLength)
    # samples to try and take an average
    numberSamples = 100
    # Samples is a vector of size (number of samples); where each row is a array of size 'arrLength' (our current arrayLength)
    runs = np.random.randint(mini, maxi, (numberSamples, arrLength))
    samples.append(runs)

for s in sortingAlgorithms:
    time_history = []  # reseting out time_history for each sortng algorithm

    for sample in samples:
        # Doing an avarage on 100 samples and appending the average time took to our time_history
        now = datetime.now()
        out = [s(run) for run in sample]
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