#!/usr/bin/python3

def pascal_triangle(n):
	"Function that returns pascals triangle"
	ans = []
	if n > 0:
		for i in range(1, n + 1):
			row = []
			C = 1
			for j in range(1, i + 1):
				row.append(C)
				C = C * (i - j) // j
			ans.append(row)
	return ans
