class Solution:
    def reverse(self, x: int) -> int:
        if x > 0:
            y = str(x)[::-1]
            if int(y) > (2 ** 31) - 1:
                return 0 
            else:
                return int(y)
        else:
            y = str(abs(x))[::-1]
            y = int('-' + y)
            if y < (-2 ** 31):
                return 0
            else:
                return y
