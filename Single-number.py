'''Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4
'''
from collections import defaultdict

class MySolution1(object):      #Mi primera solucion al ejercicio
    def mysingleNumber1(self,nums):
        for i in nums:
            if nums.count(i)==1:
                return i
        return ("no single number found in list\n")
l1=[1,1,2,3,3]
l2=[1,1,2,2,3,3]

z1=MySolution1()
print(z1.mysingleNumber1(l1))
print(z1.mysingleNumber1(l2))
print("prueba de segunda solucion hecha por mi")
class Mysolution2(object):      #Mi segunda solucion al ejercicio, disminuyendo el time complexity usando una hash table
    def mysingleNumber2(self,nums):
        hash_table=defaultdict(int)
        for i in nums:
            hash_table[i]+=1
        print(hash_table)
        for i in hash_table:
            if hash_table[i]==1:
                return i

z2=Mysolution2()
print(z2.mysingleNumber2(l1))

class Solution1(object):        #solucion entregada por la pagina
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        no_duplicate_list = []
        for i in nums:
            if i not in no_duplicate_list:
                no_duplicate_list.append(i)
            else:
                no_duplicate_list.remove(i)
        return no_duplicate_list.pop()

x=Solution1()
print(x.singleNumber(nums=[1,1,2,2,3]))

