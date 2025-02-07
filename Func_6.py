def reverse(string):
  string = string.split(' ')
  rev = []
  for i in range(len(string)):
    rev.append(string[len(string) - i - 1])
  word = ''
  for i in range(len(rev)):
    word += rev[i] + ' '
  return word

phrase = input('Enter a phrase: ')
print(reverse(phrase))
