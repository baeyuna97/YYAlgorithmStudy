# 771. Jewels and Stones

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        jew = []
        output = 0
        
        for j in J:
            jew.append(j)
            
        for s in S:
            if s in jew:
                output += 1
                
        return output