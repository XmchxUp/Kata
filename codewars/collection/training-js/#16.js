function cutIt(arr) {
  //coding here...
  let minLength = Math.min(...arr.map((str) => str.length));
  return arr.map((str) => str.slice(0, minLength));
}
