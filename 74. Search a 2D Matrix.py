#!/usr/bin/env python3

class Solution(object):
	def searchMatrix(self, matrix, target):
		"""
		:type matrix: List[List[int]]
		:type target: int
		:rtype: bool
		"""
		r = len(matrix)
		c = len(matrix[0])
		if r == 0: 
			return False
		r1, r2 = 0, r-1
		
		while r1 < r2:
			mid = r1 + (r2-r1)//2
			if matrix[mid][c-1] < target: r1 = mid+1
			elif matrix[mid][0] > target: r2 = mid-1
			else:
				r1 = mid
				break
			
		c1, c2 = 0, c-1;
		while c1 <= c2:
			mid = c1 + (c2-c1)//2
			if matrix[r1][mid] < target: c1 = mid+1
			elif matrix[r1][mid] > target: c2 = mid-1
			else: return True
			
		return False