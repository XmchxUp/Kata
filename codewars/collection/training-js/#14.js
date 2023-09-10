function colorOf(r, g, b) {
  let formatToHex = (num) => {
    const hex = num.toString(16);
    return hex.length == 1 ? '0' + hex : hex;
  };
  //coding here
  return `#${formatToHex(r)}${formatToHex(g)}${formatToHex(b)}`;
}
