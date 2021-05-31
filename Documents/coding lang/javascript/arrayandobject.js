console.log('this file for  array and object ');
const marks=[1,2,3,4];
const fruits=['orange','Apple','banana'];
const mixed=[1,2,3,'hii',[66,'h']];
// console.log(mixed);
const arr= new Array(1,2,3,5,4); //construct an array using new
// console.log(arr);
// console.log(arr[0])
console.log(arr.sort()); //for sorting increasing  order
console.log(arr.length); //find length of array
console.log(arr.reverse()); //reverse of array
//push in back of the array
// arr.push(2);
// console.log(arr);
//pop using LIFO 
// arr.pop();
// console.log(arr);
//add element at front of the array
// arr.unshift(2);
// console.log(arr);
//delete from front of the array
// arr.shift();
// console.log(arr);
//console.log(arr.shift()); remove first element from array
// console.log(arr.splice(1,2));
//splice is used for delete element from index1 to total index2 element it will return in answer
// console.log(arr.slice(-2)); 



//object
let info={
    name:'Prince',
    sem:4,
    rollNo:'CE147',
    branch:'CE'
}
console.log(info);
console.table(info); //show in table form
console.log(info['name']); //how to access memebr of object
console.log(info.name);