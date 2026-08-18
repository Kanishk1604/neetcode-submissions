class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        top = 0
        bott = m - 1

        while top < bott:
            if target > matrix[top][n -1]:
                top += 1
            if target < matrix[bott][0]:
                bott -= 1
        
        if top > bott: return False

        row = matrix[top]

        l , r = 0, n -1

        while l <= r:
            mid = (l + r) // 2
            if row[mid] == target:
                return True
            elif row[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return False
            
