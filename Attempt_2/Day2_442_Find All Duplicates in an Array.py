class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            index = abs(num) - 1
            if nums[index] > 0:
                nums[index] = -1 * nums[index]
            else:
                ans.append(index+1)
        return ans
# time - O(n)
# space - O(1)