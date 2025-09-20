nums = [25, 12, 36, 95, 14]
print("Original list: ", nums) # Original list
print("Length of list: ", len(nums)) # Length of the list
nums.sort() # Sorts the list in ascending order and modifies the original list
print(nums) # Sorted list
print("Sorted list: ", sorted(nums)) # Sorts the list in ascending order without modifying the original list
print("Original list after sorted: ", nums) # Original list remains unchanged
print("Reversed list: ", list(reversed(nums))) # Reverses the list without modifying the original list
nums.append(16) # Appends 16 to the end of the list
print("List after append: ", nums)
print(nums[0])
print(nums[2:])
print(nums[-1])
print(nums[-3:-1])
nums.insert(0, 45) # Inserts 45 at index 0
print("List after insert: ", nums)
nums.remove(16) # Removes the first occurrence of 16 from the list
print("List after remove: ", nums)
nums.pop() # Removes and returns the last item from the list
print("List after pop: ", nums)
del nums[2:] # Deletes elements from index 2 to the end
print("List after del: ", nums) # List after
nums.extend([55, 66, 77]) # Extends the list by appending elements from the iterable
print("List after extend: ", nums) # List after extend
print(min(nums)) # Returns the smallest item in the list
print(max(nums)) # Returns the largest item in the list
print(sum(nums)) # Returns the sum of all items in the list


nums.clear() # Clears the list
print("List after clear: ", nums) # List is now empty


values = [9.5, "harsh", 25] # List with heterogeneous data
print(values)

mil = [nums, values] # Nested list
print(mil)