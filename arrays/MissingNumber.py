def missingNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)
    return (n*(n+1)/2) - sum(nums)


if __name__ == "__main__":
    print(missingNumber([0,1,2,4]))

