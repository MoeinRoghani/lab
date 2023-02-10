#-------------------------------------------------------------Experiment 1-------------------------------------------------------------
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
        total1 += (end-start)

    result.append(total1/n)

plt.plot(result)
plt.xlabel("List Size")
plt.ylabel("Average Performance Time (seconds)")
plt.show()

#-------------------------------------------------------------Experiment 2-------------------------------------------------------------
for i in range(s):
    total1 = 0
    total2 = 0
    for _ in range(n):
        L = create_random_list(i,m)
        L2 = L.copy()

        start = timeit.default_timer()
        bubble_sort(L)
        end = timeit.default_timer()
        total1 += end - start

        start = timeit.default_timer()
        bubble_sort2(L2)
        end = timeit.default_timer()
        total2 += end - start

    result.append((1 - (total2/n)/(total1/n)) * 100)

plt.plot(result)
plt.xlabel("List Size")
plt.ylabel("Average Percentage Improvement")
plt.show()

#-------------------------------------------------------------Experiment 3-------------------------------------------------------------

n = 20 #runs
s = 10 #Swaps
m = 5000 #max list number

result1 = []
result2 = []
result3 = []
for i in range(s):
    total1 = 0
    total2 = 0
    total3 = 0
    for _ in range(n): #Total runs
        L = create_near_sorted_list(5000, m, s)
        L2 = L.copy()
        L3 = L.copy()

        start = timeit.default_timer()
        bubble_sort(L)
        end = timeit.default_timer()
        total1 += (end-start)

        start = timeit.default_timer()
        insertion_sort(L2)
        end = timeit.default_timer()
        total2 += (end - start)

        start = timeit.default_timer()
        selection_sort(L3)
        end = timeit.default_timer()
        total3 += (end - start)

    result1.append(total1/n)
    result2.append(total2/n)
    result3.append(total3/n)


x = range(s)
plt.plot(x,result1, label = "BubbleSort")
plt.plot(x,result2, label = "InsertionSort")
plt.plot(x,result3, label = "SelectionSort")
plt.xlabel("Number of Swaps")
plt.ylabel("Average Time")
plt.show()

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




#-------------------------------------------------------------Experiment 6-------------------------------------------------------------

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




#-------------------------------------------------------------Experiment 7-------------------------------------------------------------


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


def mergesorts_analysis():
    mergesorts = [mergesort, bottom_up_mergesort]
    mergesort_names = ['Merge Sort', 'Bottom Up Merge Sort']

    for s in mergesorts:
        arraylength = list(range(10, 10000, 10))
        time_history = []

        for i in arraylength:
            mini = 0
            maxi = max(arraylength)

            numberSamples = 1
            samples = np.random.randint(mini, maxi, (numberSamples, i))

            now = datetime.now()
            out = [s(sample) for sample in samples]
            later = datetime.now()
            time = ((later - now).total_seconds()) / numberSamples
            time_history.append(time)

        x = arraylength
        y = time_history
        plt.scatter(x, y)
        plt.plot(x, y)
        plt.title(f'Graph of {mergesort_names[mergesorts.index(s)]} Time')
        plt.xlabel('Length of our array', color='#1C2833')
        plt.ylabel('Time to Sort (Seconds)', color='#1C2833')
        plt.grid()
        plt.show()


def bottom_up_mergesort_time_improvement_percentage():
    print('Bottom Up Merge Sort Time Improvement Percentage')
    array_length = list(range(10, 10000, 10))
    time_improvements = []

    for i in array_length:
        mini = 0
        maxi = max(array_length)

        random_array = np.random.randint(mini, maxi, i)
        random_array_two = random_array.copy()

        now = datetime.now()
        mergesort(random_array)
        later = datetime.now()
        mergesort_time = ((later - now).total_seconds())

        now = datetime.now()
        bottom_up_mergesort(random_array_two)
        later = datetime.now()
        bottom_up_mergesort_time = ((later - now).total_seconds())

        time_improvements.append((bottom_up_mergesort_time - mergesort_time) / mergesort_time * 100)

    # Plotting the data considering x-axis is our n (number of iputs) and y the time for each n to be sorted
    x = array_length
    y = time_improvements
    plt.scatter(x, y)
    plt.plot(x, y)
    plt.title('Bottom up Merge Sort Improvement From Merge Sort')
    plt.xlabel('Length of our array', color='#1C2833')
    plt.ylabel('Time Increase (Percentage)', color='#1C2833')
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
algString = ['insertion sort', 'quicksort', 'mergesort']
arrayLength = list(range(3, 50, 1)) #where we have total of 47 data points on our x-axis
samples = []

#generating the list where each item of the list is a  vector of size (number of samples) for taking the average
for arrLength in arrayLength:
    #Numbers in our list can be in range of 0 to max(arrayLength) 
    mini = 0 
    maxi = max(arrayLength) 
    #samples to try and take an average
    numberSamples = 100
    #Samples is a vector of size (number of samples); where each row is a array of size 'arrLength' (our current arrayLength)
    runs = np.random.randint(mini,maxi, (numberSamples, arrLength))
    samples.append(runs)


for s in sortingAlgorithms:
    time_history = [] #reseting out time_history for each sortng algorithm

    for sample in samples:
        #Doing an avarage on 100 samples and appending the average time took to our time_history
        now = datetime.now()
        out = [s(run) for run in sample]
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