def filter_prime(num):
  prime = []
  for x in num:
    for y in range(2,x):
      if x % y == 0:
        break
    else:
      prime.append(x)
  return prime

arr = input("Enter a list of numbers one by one: ")
arr = arr.split()
nums = []
for x in arr:
  nums.append(int(x))
pri = filter_prime(nums)
print(pri)
