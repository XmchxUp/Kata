function threeInOne(arr) {
  //coding here...
  let tmpArr = arr.slice();
  let res = [];
  for (let i = 0; i < arr.length / 3; i++) {
    let cur = 0;
    for (let j = 0; j < 3; j++) cur += tmpArr[j];
    tmpArr.splice(0, 3);
    res.push(cur);
  }
  return res;
}
