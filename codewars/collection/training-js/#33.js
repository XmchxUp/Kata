function maxMin(arr1, arr2) {
  //coding here...
  let res = [];
  for (let i = 0; i < arr1.length; i++) {
    res.push(Math.abs(arr1[i] - arr2[i]));
  }
  return [Math.max(...res), Math.min(...res)];
}
