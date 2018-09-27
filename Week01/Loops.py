'''
Task 
Read an integer . For all non-negative integers , print . 

Input Format
The first and only line contains the integer, .

Constraints
1<n<20

Output Format
Print n lines, one corresponding to each .

source: https://www.hackerrank.com/challenges/python-loops/problem

'''
#dani
if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(i*i)

#elena
n = int(input())
for i in range(n):
    print(i**2)
