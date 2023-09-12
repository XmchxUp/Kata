function howManySmaller(arr, n) {
  //coding here..
  let cnt = 0;
  for (let i = 0; i < arr.length; i++) {
    arr[i] = arr[i].toFixed(2);
    if (arr[i] < n) {
      cnt++;
    }
  }
  return cnt;
}
