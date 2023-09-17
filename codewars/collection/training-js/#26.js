function isolateIt(arr) {
  //coding here...
  let tmp = arr.slice();
  return tmp.map((ele) => {
    if (ele.length % 2 == 0) {
      return ele.slice(0, ele.length / 2) + '|' + ele.slice(ele.length / 2);
    } else {
      return ele.slice(0, ele.length / 2) + '|' + ele.slice(ele.length / 2 + 1);
    }
  });
}
