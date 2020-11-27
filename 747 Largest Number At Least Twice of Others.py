
class Solution(object):
    def dominantIndex(self, nums):
        m = max(nums)
        if all(m >= 2*x for x in nums if x != m):
            return nums.index(m)
        return -1
    
class Solution(object):
    def dominantIndex(self, nums):
        maxIndex = None 
        maxValue = float(' -inf')
        secValue = float(' -inf')
        for i in range(len(nums)):
            if  maxValue < nums[i]:
                secValue = maxValue
                maxValue = nums[i]
                maxIndex = i
                # secValue < nums[i] < maxValue
            elif secValue < nums[i]:
                secValue = nums[i]
        if secValue *2 <= maxValue:
            return maxIndex
        return -1