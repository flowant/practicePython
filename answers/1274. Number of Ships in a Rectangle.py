# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Sea:
#    def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
#
# class Point:
#	def __init__(self, x: int, y: int):
#		self.x = x
#		self.y = y

class Solution:
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        """
        1274. Number of Ships in a Rectangle

        Input: ships = [[1,1],[2,2],[3,3],[5,5]], topRight = [4,4], bottomLeft = [1,1]
        Output: 3

        divide the area into 4 parts

        midX = (topRightX - bottomLeftX) // 2 + bottomLeftX  # (4-1) // 2 + 1 = 2
        midY = (topRightY - bottomLeftY) // 2 + bottomLeftY  # (4-1) // 2 + 1 = 2


        if not self.hasShips(topRight, bottomLeft):
            return 0

        if topRight == bottomLeft:
            return 1

        call this function recursively.
        topLeft([bottomLeft.x, midY+1], [midX, topRight.Y])[1,3][2,4]   topRight([midX+1, midY+1],topRight.xy)[3,3][4,4]
        bottomLeft(bottomLeft.xy, [midX, midY])[1,1][2,2]    bottomRight([midX+1,bottomLeft.y][topRight.X, midY])[3,1][4,2]

        return returnOfRecursiveCallWith(ropLeftArea) + returnOfRecursiveCallWith(topRightArea)...

        L1 4^0, 1000 2^10 = 1024
        -
        L2 L2 L2 L2 4^1 500

        L3 L3 L3 L3 L3 L3 L3 L3 L3 L3 L3 L3 L3 L3 L3 L3 4^2 250

        L10

        4 * 9 * 10 , 360 + 1

        Time Complexity = O(log4((topRightX - bottomLeftX) * (topRightY - bottomLeftY) - 1) * S),
        = log4 Volume of the sea(1000000) * the max number of ship (10)
          (log4(1000*1000) - 1) * S

        """
        if not sea or not topRight or not bottomLeft:
            return 0

        def _sum_of_ships(bottomLeftX, bottomLeftY, topRightX,
                          topRightY):  # bottomLeft = [1,1] topRight = [4,4], # [1, 1][2, 2]
            if bottomLeftX > topRightX or bottomLeftY > topRightY:
                return 0
            if not sea.hasShips(Point(topRightX, topRightY), Point(bottomLeftX, bottomLeftY)):
                return 0
            if bottomLeftX == topRightX and bottomLeftY == topRightY:
                return 1

            midX = (
                               topRightX - bottomLeftX) // 2 + bottomLeftX  # (4 - 1) // 2 + 1 = 2 # (2 - 1) // 2 + 1 = 1  # (1-1)//2 + 1 = 1
            midY = (
                               topRightY - bottomLeftY) // 2 + bottomLeftY  # (4 - 1) // 2 + 1 = 2 # (2 - 1) // 2 + 1 = 1  # (1-1)//2 + 1 = 1

            #  [1,3][2,4]   [3,3][4,4]  # [1,2][1,2] [2,2][2,2] # [1,2][1,2] [2,2][1,2]
            #  [1,1][2,2]   [3,1][4,2]  # [1,1][1,1] [2,1][2,1] #
            return (
                    _sum_of_ships(bottomLeftX, midY + 1, midX, topRightY) + _sum_of_ships(midX + 1, midY + 1, topRightX,
                                                                                          topRightY)
                    + _sum_of_ships(bottomLeftX, bottomLeftY, midX, midY) + _sum_of_ships(midX + 1, bottomLeftY,
                                                                                          topRightX, midY)
            )

        return _sum_of_ships(bottomLeft.x, bottomLeft.y, topRight.x, topRight.y)  # topRight = [4,4], bottomLeft = [1,1]
