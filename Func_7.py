def has33(nums):
  for i in range(len(nums)-1):
    if nums[i] == 3 and nums[i+1] == 3:
      return True
  return False

line = input("Enter a list of numbers separated by spaces: ")
line = line.split(" ")
nums = []
for i in line:
  nums.append(int(i))
print(has33(nums))
