class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        rows = len(word1)+1
        cols = len(word2)+1
        result = [[0]*cols  for _ in range(rows)]
        
        rowIdx = 1
        colIdx = 1
        
        while colIdx < cols:
            result[0][colIdx] = colIdx
            colIdx += 1
            
        while rowIdx < rows:
            result[rowIdx][0] = rowIdx
            rowIdx += 1
        
        rowIdx = 1
        colIdx = 1
        
        while rowIdx < rows:
            colIdx = 1
            while colIdx < cols:
                if word1[rowIdx-1] == word2[colIdx-1]:
                    result[rowIdx][colIdx] = result[rowIdx-1][colIdx-1]
                else:
                    result[rowIdx][colIdx] = min(result[rowIdx-1][colIdx],result[rowIdx-1][colIdx-1],result[rowIdx][colIdx-1])+1
                colIdx += 1
            rowIdx += 1
    
        return result[rows-1][cols-1]