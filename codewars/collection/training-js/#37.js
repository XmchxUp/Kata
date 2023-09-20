function countAnimals(animals, count) {
  //coding here...
  let res = [];
  for (let name of count) {
    res.push((animals.match(new RegExp(name, 'g')) || []).length);
  }
  return res;
}
