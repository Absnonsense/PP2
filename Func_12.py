def histograms(nums):
  for i in range(len(nums)):
    print(nums[i] * "*")

line = input('Enter a list of numbers: ')
line = line.split()
nums = []
for i in range(len(line)):
  nums.append(int(line[i]))
histograms(nums)
