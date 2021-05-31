console.log('this is for dom selectors');
/*
1. single element selectors
2. multi element selectors
*/
//single element selectors
let a=document.getElementById('myfirst');  //show an element of document  by id 
// a=a.className; // give class name of that element
// a=a.childNodes; // give child nodes of  selected element 
// a=a.parentNode; //give parent node of selected element
// a=a.parentElement;
//we can chage property of html selected element
a.style.color='red' //change color of selected element
a.innerText='Prince'; //change text of selected element
a.innerHTML='<b>Prince</b>' // change html of selected element
// console.log(a);

//in query selecotr in argument we pass id ,classname
//id using # pass
// #classname using . pass
let sel=document.querySelector('#myfirst'); //give element by id
sel=document.querySelector('.red'); //give first div which class name is red
sel=document.querySelector('div'); //give first div we can pass tag in argument of query selectors
sel.style.color='green';
// console.log(sel);


//multi element selector

let s=document.getElementsByClassName('child'); //get elements by class name
s=document.getElementsByTagName('div'); // get elements by tag name
Array.from(s).forEach(function (params) { //change color of div container content
    console.log(params);
    params.style.color='blue';
    
})
// console.log(s);