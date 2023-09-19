function bigToSmall(arr) {
  //coding here...
  return []
    .concat(...arr)
    .sort((a, b) => b - a)
    .join('>');
}
