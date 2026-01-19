class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        
        sum = 0

        for num in nums:
            divisorsCount = 2
            divisorsSum = 1 + num
            for i in range(2, floor(sqrt(num)) + 1, 1):
                if num % i == 0:
                    if i * i == num: 
                        divisorsCount += 1
                        divisorsSum += i
                    else:
                        divisorsCount += 2
                        divisorsSum += i + num // i
                    if divisorsCount > 4: break
                
            if divisorsCount == 4: 
                sum += divisorsSum

        return sum