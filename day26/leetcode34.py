from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findLeft(nums: List[int], target: int) -> int:
            left, right = 0, len(nums) - 1
            index = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    if nums[mid] == target:
                        index = mid
                    right = mid - 1
            return index

        def findRight(nums: List[int], target: int) -> int:
            left, right = 0, len(nums) - 1
            index = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] > target:
                    right = mid - 1
                else:
                    if nums[mid] == target:
                        index = mid
                    left = mid + 1
            return index

        return [findLeft(nums, target), findRight(nums, target)]
