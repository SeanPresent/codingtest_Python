"""

# Question is and code is from : https://youtu.be/Peq4GCPNC5c?t=413

"""
arr = [2, 4, 5, 5, 5, 5, 7, 9, 9]
target = 5
output = [2,6] # answer is a list type, gotta keep brackets for the answer. 

def solution(arr, target):
  for i in range(len(arr)):
    if arr[i] == target :
      start = i
      while i+1 < len(arr) and arr[i+1] == target :
        i += 1 
       return [start, i]
   return [-1, 1] # in case, there is no target value in array.


print(solution(arr, target))

