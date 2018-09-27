'''
Task 
Read two integers and print two lines. The first line should contain integer division,  // . The second line should contain float division,  / .

You don't need to perform any rounding or formatting operations.

source: https://www.hackerrank.com/challenges/python-division

Sample Solution with the method format():

a = int(input())
b = int(input())
print('{0} \n{1}'.format(a//b, a/b))
     # print("{}\n{}".format(a//b, a/b))
'''
#elena
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a//b)
    print(a/b)
