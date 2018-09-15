#find minimum and maximum nos.

import heapq

def smallest(nums):
    num = heapq.nsmallest(3,nums)[0] #prints only first smallest number
    print(num)

def largest(nums):
    num = sorted(nums)[-1] #prints largest element
    print(num)


if __name__ == "__main__":
    arr = [10,20,15,40,30,50]
    smallest(arr)
    largest(arr)
