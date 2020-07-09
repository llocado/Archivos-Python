class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k=nums.count(0)
        for i in range(k):
            nums.remove(0)
            nums.append(0)
        return(nums)
x=Solution()
L=[1,0,2,2,0,5,4,0,8,3]
print(x.moveZeroes(L))