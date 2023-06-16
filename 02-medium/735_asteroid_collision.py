# We are given an array asteroids of integers representing asteroids in a row.

# For each asteroid, the absolute value represents its size, and the sign
# represents its direction (positive meaning right, negative meaning left).
# Each asteroid moves at the same speed.

# Find out the state of the asteroids after all collisions. If two asteroids
# meet, the smaller one will explode. If both are the same size, both will
# explode. Two asteroids moving in the same direction will never meet.


# Example 1:

# Input: asteroids = [5,10,-5]
# Output: [5,10]
# Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never
# collide.
# Example 2:

# Input: asteroids = [8,-8]
# Output: []
# Explanation: The 8 and -8 collide exploding each other.
# Example 3:

# Input: asteroids = [10,2,-5]
# Output: [10]
# Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide
# resulting in 10.


class Solution:
    def asteroidCollision(self, asteroids):
        stack = [asteroids[0]]
        i = 1
        while i < len(asteroids):
            try:
                if abs(asteroids[i]) > abs(stack[-1]) and (asteroids[i] < 0 and stack[-1] > 0):  # noqa
                    stack.pop()
                elif abs(asteroids[i]) < abs(stack[-1]) and (asteroids[i] < 0 and stack[-1] > 0): # noqa
                    i += 1
                elif abs(asteroids[i]) == abs(stack[-1]) and (asteroids[i] < 0 and stack[-1] > 0): # noqa
                    stack.pop()
                    i += 1
                else:
                    stack.append(asteroids[i])
                    i += 1
            except IndexError:
                stack.append(asteroids[i])
                i += 1
        return stack


class Solution2(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []
        for num in asteroids:
            if num > 0:
                stack.append(num)
            else:
                while stack and stack[-1] > 0 and stack[-1] < abs(num):
                    stack.pop()
                if not stack or stack[-1] < 0:
                    stack.append(num)
                elif stack[-1] == -num:
                    stack.pop()
        return stack
