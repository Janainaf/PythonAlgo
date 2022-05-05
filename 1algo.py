def twoNumberSum(array, targetSum):
    sum = []
    for i in array:
        for index, _ in enumerate(array): 
            if i != array[index]:
                if i + array[index] == targetSum:
                    return ([i, array[index]]) 
		
    return sum
			# Write your code here.
    pass


print(twoNumberSum([-21, 301, 12, 4, 65, 56, 210, 356, 9, -47], 164))
print(twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 10))


