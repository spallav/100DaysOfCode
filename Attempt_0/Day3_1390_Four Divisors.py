class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        total_sum = 0
        for n in nums:
            divisors = []
            i = 1
            while i * i <= n:
                if n % i == 0:
                    divisors.append(i)
                    if i != n // i:
                        divisors.append(n // i)
                if len(divisors) > 4:
                    break
                i = i + 1
            print(divisors)
            if len(divisors) == 4:
                total_sum = total_sum + sum(divisors)
        return total_sum