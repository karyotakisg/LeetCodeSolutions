class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        smallest_word= len(strs[0])
        pr = ""
        for word in strs:
            if len(word) < smallest_word:
                smallest_word = len(word)
        for i in range(smallest_word): 
            counter = 0
            for word in strs:
                if strs[0][i] == word[i]:
                    counter += 1
            if counter == len(strs):
                pr += strs[0][i]
            else:
                break                   
        return pr
