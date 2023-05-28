# Given a string s, reverse only all the vowels in the string and return it.

# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both
# lower and upper cases, more than once.


# Example 1:

# Input: s = "hello"
# Output: "holle"
# Example 2:

# Input: s = "leetcode"
# Output: "leotcede"

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
        s_list = list(s)
        left = 0
        r = len(s) - 1
        while left <= r:
            if s_list[left] in vowels and s_list[r] in vowels:
                s_list[left], s_list[r] = s_list[r], s_list[left]
                left += 1
                r -= 1
            elif s_list[left] in vowels:
                r -= 1
            elif s_list[r] in vowels:
                left += 1
            else:
                left += 1
                r -= 1
        return "".join(s_list)
