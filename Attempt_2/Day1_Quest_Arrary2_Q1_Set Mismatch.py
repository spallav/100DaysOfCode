class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        sum_nums = sum(nums)
        set_nums = set(nums)
        set_nums_sum = sum(set_nums)
        expected_sum = n*(n+1)//2
        duplicate_num = sum_nums-set_nums_sum
        missing_num = expected_sum - set_nums_sum

        return [duplicate_num,missing_num]