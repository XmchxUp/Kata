def get_count(sentence):
  vowels = set(["a","e","i","o","u"])
  cnt = 0
  for c in sentence:
    if c in vowels:
      cnt += 1
  return cnt