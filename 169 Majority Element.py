#!/usr/bin/env python3

class Solution(object):
	def majorityElement(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		index, cnt=0,1
		for i in range(1,len(nums)):
			if nums[index] == nums[i]:
				cnt += 1
			else:
				cnt -= 1
				if cnt == 0:
					index = i
					cnt = 1
					
		return nums[index]
	
#dict()
	def majorityElement(self, nums: List[int]) -> int:
			check = {}
		
			for number in nums:
				if number in check:
					check[number] += 1
				else:
					check[number] = 1
					
			for key in check:
				if check[key] > len(nums) / 2:
					return key
				
			return None