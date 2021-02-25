#!/usr/bin/env python3

class Solution(object):
	def matrixReshape(self, nums, r, c):
		"""
		:type nums: List[List[int]]
		:type r: int
		:type c: int
		:rtype: List[List[int]]
		"""
		row = len(nums)
		
		cow = len(nums[0])
		
		tot = []
		for i in range (row):
			for j in range(cow):
				tot.append(nums[i][j])
				
				
				
		if row*cow < r*c:
			return nums
		
		b=[[] for i in range(r)]
		
		for i in range(r):
			for j in range(c):
				b[i].append(tot[i*c+j])
				
		return b