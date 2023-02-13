# palindrome, fliping it backward should be the same.
def solution(inputString):
    if inputString[:] == inputString[::-1]:
        return True
    else : 
        return False

# the other answer by adjeko
def solution(inputString):
    return inputString == inputString[::-1]
