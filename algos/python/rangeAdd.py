## IDEA

#The result matrix is always going to be in the top-left of the original matrix
#What cells will be increased by 1 for every range?
#All coordinates, where x <= minimum of prev x coordinates and y <= minimum of prev y coordinates.
#That means, we need to continue updating the minimum value of operators[i][1] and operators[i][0] bottom right corner
#The answer would be their multiplication

class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        xmin = m
        ymin = n
        for i in ops:
            if i[0] < xmin:
                xmin = i[0]
            if i[1] < ymin:
                ymin = i[1]
        return xmin*ymin
