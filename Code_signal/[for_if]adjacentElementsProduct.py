"""
inputArray = [3, 6, -2, -5, 7, 3]
solution(inputArray) = 21
"""
def solution (inputArray):
    max_product = inputArray[0] * inputArray[1]
    for i in range(1, len(inputArray) - 1):
        current_product = inputArray[i] * inputArray[i + 1]
        if current_product > max_product:
            max_product = current_product
    return max_product
  
 # solution from salevin

def solution(inputArray):
    return max([inputArray[i] * inputArray[i+1] for i in range(len(inputArray)-1)])
  
"""
Personally think that max function made it simple. Let use more functions in the code.
"""

