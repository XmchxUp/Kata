function shuffleIt(arr, ...swapPoints) {
  //coding here...
  for (let [p1, p2] of swapPoints) {
    [arr[p1], arr[p2]] = [arr[p2], arr[p1]];
  }
  return arr;
}
