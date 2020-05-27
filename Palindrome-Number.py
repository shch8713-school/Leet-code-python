class Solution:
    def isPalindrome(self, x: int) -> bool:
        y = str(x)[::-1]
        # if y == str(x):
        #     return True
        # else:
        #     return False
        return y == str(x)
