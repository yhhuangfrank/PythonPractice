class Solution:
    def addMinimum(self, word: str) -> int:
        # return self.solution1(word)
        return self.solution2(word)

    # O(N) time
    def solution1(self, word: str) -> int:
        valid = 'abc'
        l = 0 # pointer for word
        r = 0 # pointer for 'abc'
        count = 0
        while l < len(word):
            while word[l] != valid[r]:
                r += 1
                if r == len(valid):
                    r = 0
                count += 1
            l += 1
            r += 1
            if r == len(valid):
                r = 0
        # 最後不是指到 'a'，代表需要補齊
        if r != 0:
            count += len(valid) - r
        return count

    # O(N) time, 從數學上角度，先計算需要幾組 abc，再計算出需要補的數量
    def solution2(self, word: str) -> int:
        pairs = 1
        for prev, cur in zip(word, word[1:]):
            if cur <= prev:
                pairs += 1
        return 3 * pairs - len(word)

# Example 1:
# Input: word = "b"
# Output: 2
# Explanation: Insert the letter "a" right before "b", and the letter "c" right next to "b" to obtain the valid string "abc".
#
# Example 2:
# Input: word = "aaa"
# Output: 6
# Explanation: Insert letters "b" and "c" next to each "a" to obtain the valid string "abcabcabc".
#
# Example 3:
# Input: word = "abc"
# Output: 0
# Explanation: word is already valid. No modifications are needed.

sol = Solution()
print(sol.addMinimum('a')) # 2
print(sol.addMinimum('aaa')) # 6
print(sol.addMinimum('abc')) # 0
print(sol.addMinimum('aaaaca')) # 9