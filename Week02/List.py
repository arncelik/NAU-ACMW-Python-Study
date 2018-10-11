'''
Problem source: https://www.hackerrank.com/challenges/list-comprehensions/problem
Please write your solution below
'''
'''
ELENA 
x=int(input("Enter a number:"))
y=int(input("Enter a number:"))
z=int(input("Enter a number:"))
n=int(input("Enter a number:"))
list=[]
count=0
for i in range(x+1):
  for j in range(y+1):
    for k in range(z+1):
      if i+j+k!=n:
        list.append([])
        list[count]=[i,j,k]
        count=count+1
print (list)

'''
