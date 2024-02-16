function isValidSubsequence(array, sequence) {
  // Write your code here.
  let idx = 0;
  for (let i = 0; i < array.length; i++) {
    if (array[i] == sequence[idx]) {
      idx += 1;
    }
  }
  return idx == sequence.length;
}
