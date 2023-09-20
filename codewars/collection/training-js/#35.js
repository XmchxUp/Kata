function thinkingAndTesting(number, base) {
  return number - base ** Math.floor(Math.log(number) / Math.log(base));
}

// ex
// 100 - 2 ** something = 36
// 2 ** something = 64
// something = 6  ...6.64

// ex
// 1000 - 2 ** something = 488
// 2 ** something = 512
// something = 9  ...9.965

// ex
// 1111 - 10 ** something = 111
// 10 ** something = 1000
// something = 3  ...3.04

// ex
// 2 - 2 ** something = 0
// 2 ** something = 2
// something = 1
