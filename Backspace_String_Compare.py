'''Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

Note that after backspacing an empty text, the text will continue empty.


Example 1:

Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".
Example 2:

Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".
Example 3:

Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".
Example 4:

Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".
Note:

1 <= S.length <= 200
1 <= T.length <= 200
S and T only contain lowercase letters and '#' characters.
Follow up:

Can you solve it in O(N) time and O(1) space?'''

class Solution (object):
    def Requal (self,str1):
        l1=[]
        k= ""
        for i in str1:
            l1.append(i)
            if i=="#" and l1.index("#")>0:
                l1.remove("#")
                l1.remove(k)
            elif i=="#" and l1.index("#")==0:
                l1.remove("#")
            else:
                k=i
        return l1
            
z=Solution()
q="#12j#fi#"
print(z.Requal(q))
