class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m=len(matrix)
        n=len(matrix[0])

        low=0
        high=(n*m)-1

        while low<=high:
            mid=(low+high)//2
            if matrix[mid//n][mid%n]==target:
                return True
            elif matrix[mid//n][mid%n]<target:
                low=mid+1
            else:
                high=mid-1
        return False
        