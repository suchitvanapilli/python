import heapq
numbers = [5,2,8,9,7,1,0,15,20,21]
largest_3 = heapq.nlargest(3, numbers)
print(largest_3)