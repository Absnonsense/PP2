def unique(list1):
  unique_list = []
  for x in list1:
    if x not in unique_list:
      unique_list.append(x)
  return unique_list

line = input("Enter elements: ")
line = line.split(" ")
print(unique(line))
