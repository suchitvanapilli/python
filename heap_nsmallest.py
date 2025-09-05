import heapq
numbers = [5, 8, 0, 3, 6, 7, 9, 1, 2, 4]
smallest_3 = heapq.nsmallest(3, numbers)
print(smallest_3)