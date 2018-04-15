class Solution(object):
        def twoSum(self, nums, target):
            """
            :type nums: List[int]
            :type target: int
            :rtype: List[int]
            """
            complements = {}
            for i in range(len(nums)):
                diff = target - nums[i]
                if diff in complements:
                    return [complements[ diff ], i]
                else:
                    complements[ nums[i] ] = i
            return []

print(Solution().twoSum([2, 7, 11, 15], 9))
