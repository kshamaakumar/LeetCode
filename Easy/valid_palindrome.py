class Solution:
    def isPalindrome(self, s: str) -> bool:
        punctuations = '''!()-[]{};:'`"\,<>./?@#$%^&*_~'''

        result = "".join([c.lower() for c in s if c not in punctuations])
        result = result.replace(" ", "")
        
        return self.checkPalindrome(result, 0, len(result)-1)

    def checkPalindrome(self,string,start,end):
        if start >= end:
            return True

        if string[start] != string[end]:
            return False

        return self.checkPalindrome(string, start+1, end-1)