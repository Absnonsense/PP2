def solve(numhead, numlegs):
  return (4*numhead - numlegs)/2, numhead - (4*numhead - numlegs)/2

numhead = int(input("Enter the number of heads: "))
numlegs = int(input("Enter the number of legs: "))
numchicken, numrabbit = solve(numhead, numlegs)
print("Number of chickens: ", numchicken)
print("Number of rabbits: ", numrabbit)
