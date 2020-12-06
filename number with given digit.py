# A Python program to print all 
# combinations of given length 
from itertools import combinations 

# Get all combinations of [1, 2, 3, 4, 5, 6, 7, 8, 9, 0] 
# and length 2 
comb = combinations([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], 3) 

# Print the obtained combinations 
for i in list(comb): 
	print (i) 
