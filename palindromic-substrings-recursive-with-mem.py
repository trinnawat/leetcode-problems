'''
    https://leetcode.com/problems/palindromic-substrings/
'''

class Solution:
    def countSubstrings(self, s: str) -> int:
        mem = {}
        def is_palindromic(sub_s):
            if sub_s in mem:
                return mem[sub_s]
            if len(sub_s) == 1:
                mem[sub_s] = True
            elif len(sub_s) == 2:
                mem[sub_s] = (sub_s[0] == sub_s[1])
            else:
                mem[sub_s] = (is_palindromic(sub_s[1:-1])) and (sub_s[0] == sub_s[-1])
            return mem[sub_s]
        count_palindrom = 0
        len_s = len(s)
        for i in range(len_s):
            for j in range(i+1, len_s+1):
                if is_palindromic(s[i:j]):
                    count_palindrom += 1
        return count_palindrom