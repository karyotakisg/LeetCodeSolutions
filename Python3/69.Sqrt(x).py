class Solution:
    def mySqrt(self, x: int) -> int:
        sqr = -1
        if x <= 1:
            return x
        if x== 2:
            return 1
        for i in range(x):
            sq = i*i
            if sq > x:
                sqr = i - 1
                break
            elif sq == x:
                sqr = i
                break
        return sqr