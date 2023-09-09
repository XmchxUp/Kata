function whatNumberIsIt(n) {
  //coding here
  strName = '';
  if (Number.isNaN(n)) {
    strName = 'Number.NaN';
  } else if (Number.POSITIVE_INFINITY == n) {
    strName = 'Number.POSITIVE_INFINITY';
  } else if (Number.NEGATIVE_INFINITY == n) {
    strName = 'Number.NEGATIVE_INFINITY';
  } else if (Number.MAX_VALUE == n) {
    strName = 'Number.MAX_VALUE';
  } else if (Number.MIN_VALUE == n) {
    strName = 'Number.MIN_VALUE';
  } else {
    strName = '' + n;
  }
  return `Input number is ${strName}`;
}
