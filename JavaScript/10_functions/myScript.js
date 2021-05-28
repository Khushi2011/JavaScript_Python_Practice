/* function name(parameters){
   statements
/}*/
print_message('Hello World');
function print_message(message) {
	console.log(message);
}
print_message('Hello World'); //we can do both first call than define or first define than call

//function name in different way
let add = function (a, b) {
	return a + b;
};
console.log(add(4, 3));

// function print_message(message) {
//     console.log(message);
// }
// let result = say('Hello khushi');//say is undefined...referenceRrror
// console.log('Result:', result);

function get_Distance(speed, time) {
	let dist = speed * time;
	return dist;
}
const myDistance = get_Distance(8, 5);
console.log(myDistance);

//default parameters
const mygreet = function (name, thank = 'Thank You') {
	let msg = `Happy Birthday ${name} How I wish I could fly to you right now and be with you on this special day of yours. But remember, my good wishes are always there with you. ${thank}!`;
	return msg;
};

let name = 'khushi';
let name2 = 'shalin';

let val = mygreet(name, 'Thanks a lot');
console.log(val);

//function in object
const myobj = {
	name: 'SkillF',
	hobby: function () {
		return 'Programming';
	},
};
console.log(myobj.hobby());

//printing array
arr = ['fruit', 'vegetable', 'furniture'];
arr.forEach(function (element, index, array) {
	console.log(element, index);
});

//let or const have block level scope,while var has function level scope