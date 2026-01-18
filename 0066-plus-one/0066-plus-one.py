class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        carry = 0

        if digits == [9]: return [1, 0]

        if digits[-1] + 1 <= 9: 
            digits[-1] += 1
            # print("One")
            return digits
        else: 
            carry = 1
            digits[-1] = 0
            for i in range(len(digits) - 2, 0, -1):
                if digits[i] + 1 > 9:
                    digits[i] = 0
                    carry = 1
                else:
                    digits[i] += carry
                    carry = 0
                if carry == 0: 
                    # print("Two")
                    return digits

            if carry == 1:
                if digits[0] + 1 > 9:
                    digits[0] = 0
                    # print("Three")
                    return [1] + digits
                else:
                    digits[0] += 1
                    # print("Four")
                    return digits
            # print("Five")
            return digits