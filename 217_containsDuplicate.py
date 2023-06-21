def containsDuplicate(nums):
    what_we_saw = set()
    
    for i in nums:
        if i in what_we_saw:
            return True
        what_we_saw.add(i)
    return False