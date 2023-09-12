function splitAndMerge(string, separator) {
  let words = string.split(' ');
  words = words.map((w) => w.split('').join(separator));
  return words.join(' ');
}
