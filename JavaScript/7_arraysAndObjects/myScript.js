const arr1=[75,88,91,20,47];
const arr2=['khushi','manish','rita','shalin'];
const arr3=['str',78,90,[56,79]];//length will be 4
const arr4=new Array(24,7,34,13);
console.log(arr1);      
console.log(arr2); 
console.log(arr3); 
console.log(arr4);  

//array properties
console.log(arr1.length);
console.log(Array.isArray(arr1));//returns true or false
console.log(Array.isArray('khushi'));

arr1[0]= 99;
console.log(arr1); 

let value1=arr2.indexOf('manish');
let value2=arr2.indexOf('khushi234');
console.log(value1); 
console.log(value2); //if don't found any value in array than return -1.

//mutating array ..........It will originally change the array.
const arr=[89,98,78,92,83];
arr.push(72);//push ad the end
arr.unshift(72);//push at front end
arr.pop();//pop from the end
arr.shift();//pop at front
arr.splice(1,2);//it will remove 2 elements from index 1 .........ex:-arr.splice(3,8)-it will remove 8 elements starting from index 3....if it don't have index 3 then it will do nothing.
arr.reverse();//reverse the array
console.log(arr);

//to concat two arrays
const arr5=[99,90,98,97];
arr6=arr.concat(arr5);
console.log(arr6);
arr6=arr5.concat(arr);
console.log(arr6);//for concat two array's let,const type should be same.

let myObj={
        'first name':'khushi',//to add space 
        department:'CE',//department is key and CE is value of it
        isPass:true,
        marks:[31,26,28,32,33],
}

console.log(myObj);//to print whole object
console.log(myObj.department);
console.log(myObj['first name']);//for space in key of object...
console.log(myObj.marks);