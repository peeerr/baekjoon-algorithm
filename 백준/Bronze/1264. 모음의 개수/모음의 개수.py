words = []
vowel = ['a', 'e', 'i', 'o', 'u']

while True:
  word = input().lower()
  if word == '#':
    break
  words.append(word)

for word in words:
  cnt = 0
  for w in word:
    if w in vowel:
      cnt += 1
  print(cnt)