# 605. Can Place Flowers
# Easy
# 5K
# 843
# Companies
# You have a long flowerbed in which some of the plots are planted, and some
# are not. However, flowers cannot be planted in adjacent plots.

# Given an integer array flowerbed containing 0's and 1's, where 0 means empty
#  and 1 means not empty, and an integer n, return true if n new flowers can
#  be planted in the flowerbed without violating the no-adjacent-flowers rule
#  and false otherwise.

# Example 1:

# Input: flowerbed = [1,0,0,0,1], n = 1
# Output: true
# Example 2:

# Input: flowerbed = [1,0,0,0,1], n = 2
# Output: false


# Constraints:

# 1 <= flowerbed.length <= 2 * 104
# flowerbed[i] is 0 or 1.
# There are no two adjacent flowers in flowerbed.
# 0 <= n <= flowerbed.length

class Solution:
    def canPlaceFlowers(self, flowerbed, n) -> bool:
        if n == 0:
            return True
        if len(flowerbed) < 2:
            if 1 in flowerbed:
                return False
            if n < 2:
                return True
            elif n >= 2:
                return False
        placable_flowers = 0
        if flowerbed[0] == flowerbed[1] == 0:
            placable_flowers += 1
            flowerbed[0] = 1
        for i in range(1, len(flowerbed)-1):
            if flowerbed[i] == flowerbed[i-1] == flowerbed[i+1] == 0:
                placable_flowers += 1
                flowerbed[i] = 1
        if flowerbed[-1] == flowerbed[-2] == 0:
            placable_flowers += 1
            flowerbed[-1] = 1

        return placable_flowers >= n
