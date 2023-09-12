function alienLanguage(str) {
  //coding here...
  let words = str.split(' ');
  for (let i = 0; i < words.length; i++) {
    words[i] =
      words[i].slice(0, words[i].length - 1).toUpperCase() +
      words[i].slice(words[i].length - 1).toLowerCase();
  }
  return words.join(' ');
}
