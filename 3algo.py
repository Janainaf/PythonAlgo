# Sorted Squared Array

#   Write a function that takes in a non-empty array of integers that are sorted
#   in ascending order and returns a new array of the same length with the squares
#   of the original integers also sorted in ascending order.

#   Sample Input
#   array   = [1, 2, 3, 5, 6, 8, 9]
#   Sample Out
#   array =   [1, 4, 9, 25, 36, 64, 81]


# def sortedSquaredArray(array):
#     # Write your code here.
#     return []
    
def sortedSquaredArray(array):
    result = []
    for n in array:
        result = result + [n**2]
    result.sort()
    return result

   
sortedSquaredArray([1, 2, 3])
