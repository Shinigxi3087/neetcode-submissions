class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {} # val : index
        for i, j in enumerate(nums):
            diff = target - j
            if diff in map:
                return [map[diff], i]
            map[j] = i
        return