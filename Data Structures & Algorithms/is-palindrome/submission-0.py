class Solution:
    def isPalindrome(self, s: str) -> bool:
        q=''
        for i in s:
            if i.isalnum():
                q+=i.lower()      
        return q==q[::-1]        