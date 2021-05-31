console.log('var2 file');
// string
let name="prince";
console.log("Data type is "+ typeof name);
//number
let mark=34;
console.log("Data type is "+ typeof mark);
//boolean
let isStudent = true;
console.log("Data type is "+ typeof isStudent);
//null
let val= null;
console.log("Data type is "+ typeof val);
//undefined
let val1; // means val1=undefined;
console.log("Data type is "+ typeof val1);

//Reference datatype
// number,boolean,array,date -->string
//string,boolean --> number ,if string is valid number otherwise it will give NaN
//toFixed(n) n digit after decimal it will print
//parseInt parseFloat...
//arrays
let myarr=[1,2,3,4,true,"string"]; // array can contain different type of element
console.log("Data type is "+ typeof myarr);
//object litreals
let stMarks={
    prince :39,
    yash: 38,
    keyur:35
}
console.log("Data type is "+ typeof stMarks);
//function
function name1(params) {
    
}
console.log("Data type is "+ typeof name1);
//date
let date= new Date();
// console.log(date);
console.log("Data type is "+ typeof date);
