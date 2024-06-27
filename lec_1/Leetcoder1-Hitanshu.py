nums = [2, 4, 8, 9, 12, 13]
target = 6

number_dict = {}  # Dictionary to store numbers and their indices

# Traverse through the array
for i in range(len(nums)):
    complement = target - nums[i]  # Calculate the complement needed

    # Check if the complement is already in the dictionary
    if complement in number_dict:
        print("Indices are:", number_dict[complement], i)  # Print the indices

    number_dict[nums[i]] = i  # Store the current number and its index in the dictionary
