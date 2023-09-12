function fiveLine(s) {
  //coding here...
  s = s.trim();
  let chars = [];
  for (let i = 0; i < 5; i++) {
    let curStr = '';
    for (let j = 0; j <= i; j++) {
      curStr += s;
    }
    if (i == 4) {
      chars.push(curStr);
    } else {
      chars.push(curStr + '\n');
    }
  }
  return chars.join('');
}
