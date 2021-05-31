console.log('This file for regular expression');
let reg=/prince/;
let s="hi this is prince. prince is great coder";
// reg=/prince/g;
// reg=/prince/i;
let result= reg.exec(s);
result=reg.test(s);
result=s.match(reg);
result=s.search(reg);
result=s.replace(reg,'PRINCE');
// console.log(result);

// meta charcter
