class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        
        hashMap = {}

        for num in nums:
            if hashMap.get(num) == None:
                hashMap[num] = 1
            else: return num