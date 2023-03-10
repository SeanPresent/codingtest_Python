"""
An array A consisting of N different integers is given. The array contains integers in the range [1..(N + 1)], which means that exactly one element is missing.

Your goal is to find that missing element.

Write a function:

def solution(A)

that, given an array A, returns the value of the missing element.

For example, given array A such that:

  A[0] = 2
  A[1] = 3
  A[2] = 1
  A[3] = 5
the function should return 4, as it is the missing element.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..100,000];
the elements of A are all distinct;
each element of array A is an integer within the range [1..(N + 1)].
"""


# 90 percent right, time complexity

def solution(A):
    if not A:
        return A
    
    n = len(A)
    A_set = set(A)
    
    for i in range(1, n+2):
        if i not in A_set:
            return i
          
          
# 백점짜리 답 
def solution(A):
    n = len(A)
    total_sum = (n+1)*(n+2)//2
    array_sum = sum(A)
    missing_element = total_sum - array_sum
    return missing_element





