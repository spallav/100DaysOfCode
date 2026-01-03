class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()               # Remove leading/trailing spaces
        last_word = s.split()[-1]   # Split into words and take the last one
        return len(last_word)