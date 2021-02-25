#!/usr/bin/env python3

class Solution(object):
	def spiralOrder(self, matrix):
		"""
		:type matrix: List[List[int]]
		:rtype: List[int]
		"""
		result=[]
		r = len(matrix)
		c = len(matrix[0])
		if r == 0:
			return []
		
		top = 0
		bottom = r
		left = 0
		right = c
		
		while top<bottom and left<right:
			for i in range(left,right):
				result.append(matrix[top][i])
				
			for i in range(top+1,bottom-1):
				result.append(matrix[i][right-1])
				
				
			if bottom!= top+1:
				for i in range(right-1,left-1,-1):
					result.append(matrix[bottom-1][i])
					
					
			if left != right -1:
				for i in range(bottom-2,top,-1):
					result.append(matrix[i][left])
					
			top +=1
			bottom -=1
			left = left +1
			right-=1
			
			
		return result