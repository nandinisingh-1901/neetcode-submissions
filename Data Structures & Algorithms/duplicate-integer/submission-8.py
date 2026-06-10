class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map = {}
        flag = False
        for n in nums:
            if n not in map:
                map[n] = 1
            else:
                return True
        return flag