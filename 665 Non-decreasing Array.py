#!/usr/bin/env python3

class Solution:
	def checkPossibility(self, nums: List[int]) -> bool:
		if len(nums) < 2: 
			return True 
		
		cnt=0 
		
		for i in range( 1, len(nums) ): 
			if nums[i-1]>nums[i]: 
				cnt = cnt + 1 
				
				if i == 1 or nums[i-2] <= nums[i]: 
					nums[i-1] = nums[i] 
				else: nums[i] = nums[i-1] 
				
				if cnt > 1: 
					return False
				
				
		return True
	


class Solution(object):
	def checkPossibility(self, nums):
		"""
		:type nums: List[int]
		:rtype: bool
		"""
		
		now = nums[0]
		change = True
		for index in range(1, len(nums)):
			if nums[index] >= now:
				now = nums[index]
			elif change:
				if index == 1 or nums[index - 2] <= nums[index]:
					now = nums[index]
				change = False
			else:
				return False
			
		return True