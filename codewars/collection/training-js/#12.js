function giveMeFive(obj) {
  //coding here
  let res = [];
  for (let k in obj) {
    if (k.length == 5) {
      res.push(k);
    }
    if (obj[k].length == 5) {
      res.push(obj[k]);
    }
  }
  return res;
}
