class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        strdict1={}
        strdict2={}
        for i in range(len(s)):
            if s[i] in strdict1:
                strdict1[s[i]]+=1
            else:
                strdict1[s[i]]=1

        for j in range(len(t)):
            if t[j] in strdict2:
                strdict2[t[j]]+=1
            else:
                strdict2[t[j]]=1
        return strdict1==strdict2