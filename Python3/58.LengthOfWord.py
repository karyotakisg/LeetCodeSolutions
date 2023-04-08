class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ans = 0
        flag = False
        for i in range (len(s)-1,-1,-1):
            if s[i] != " ":
                flag = True
            if flag == True:
                if s[i] != " ":
                    ans += 1
                else:
                    break
        if flag == False:
            return len(s)
        return ans