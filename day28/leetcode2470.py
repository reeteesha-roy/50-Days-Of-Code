import math
class Solution:
  def subarrayLCM(self, nums: list[int], k: int) -> int:
    def lcm(a, b):
            return abs(a * b) // math.gcd(a, b)

        count = 0
        n = len(nums)

        for i in range(n):
            curr_lcm = nums[i]
            if k % nums[i] != 0:
                continue  # can't be part of a subarray forming k

            for j in range(i, n):
                curr_lcm = lcm(curr_lcm, nums[j])

                if curr_lcm == k:
                    count += 1
                elif curr_lcm > k:
                    break  # no point in continuing

        return count
