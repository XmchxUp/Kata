function infiniteLoop(arr, d, n) {
  //coding here...
  let elements = [];
  for (let a of arr) {
    elements.push(...a);
  }
  if (d == 'left') {
    for (let i = 0; i < n; i++) {
      let val = elements.shift();
      elements.push(val);
    }
  } else {
    // "right"
    for (let i = 0; i < n; i++) {
      let val = elements.pop();
      elements.unshift(val);
    }
  }
  let idx = 0;
  for (let a of arr) {
    for (let i = 0; i < a.length; i++) {
      a[i] = elements[idx];
      idx++;
    }
  }
  return arr;
}
