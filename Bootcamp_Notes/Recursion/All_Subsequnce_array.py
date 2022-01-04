class Solution:
    def subsetGenerator(self, idx, nums, sub, powerSet):
        
        if idx>=len(nums):
            powerSet.append(sub[:])
            return
        
        self.subsetGenerator(idx+1, nums, sub, powerSet) #notTake
        
        sub.append(nums[idx])
        self.subsetGenerator(idx+1, nums, sub, powerSet) #take
        sub.pop()
        
    def subsets(self, nums):
        sub = []
        powerSet = []
        self.subsetGenerator(0, nums, sub, powerSet)
        return powerSet