function grabDoll(dolls) {
  var bag = [];
  //coding here
  for (let i = 0; i < dolls.length; i++) {
    if (dolls[i] != 'Hello Kitty' && dolls[i] != 'Barbie doll') continue;
    bag.push(dolls[i]);
    if (bag.length == 3) break;
  }
  return bag;
}
