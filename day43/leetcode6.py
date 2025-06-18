class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
            
        cycle = 2 * numRows - 2
        result = []
        
        for i in range(numRows):
            for j in range(i, len(s), cycle):
                result.append(s[j])
                if i != 0 and i != numRows - 1:
                    k = j + cycle - 2 * i
                    if k < len(s):
                        result.append(s[k])
        
        return ''.join(result)
