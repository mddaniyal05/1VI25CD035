class Solution:
    def lengthOfLongestSubstring(self, s):
        max_len = 0

        for i in range(len(s)):
            temp = ""

            for j in range(i, len(s)):
                ch = s[j]

                if ch not in temp:
                    temp += ch
                else:
                    break

            if len(temp) > max_len:
                max_len = len(temp)

        return max_len