#!/usr/bin/env python3

class Solution(object):
	def transpose(self, matrix):
		"""
		:type matrix: List[List[int]]
		:rtype: List[List[int]]
		"""
		row = len(matrix)
		column = len(matrix[0])
		
		new=[[None]*row for i in range (column)]
		
		
		
		for i in range(row):
			for j in range(column):
				new[j][i]= matrix[i][j]
				
		return new