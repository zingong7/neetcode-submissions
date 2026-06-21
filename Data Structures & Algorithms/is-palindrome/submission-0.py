class Solution:
    def isPalindrome(self, s: str) -> bool:
        l=0
        r=len(s)-1
        def isvalidalphanumeric(ch):
            if 48<=ord(ch)<=57:
                return True
            elif 97<=ord(ch.lower())<=122:
                return True
            else:
                return False
            

        while l<=r:
            if isvalidalphanumeric(s[l]) and isvalidalphanumeric(s[r]):
                if s[l].lower()==s[r].lower():
                    l+=1
                    r-=1
                else:
                    return False
            elif isvalidalphanumeric(s[l]):
                r-=1
            else:
                l+=1
        return True            
