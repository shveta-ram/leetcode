#Solution 1: Swapping

x = 0  # iterator one
for y in range(len(nums)):  # iterator two moves through full array
    if nums[y] != 0:  # nonzero integers are swapped with zeroes
        nums[x], nums[y] = nums[y], nums[x]
        x += 1  # only moves to the next index if the element is not 0
#  this method allows the zeroes to be together as they move through the array to the end

#Solution 2: Built-In Functions

for x in range(len(nums)-1, -1, -1):
	if nums[x] == 0:
	    nums.append(nums.pop(x)) # pop can only be used through reverse iteration