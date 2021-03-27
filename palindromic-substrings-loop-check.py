'''
    https://leetcode.com/problems/palindromic-substrings/
'''

class Solution:
    def countSubstrings(self, s: str) -> int:
        count_palindrom = len_s = len(s)
        for i in range(len_s):
            left_i = i - 1
            right_i = i + 1
            while left_i >= 0 and right_i < len_s and s[left_i] == s[right_i]:
                count_palindrom += 1
                left_i -= 1
                right_i += 1
            if i+1 < len_s:
                if s[i] == s[i+1]:
                    count_palindrom += 1
                    left_i = i-1
                    right_i = i+2
                    while left_i >= 0 and right_i < len_s and s[left_i] == s[right_i]:
                        count_palindrom += 1
                        left_i -= 1
                        right_i += 1
        return count_palindrom
            