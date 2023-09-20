function findSimilarity(str, word) {
  //coding here...
  let regx = new RegExp(
    `^${word[0]}${word.slice(1, -1).replace(/./g, '.')}${word.slice(-1)}$`,
  );
  return str
    .split(/ /)
    .filter((w) => regx.test(w))
    .join(' ');
}
