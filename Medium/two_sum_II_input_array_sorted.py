class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers)-1

        while i<j:
            guess = numbers[i] +numbers[j]

            if guess == target:
                return [i+1,j+1]
            
            elif guess < target:
                i+=1
            
            else:
                j -= 1