class Solution(object):
	def twoSum(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: List[int]
		"""
		for i in nums:
			rest = target-i
			i_index = nums.index(i)
			next_index = i_index+1
			temp_nums = nums[next_index:]
			if rest in temp_nums:
				return (nums.index(i),next_index+temp_nums.index(rest))