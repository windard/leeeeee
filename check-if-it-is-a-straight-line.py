# coding=utf-8


class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        # divide by zero
        if len(coordinates) < 3:
            return True

        if not coordinates[1][0] - coordinates[0][0]:
            for coordinate in coordinates[2:]:
                if coordinate[0] - coordinates[0][0]:
                    return False
            return True

        if not coordinates[1][1] - coordinates[0][1]:
            for coordinate in coordinates[2:]:
                if coordinate[1]-coordinates[0][1]:
                    return False
                return True

        for coordinate in coordinates[2:]:
            # if (coordinate[0] - coordinates[0][0]) / coordinates[1][0]-coordinates[0][0] != \
            #         coordinate[1] - coordinates[0][1] / coordinates[1][1]-coordinates[0][1]:
            #     return False
            if not coordinate[1]-coordinates[0][1]:
                return False
            if (coordinate[0]-coordinates[0][0]) / (coordinate[1]-coordinates[0][1]) != \
                    (coordinates[1][0]-coordinates[0][0]) / (coordinates[1][1]-coordinates[0][1]):
                return False
        return True
