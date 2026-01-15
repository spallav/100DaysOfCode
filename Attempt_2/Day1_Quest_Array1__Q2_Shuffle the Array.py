class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = [0] * len(nums)
        x = nums[:n]
        y = nums[n:2*n]
        for i in range(n):
            ans[2 * i], ans[2*i+1] = x[i],y[i]
        return ans