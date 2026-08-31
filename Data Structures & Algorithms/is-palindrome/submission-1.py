class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = "".join(c.lower() for c in s if c.isalnum())
        left, right = 0, len(cleaned)-1

        if len(cleaned) == 0:
            return True

        while left != right and left < right:
            if cleaned[left] != cleaned[right]:
                return False

            left +=1
            right -=1
        
        return True