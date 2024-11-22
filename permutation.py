class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        # Step 1: Finding the smallest index from left to right
        index = -1
        for i in range(len(nums) - 1, 0, -1):
            if nums[i - 1] < nums[i]:
                index = i - 1  
                break

        # Step 2: If no such index is found, the array is in descending order,reverse the entire array
        if index == -1:
            nums.reverse()
            return

        # Step 3: Finding the smallest element larger than nums[index] from the right to left 
        minIndex = 0
        for i in range(len(nums) - 1, index, -1):
            if nums[i] > nums[index]:
                minIndex = i  
                break

        # Step 4: Swapping the  index and minIndex
        nums[index], nums[minIndex] = nums[minIndex], nums[index]

        # Step 5: Reverse the subarray nums[index + 1:] to get the smallest lexicographical order
        nums[index + 1:] = reversed(nums[index + 1:])
