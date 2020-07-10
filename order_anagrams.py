from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        table=defaultdict(list)
        
z=Solution()
print(z.groupAnagrams(["abc","adc","erb","bce"]))