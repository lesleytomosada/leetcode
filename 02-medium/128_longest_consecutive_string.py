# Given an unsorted array of integers nums, return the length of the longest
# consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.


# Example 1:

# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4].
# Therefore its length is 4.
# Example 2:

# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9


# Constraints:

# 0 <= nums.length <= 105
# -109 <= nums[i] <= 109

class Solution:
    def longestConsecutive(self, nums) -> int:
        nums.sort()

        if nums:
            consec = [nums[0]]
            longest_consec = 1

        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] == 1:
                if not consec:
                    consec.append(nums[i-1])
                consec.append(nums[i])
                longest_consec = max(longest_consec, len(consec))
            elif nums[i] == nums[i-1]:
                continue
            else:
                consec = []

        return longest_consec if nums else 0
