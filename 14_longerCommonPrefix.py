def longestCommonPrefix(strs):
        pm=''
        if not strs:
            return pm
            
        for i in range(len(strs[0])):
            char=strs[0][i]
            for j in range(1,len(strs)):
                if i==len(strs[j]) or strs[j][i] != char:
                    return pm
                
            pm+=char
        return pm