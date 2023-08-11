class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]+nums[j] == target:
        #             return [i,j]

        encountered = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in encountered:
                return [encountered[diff],i]
            else:
                encountered[nums[i]] = i