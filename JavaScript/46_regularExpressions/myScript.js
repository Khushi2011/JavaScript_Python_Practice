let reg = /khushi/; // This is a regular expression literal in js
//reg = /khushi/g; // g means global
// reg = /khushi/i; // i means case insensitive

console.log(reg);
console.log(reg.source);

let s = "This is great code with khushi and also khushi ";

// Functions to match expressions
// 1. exec() - This function will return an array for match or null for no match
let result = reg.exec(s);
result = reg.exec(s);
console.log(result);
// ---> We can use multiple exec with global flag

// if (result) {
//     console.log(result);
//     console.log(result.input);
//     console.log(result.index);
// }

// 2. test() - Returns true or false
let result2 = reg.test(s);
 console.log(result2); //--> This will only print true if the "reg" is there in the string "s"

// 3. match() - It will return an array of results or null
// let result3 = reg.match(s) ---> This is wrong!!
let result3 = s.match(reg) // ---> This is right
console.log(result3);

// 4. search() - Returns index of first match else -1
// let result4 = reg.search(s) ---> This is wrong!!
let result4 = s.search(reg) // ---> This is right
console.log(result4);

// 5. replace() - Returns new replaced string with all the replacements (if no flag is given, first match will be replaced)

let result5 = s.replace(reg, 'SHALIN');
console.log(result5);

let s1 = "This is great code with Khushi and also khushi";
reg1 = /This/g;
result = reg1.exec(s1);
console.log(result);