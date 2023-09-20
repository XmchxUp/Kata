function roundIt(n) {
  // coding here...
  tmps = String(n).split('.');
  if (tmps[0].length < tmps[1].length) {
    return Math.ceil(n);
  } else if (tmps[0].length > tmps[1].length) {
    return Math.floor(n);
  } else {
    return Math.round(n);
  }
}
