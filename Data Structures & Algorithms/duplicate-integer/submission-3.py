class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        flag = False
        map ={}
        for i in nums:
            if i not in map:
                map[i] = 1
                # map[i] += 1
                # i +=1
                # print(i)
            else:
                flag = True
                map[i] += 1
        return flag        