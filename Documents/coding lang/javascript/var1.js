console.log('varible');
// variable in js
//var ,let,const using keyword we make variable
var c=6; //if we declare variable and not assign any value it called undefined type
console.log(c);
const arr1=[1,2,3,4,5]; // we can push/pop in const keyword array but we cannot re-assgined it.
// arr1=[5,6,7,8];
// arr1.push(6);
// arr1.pop();
console.log(arr1);
//scope of var variable is global scope
//const var2;  at the declaration time we need to assign const variable value otherwise it will be give an error
{
   let c=7;  // let variable scope is block or local scope 
   c=9;
   console.log(c);
}
console.log(c);
/*
 1. camelCase
 2. kebab-case
 3.snake_case
 4.PascalCase
 */