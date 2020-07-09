''' Given an integer array arr, count element x such that x+1 is also in arr
if they are multiple in are, count them separately'''

class solution():
    def count(self,arr):
        x=0
        for i in arr:
            if i+1 in arr:
                x+=1
        return x

z=solution()
L=[1,2,3,4,4,5]

print(z.count(L))
