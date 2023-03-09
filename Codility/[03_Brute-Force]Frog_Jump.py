"""
Task description
A small frog wants to get to the other side of the road. The frog is currently located at position X and wants to get to a position greater than or equal to Y. The small frog always jumps a fixed distance, D.

Count the minimal number of jumps that the small frog must perform to reach its target.

Write a function:

def solution(X, Y, D)

that, given three integers X, Y and D, returns the minimal number of jumps from position X to a position equal to or greater than Y.

For example, given:

  X = 10
  Y = 85
  D = 30
the function should return 3, because the frog will be positioned as follows:

after the first jump, at position 10 + 30 = 40
after the second jump, at position 10 + 30 + 30 = 70
after the third jump, at position 10 + 30 + 30 + 30 = 100
Write an efficient algorithm for the following assumptions:

X, Y and D are integers within the range [1..1,000,000,000];
X ≤ Y.
Copyright 2009–2023 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.
"""

# 1. 지점 X부터 Y까지 가거나 더 멀리가길 원한다
# 2. 뛸 수 있는 거리는 D라고 할 때 최대 몇 번 뛸 수 있나가 문제이다
# 3. Y-X = distance이고 기준이 된다.


def solution(X, Y, D): 
    distance = Y-X # distance setting을 통해 Time complexity 조절 
    if distance % D == 0: # 만약 몫이 0이 나올경우 
        return distance // D # 거리에서 뛸수있는 만큼을 나누면 된다.
    else : 
        return distance // D + 1 # 그 외의 경우는 일반적으로 -1이 부족하게 나옴으로 1을 추가 해준다.

      
      
      
      
      
      
      
      
      
      
