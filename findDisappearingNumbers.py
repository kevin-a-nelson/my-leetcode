class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        appearedNumbers = {}
        disappearedNumbers = []

        for num in nums:
            appearedNumbers[num] = True

        for i in range(1, len(nums) + 1):
            if not appearedNumbers.get(i):
                disappearedNumbers.append(i)

        return disappearedNumbers
