#!/usr/bin/env python3

class Solution(object):
	def maxProfit(self, prices):
		"""
		:type prices: List[int]
		:rtype: int
		"""
		length = len(prices)
		minmum = 0
		total = 0
		
		if len(prices)<=1:
			return 0
		
		total = 0
		for i in range(1,length):
			if prices[i]>prices[i-1]:
				total += prices[i]-prices[i-1]
				
		return total
	