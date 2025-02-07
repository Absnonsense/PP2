def all_permutaions(string):
  if len(string) == 1:
    return string
  permutation = []
  for i in range(len(string)):
    for j in all_permutaions(string[:i] + string[i+1:]):
      permutation.append(string[i] + j)
  return permutation

word = input("Enter a word: ")
print(all_permutaions(word))
