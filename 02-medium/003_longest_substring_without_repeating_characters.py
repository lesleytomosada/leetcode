# Given a string s, find the length of the longest substring without
# repeating characters.

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not
# a substring.


# Constraints:

# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        i = 0
        j = 1

        letters = set(s[i])
        substring = s[i]
        longest_len = 1

        while i < len(s) - 1 and j < len(s):
            if not substring:
                substring = s[i]
                letters.add(s[i])
            if s[j] not in letters:
                letters.add(s[j])
                substring += s[j]
                j += 1
            else:
                if len(substring) > longest_len:
                    longest_len = len(substring)
                else:
                    substring = ""
                    letters = set()
                    i += 1
                    j = i + 1

        if len(substring) > longest_len:
            return len(substring)
        else:
            return longest_len


class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        left = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[left])
                left += 1
            charSet.add(s[r])
            res = max(res, r - left + 1)
        return res
