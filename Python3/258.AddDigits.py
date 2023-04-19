class Solution:
    def addDigits(self, num: int) -> int:
        if num <= 9:
            return num
        return 9 if num % 9 == 0 else self.addDigits(num % 9)