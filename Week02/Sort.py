'''
Problem:
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. 
You are given n scores. 
Store them in a list and find the score of the runner-up.

Sample Solution:
n = int(input())
arr = list(map(int, input().split()))
first = max(arr)
i=0
while(i<n):
    if first ==max(arr):
        arr.remove(max(arr))
    i+=1
print(max(arr))
'''

# ELENA 

list=[]
count=0
num=int(input("how many players: "))
while count<num:
  score=int(input("What is your score: "))

  list.append(score)
  count=count+1

list.sort()
print("The winner is the one with ", list[-1], "points")

