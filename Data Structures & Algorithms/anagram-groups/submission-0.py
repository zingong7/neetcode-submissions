class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        used = [False] * len(strs)
        
        for i in range(len(strs)):
            if used[i]:
                continue
            
            cnt_str = {}
            for k in range(len(strs[i])):
                if strs[i][k] in cnt_str:
                    cnt_str[strs[i][k]] += 1
                else:
                    cnt_str[strs[i][k]] = 1
            
            group = [strs[i]]
            used[i] = True
            
            for j in range(i+1, len(strs)):
                if used[j]:
                    continue
                
                temp_store = {}
                for l in range(len(strs[j])):
                    if strs[j][l] in temp_store:
                        temp_store[strs[j][l]] += 1
                    else:
                        temp_store[strs[j][l]] = 1
                
                if temp_store == cnt_str:
                    group.append(strs[j])
                    used[j] = True
            
            output.append(group)
        
        return output
                
                        

                

