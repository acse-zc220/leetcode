#!/usr/bin/env python3

class Solution(object):
	def plusOne(self, digits):
		"""
		:type digits: List[int]
		:rtype: List[int]
		"""
		n = len(digits)
		
		for i in reversed(range(n)):
			if digits[i]==9:
				digits[i] = 0
			else:
				digits[i]+=1
				return digits
			
		digits[0] = 1
		digits.append(0)
		return digits