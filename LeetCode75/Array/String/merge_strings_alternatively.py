class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        str1 = len(word1)
        str2 = len(word2)
        output = ""

        minstr = min(str1,str2)
        
        for i in range(minstr):
            output += word1[i]
            output += word2[i]
        
        output += word1[minstr:]
        output += word2[minstr:]
            
        
        return output