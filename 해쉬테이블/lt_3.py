# 3. Longest Substring Without Repeating Characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        output = 0
        
        strings = []
        s_lst = list(s)
        s_set = set(s_lst)
        
        # 들어온 입력 값이 set(unique)값이 0,1 이면 굳이 다 살펴볼 필요 없다.
        if len(s_set) == 0:
            output = 0
        elif len(s_set) == 1:
            output = 1
        
        # 인자값 살피며 유니크 가장 긴 문자열 찾아보장~
        else:
            for i in range(len(s_lst)):
                sub = []
                for j in range(i, len(s_lst)):
                    # 해당 위치 문자열이 이미 저장된 값에 있다면 더이상 추가하지 않고 기존까지 저장된 값이 Max
                    if s[j] in sub:
                        # 지금까지 더해진값 붙이기  
                        string = ''.join(sub)
                        # 그 길이 반환
                        strings.append(len(string))
                        break

                    # 해당 위치 문자열이 지금까지 저장된 값에 없다면 추가
                    else:
                        sub.append(s[j])
                    
                    # 맨 마지막 문자에서 체크 시
                    if j == len(s) - 1: 
                        sub = ''.join(sub)
                        strings.append(len(sub))
            output = max(strings)
            
        return output