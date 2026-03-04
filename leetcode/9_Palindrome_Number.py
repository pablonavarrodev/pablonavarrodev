class Solution:
    def isPalindrome(self, x: int) -> bool:

        s = str(x)
        s2 = ""
        
        for i in range(len(s)-1, -1, -1):
            s2 = s2 + s[i]
        
        return s2 == s