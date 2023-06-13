# 217. Contains Duplicate
# Easy
# 9.5K
# 1.2K
# Companies
# Given an integer array nums, return true if any value appears at least twice
# in the array, and return false if every element is distinct.


# Example 1:

# Input: nums = [1,2,3,1]
# Output: true
# Example 2:

# Input: nums = [1,2,3,4]
# Output: false
# Example 3:

# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true


class Solution:
    def containsDuplicate(self, nums):
        return len(set(nums)) != len(nums)


class Solution2:
    def containsDuplicate(self, nums):
        visited = {}
        for num in nums:
            if num in visited:
                return True
            else:
                visited[num] = 1
        return False
