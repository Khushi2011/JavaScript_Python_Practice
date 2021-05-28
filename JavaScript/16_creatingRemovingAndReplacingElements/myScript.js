//creating element using method 1

let element = document.createElement('li');
let text = document.createTextNode('I am a text node');
element.appendChild(text)
let ul = document.querySelector('ul.this');
ul.appendChild(element);

console.log(element);

// Add a class name to the li element

//by second method 2
let element2= document.createElement('li');
element2.className = 'childul';
element2.id = 'createdLi';
element2.setAttribute('title', 'mytitle');
element2.innerText = 'Hello this is created by khushi';
element2.innerHTML = '<b>Hello this is created by khushi</b>';

let u2 = document.querySelector('ul.this');
u2.appendChild(element2);
// console.log(ul)
 console.log(element2);

//practice
let element3=document.createElement('a');
let text3=document.createTextNode('Hello!!!');
element3.title = "This is Link";
element3.href="https://www.google.com/";
element3.appendChild(text3);
let add3=document.querySelector('.child');
add3.appendChild(element3);
console.log(element3);

let elem2 = document.createElement('h3');
elem2.id = 'elem2';
elem2.className = 'elem2';
let tnode = document.createTextNode('This is a created node for elem2');
elem2.appendChild(tnode);

element.replaceWith(elem2);
let myul = document.getElementById('myul');
myul.replaceChild(element, document.getElementById('fui'));
myul.removeChild(document.getElementById('lui'));
let pr = elem2.hasAttribute('href');
elem2.removeAttribute('id');
elem2.setAttribute('title', 'myelem2title');
console.log(elem2, pr);