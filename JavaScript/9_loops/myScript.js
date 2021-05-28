//for loop
console.log('for LOOP');
for (let i = 0; i < 10; i++) {
	console.log(i);
}

//while loop
console.log('while LOOP');
let j = 5;
while (j < 10) {
	console.log(j);
	j++;
}

//do while is same as another language

//for each loop
console.log('forEACH LOOP');
const arr = [1, 5, 10, 15, 20];
arr.forEach(function (ele) {
	console.log(ele);
});
arr.forEach(function (element, index, array) {
	console.log(element, index, array);
});

//without for each loop
const alpha = ['a', 'b', 'c'];
for (let i = 0; i < alpha.length; i++) {
	console.log(alpha[i]);
}

//for object
console.log('object printing');
let obj = {
	name: 'khushi doshi',
	age: 19,
	type: 'Programmer',
	os: 'windows 10',
};
for (let key in obj) {
	console.log(`The ${key} of object is ${obj[key]}`);
}
