#!/usr/bin/python3

s=0 #sum

for i in range(1000):
	if i%3==0 or i%5==0:
		s+=i

print(s)
