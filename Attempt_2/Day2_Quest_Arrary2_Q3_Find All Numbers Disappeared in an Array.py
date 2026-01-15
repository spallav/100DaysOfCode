#Solution - 2
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums = set(nums)
        ans = []
        for i in range(1, n + 1):
            if i not in nums:
                ans.append(i)
        return ans

#time - O(n)
#space - O(n)

#Solution - 2

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums :
            index = abs(num) -1
            if nums[index] > 0 :
                nums[index] = -1 * nums[index]
        
        for i in range(len(nums)) :
            if nums[i] >0 :
                ans.append(i+1)
        return ans


#time - O(n)
#space - O(1)