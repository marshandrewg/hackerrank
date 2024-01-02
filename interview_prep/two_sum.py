Ok, 

1 3 5 4 2 7
sort them and remove any greater than sum (n) 7
1 2 3 4 5 7

now we have to find the pairs that sum to n

1 7 L move right index to left
1 5 H move left index to right
2 5 dead on


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i,v in enumerate(nums):
            for i2,v2 in enumerate(nums[i+1:]):
                if(v+v2 == target):
                    return [i,i2+1+i]



class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsSorted = sorted(nums)
        leftIndex = 0
        rightIndex = len(nums) - 1
        solutionFound = False
        while(solutionFound != True):
            leftVal = numsSorted[leftIndex]
            rightVal = numsSorted[rightIndex]
            sum = leftVal + rightVal
            print(f"solution {leftIndex} {rightIndex} {leftVal} {rightVal}")
            if sum > target:
                rightIndex -= 1
            elif sum < target:
                leftIndex += 1
            else:
                if(leftVal == rightVal):
                    leftIndex = nums.index(leftVal)
                    rightIndex = nums[leftIndex+1:].index(leftVal)+leftIndex+1
                    return [leftIndex, rightIndex]
                return [nums.index(leftVal),nums.index(rightVal)]

# 3 2 3
# 3 3
# leftIndex = 0
#
        
# Downsides
            # Memory usage is high
            # Could solve by using a generator / iterator on original list rather than copying to new list


