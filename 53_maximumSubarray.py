def maxSubArray(nums):
    maxadj,currmax=nums[0],nums[0]
    for i in range(1,len(nums)):
        item=nums[i]
        currmax=max(item,item+currmax)
        maxadj=max(maxadj,currmax)
    return maxadj