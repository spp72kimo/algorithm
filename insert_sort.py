import random

def insert_sort(x=[]):
	for i in range(1,len(x)):					# x[i]是當前檢查數字的索引位置
			temp = x[i]
			j = i - 1							# x[j]是已經檢查好的索引位置
			while temp < x[j] and j >= 0:		
				x[j + 1] = x[j]
				x[j] = temp
				j -= 1
	return x

def main():
		x = random.sample(range(100),10)		# 隨機產生10個不重複的數字List
		print('')
		print('隨機產生10個數字清單：\n', x)
		print('')
		print('排序後的數字清單：\n', insert_sort(x))

main()