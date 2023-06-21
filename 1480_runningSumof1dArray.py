def runningSum(nums):
    r_sum=[]
    k=0
    for i in range(len(nums)):
        k+=nums[i]
        r_sum.append(k)
    return r_sum