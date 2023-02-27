"""
input :
arr = [4, 2, 9, 7, 5, 6, 7, 1, 3]
k = 4
"""

# First method : Using remove function for array, less time complexity
# 1st iteration remove max num 9, 2nd iteration remove max num 7, 3rd iteration remove max num 7
# 4th max num is 6, which in case for k = 4. 

def solution (arr, k):
  for i in range(k-1):
    arr.remove(max(arr))
   return max(arr)
    
  
# Second improving time complexity. 

def solution(arr, k):
  n = len(arr)
  arr.sort()
  return arr[n-k] # 10-5

# Thrid the best method for time complexity. 
import heapq

def solution(arr, k):
  arr = [-elem for elem in arr]
  heapq.heapify(arr)
  for i in range(k-1):
    heapq.happop(arr)
  return -heapq.heappop(arr)


