function firstToLast(str, c) {
  //coding here..
  let firstP = str.indexOf(c);
  let lastP = str.lastIndexOf(c);
  if (firstP == -1 && lastP == -1) {
    return -1;
  } else if (firstP == -1 || lastP == -1) {
    return 0;
  } else {
    return lastP - firstP;
  }
}
