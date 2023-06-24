// Recover toString() here :)

Boolean.prototype.toString = function () {
  return this.valueOf() ? "true" : "false";
}
Number.prototype.toString = function () {
  return String(this.valueOf());
}
Array.prototype.toString = function () {
  return "[" + this.join(",") + "]"
}

console.log([2, 4, 8, 17].toString())
