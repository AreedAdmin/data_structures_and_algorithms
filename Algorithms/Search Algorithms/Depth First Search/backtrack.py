class Solution:
    def subsets(self, nums):
        result = []
        
        # 'i' is the index of the number we are making a decision on
        # 'curr' is the current subset we are building
        def backtrack(i, curr):
            
            # --- BASE CASE (Stop Condition) ---
            # We have made a decision for every number (we went past the last index)
            if i == len(nums):
                result.append(curr[:]) # Important: Make a copy using [:]
                return

            # --- DECISION 1: INCLUDE nums[i] ---
            curr.append(nums[i])       # 1. Add the number
            backtrack(i + 1, curr)     # 2. Move to next number with this item added
            
            # --- THE "BACKTRACK" STEP (Undo) ---
            # We are done with the "Include" branch. 
            # Before we go to the "Exclude" branch, we must clean up!
            curr.pop()                 # 3. Remove the number we just added
            
            # --- DECISION 2: EXCLUDE nums[i] ---
            backtrack(i + 1, curr)     # 4. Move to next number without this item
            
        # Start the recursion at index 0 with an empty list
        backtrack(0, [])
        return result