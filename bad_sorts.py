"""
This file corresponds to the first graded lab of 2XC3.
Feel free to modify and/or add functions to this file.
"""
import random
import timeit
import matplotlib.pyplot as plt


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


# ******************* Insertion sort code *******************

# This is the traditional implementation of Insertion Sort.
def insertion_sort(L):
    for i in range(1, len(L)):
        insert(L, i)


def insert(L, i):
    while i > 0:
        if L[i] < L[i-1]:
            swap(L, i-1, i)
            i -= 1
        else:
            return


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


# ******************* Bubble sort code *******************

# Traditional Bubble sort
def bubble_sort(L):
    for i in range(len(L)):
        for j in range(len(L) - 1):
            if L[j] > L[j+1]:
                swap(L, j, j+1)

def bubble_sort2(L):
    for i in range(len(L)):
        value = L[0]
        for j in range(len(L) - 1):
            if value > L[j+1]:
                L[j] = L[j+1]
            else:
                L[j] = value
                value = L[j+1]
        L[-1] = value

# ******************* Selection sort code *******************

# Traditional Selection sort
def selection_sort(L):
    for i in range(len(L)):
        min_index = find_min_index(L, i)
        swap(L, i, min_index)

def selection_sort2(L):
    for i in range(int(len(L)/2)):
        min_index = find_min_index(L, i)
        swap(L, i, min_index)

        max_index = find_max_index(L, i)
        swap(L, (-i - 1), max_index)

# Find min before finding max. Hence, n index will be smallest at that iteration. Skip to the next index for max and
#  start at n + 2. Remember to not include sorted max section in list.
def find_max_index(L,n):
    max_index = n + 1
    for i in range(n + 2, len(L) - n):
        if L[i] > L[max_index]:
            max_index = i
    return max_index

def find_min_index(L, n):
    min_index = n
    for i in range(n+1, len(L)):
        if L[i] < L[min_index]:
            min_index = i
    return min_index

#Testing
def sorted(L):
    for i in range(len(L)-1):
        if L[i] > L[i+1]:
            return False
    return True

n = 20 #Runs
s = 1000 #List Size
m = 1000 #Max List Number

average = 0
result = []

for _ in range(n):
    L = create_random_list(s, s)
    selection_sort2(L)
    if not sorted(L):
        print("List Unsorted")
        break

#EXPERIMENT 1
# for i in range(s):
#     total1 = 0
#     for _ in range(n):
#         L = create_random_list(i, m)
#
#         start = timeit.default_timer()
#         insertion_sort(L)
#         end = timeit.default_timer()
#         total1 += (end-start)
#
#     result.append(total1/n)
#
# plt.plot(result)
# plt.xlabel("List Size")
# plt.ylabel("Average Performance Time (seconds)")
# plt.show()

#EXPERIMENT 2
# for i in range(s):
#     total1 = 0
#     total2 = 0
#     for _ in range(n):
#         L = create_random_list(i,m)
#         L2 = L.copy()
#
#         start = timeit.default_timer()
#         bubble_sort(L)
#         end = timeit.default_timer()
#         total1 += end - start
#
#         start = timeit.default_timer()
#         bubble_sort2(L2)
#         end = timeit.default_timer()
#         total2 += end - start
#
#     result.append((1 - (total2/n)/(total1/n)) * 100)
#
# plt.plot(result)
# plt.xlabel("List Size")
# plt.ylabel("Average Percentage Improvement")
# plt.show()

#EXPERIMENT 3
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


