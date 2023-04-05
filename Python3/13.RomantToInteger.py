class Solution:
    def romanToInt(self, s: str) -> int:
        r = 0
        i=0
        for char in s:
            if char == 'I':
                if i == len(s)-1:
                    r += 1
                elif s[i+1] == 'V'or s[i+1] == 'X':
                    r += -1   
                else:
                    r += 1        
            elif char == 'V':
                r += 5
            elif char == 'X':
                if i == len(s)-1:
                    r += 10
                elif s[i+1] == 'L' or s[i+1] == 'C':
                    r += -10
                else:
                    r += 10
            elif char == 'L':
                r += 50
            elif char == 'C':
                if i == len(s)-1:
                    r += 100
                elif s[i+1] == 'D' or s[i+1] == 'M':
                    r += -100
                else:
                    r += 100 
            elif char == 'D':
                r += 500
            elif char == 'M':
                r += 1000
            i += 1
        return r
                