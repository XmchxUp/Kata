const FIRST_SECOND_CHARS = 'ABCDEFGHIJKLM';
const SYMBOLS = '~!@#$%^&*';

function rndCode() {
  //coding here...
  let res = '';
  for (let i = 0; i < 2; i++) {
    res += FIRST_SECOND_CHARS[~~(Math.random() * FIRST_SECOND_CHARS.length)];
  }
  for (let i = 0; i < 4; i++) {
    res += ~~(Math.random() * 10);
  }
  for (let i = 0; i < 2; i++) {
    res += SYMBOLS[~~(Math.random() * SYMBOLS.length)];
  }
  return res;
}
