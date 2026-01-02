class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        count = Counter(nums)
        for i in count:
            if count[i] == len(nums)/2 :
                return i
        return -1