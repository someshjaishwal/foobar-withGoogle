def solution(s):
    # Your code here
    # assume s is not empty
	w = 1
	while w <= len(s):

		i, j = 0, 0

		while i < len(s):
			if(s[i] == s[j]):
				i = i+1; j = (j+1)%w
			else:
				break

		if i == len(s) and j == 0:
			return i//w

		w = w + 1

	return 1
        
s = input()
print(solution(s))
