function topSecret(str) {
  //coding here...
  let chars = str.split('');
  for (let i = 0; i < chars.length; i++) {
    if (chars[i] >= 'a' && chars[i] <= 'z') {
      let code =
        ((chars[i].charCodeAt() - 'a'.charCodeAt() - 3 + 26) % 26) +
        'a'.charCodeAt();
      chars[i] = String.fromCharCode(code);
    } else if (chars[i] >= 'A' && chars[i] <= 'Z') {
      let code =
        ((chars[i].charCodeAt() - 'A'.charCodeAt() - 3 + 26) % 26) +
        'A'.charCodeAt();
      chars[i] = String.fromCharCode(code);
    }
  }
  return chars.join('');
}
//question1: The top secret file number is...
answer1 = '3720';
//question2: Super agent's name is...
answer2 = 'XObm';
//question3: He stole the treasure is...
answer3 = 'Smelly socks';
