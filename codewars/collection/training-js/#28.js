function mirrorImage(arr) {
  //coding here...
  let a = -1;
  let b = -1;
  let isMirror = (x, y) => {
    return x == y || x.toString().split('').reverse().join('') == y.toString();
  };
  arr.some((x, i) => {
    if (i == arr.length - 1) return false;
    a = arr[i];
    b = arr[i + 1];
    return isMirror(a, b);
  });
  return isMirror(a, b) ? [a, b] : [-1, -1];
}
