#!/usr/bin/env python3

class Solution(object):
	def setZeroes(self, matrix):
		"""
		:type matrix: List[List[int]]
		:rtype: None Do not return anything, modify matrix in-place instead.
		"""
		row = len(matrix) 
		column = len(matrix[0])     
		rown = []
		coln = []
		for i in range(row):
			for j in range(column):
				if matrix[i][j] == 0:
					rown.append(i)
					coln.append(j)
					
					
					
		row2 = len(rown)
		for i in range(row2):
			for j in range(column):
				matrix[rown[i]][j]=0
			for j in range(row):
				matrix[j][coln[i]]=0