def spy_game(nums):
  code = [0, 0, 7]
  for num in nums:
      if num == code[0]:
          code.pop(0)
      if not code:  
          return True
  return False

line = input(str("Enter a list of numbers: "))
line = line.split()
num = []
for i in range(len(line)):
  num.append(int(line[i]))
print(spy_game(num))
