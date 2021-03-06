#You are going to be given an array of integers. Your job is to take that array and find an index N where the sum of the integers to the left of N is equal to the sum of the integers to the right of N. If there is no index that would make this happen, return -1.
#Let's say you are given the array {1,2,3,4,3,2,1}:
#Your function will return the index 3, because at the 3rd position of the array, the sum of left side of the index ({1,2,3}) and the sum of the right side of the index ({3,2,1}) both equal 6.
#The lowest index N where the side to the left of N is equal to the side to the right of N. If you do not find an index that fits these rules, then you will return -1.
def find_even_index(arr):
    try: return [i for i in range(len(arr)) if sum(arr[:i+1])==sum(arr[i:])][0]
    except: return -1
