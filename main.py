import sys 


def dropEgg(m, j): 

	 
	if (j == 1 or j == 0): 
		return j 

	 
	if (m == 1): 
		return j 

	min = sys.maxsize 

	 
	for x in range(1, j + 1): 

		res = max(dropEgg(m - 1, x - 1), 
				dropEgg(m, j - x)) 
		if (res < min): 
			min = res 

	return min + 1


if __name__ == "__main__": 

	m = 2
	j = 10
	print("Min Trials with", 
		m, "eggs and", j, "floors is", dropEgg(m, j)) 



