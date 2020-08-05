# 3. Longest Substring Without Repeating Characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        output = 0
        
        strings = []
        s_lst = list(s)
        s_set = set(s_lst)
        
        if len(s_set) == 0:
            output = 0
        elif len(s_set) == 1:
            output = 1
        else:
            for i in range(len(s_lst)):
                sub = []
                for j in range(i, len(s_lst)):
                    if s[j] in sub:
                        # 마무리 
                        string = ''.join(sub)
                        strings.append(len(string))
                        break
                    else:
                        sub.append(s[j])
                    
                    # 맨 마지막 문자에서 체크 시
                    if j == len(s) - 1:
                        sub = ''.join(sub)
                        strings.append(len(sub))
            output = max(strings)
            
        return output