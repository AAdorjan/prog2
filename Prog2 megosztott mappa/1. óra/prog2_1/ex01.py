# 1. Exercise
# Write a Python function to find and return maximum and the minimum
# value in a set
import sys

def findMinAndMax(set):
    li = list(set)
    min = float('inf') #li[0]
    max = float('-inf')
    for n in li:
        if n < min:
            min = n
        if n > max:
            max = n
    return (min,max)


def findMinAndMax2(set):
    return (min(set),max(set))

s = {2,6,4,7,8}
(min,max) = findMinAndMax(s)
print("Minimum of the set: ",min)
print("Maximum of the set: ",max)
