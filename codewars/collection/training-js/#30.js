function tailAndHead(arr) {
  //coding here...
  return arr.reduce((prev, curr, idx, ar) => {
    if (idx == arr.length - 1) {
      return prev;
    }
    let nextVal = ar[idx + 1];
    while (nextVal >= 10) {
      nextVal -= nextVal % 10;
      nextVal /= 10;
    }
    return prev * ((curr % 10) + nextVal);
  }, 1);
}

tailAndHead([1, 2, 3, 4, 5]);
