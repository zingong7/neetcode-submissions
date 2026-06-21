class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count=defaultdict(list)
        for i in strs:
            alphabet_cnts=[0]*26
            for ch in i:
                alphabet_cnts[ord(ch)-ord("a")]+=1
            count[tuple(alphabet_cnts)].append(i)
        return list(count.values())
                
                        

                

