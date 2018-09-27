'''
Read an integer n.

Without using any string methods, try to print the following:
1 2 3......n

Input Format
The first line contains an integer

source: https://www.hackerrank.com/challenges/python-print

Sample Solution:
print(*range(1, int(input())+1), sep='')

'''
#dani
if __name__ == '__main__':
    n = int(input())
    for i in range(1,n+1):
        print (i, end ="")
