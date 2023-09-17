function sortIt(arr) {
  //coding here...

  let m = {};
  for (let a of arr) {
    if (a in m) {
      continue;
    }
    m[a] = arr.reduce((p, c) => {
      return c == a ? p + 1 : p;
    }, 0);
  }
  let res = arr.slice();
  res.sort((a, b) => {
    if (m[a] == m[b]) {
      return 0;
    }
    return m[a] - m[b];
  });
  return res;
}

console.log(sortIt([1, 1, 1, 2, 2, 3]));
