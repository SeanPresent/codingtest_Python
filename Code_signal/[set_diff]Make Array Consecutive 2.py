"""
Ratiorg got statues of different sizes as a present from CodeMaster for his birthday, 
each statue having an non-negative integer size. Since he likes to make things perfect, 
he wants to arrange them from smallest to largest so that each statue will be bigger than the previous one exactly by 1. 
He may need some additional statues to be able to accomplish that. Help him figure out the minimum number of additional statues needed.

"""
statues = [6, 2, 3, 8]
def solution(statues):
    count_list = [i for i in range(min(statues), max(statues))]
    intersec = set(count_list) - set(statues) #차집합
    return len(intersec) 

solution(statues)
