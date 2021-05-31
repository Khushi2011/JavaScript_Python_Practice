console.log('This is use for creating,removing & Replacing Elements');
let element=document.createElement('li');
//add class name to created element
element.className='demo';
//add id to created element
element.id='hey';
// element.innerText='just for adding'; //we use html for add text using inner html
//insted of innertext we can use textnode for insert text in created element
let text=document.createTextNode('this is textnode');
element.appendChild(text);
//add setattribute(name,value) to created element
element.setAttribute('set','nothing');
//grap your location where you want to insert a element
let ul=document.querySelector('ul.this');
ul.appendChild(element);
// console.log(ul);
// console.log(element);

//Replace element with elem2
let elem2=document.createElement('h3');
elem2.className='elem2';
elem2.id='elem2';
let tnode=document.createTextNode('This is for replacing');
elem2.appendChild(tnode);
element.replaceWith(elem2);
// console.log(elem2.getAttribute('class'));
let ul1=document.getElementById('myul');
//Replace child(new,old) replace child element
ul1.replaceChild(element,document.getElementById('fli'));
// ul1.removeChild(document.getElementById('lli'));
// Remove child in ul1
// console.log(element.hasAttribute('class'));//to check element contain class attribute  so print true otherwise false
// remove Attribute from an element
// element.removeAttribute('class');

//Exercise
let element3=document.createElement('a');
let text3=document.createTextNode('Go to Google');
element3.appendChild(text3);
element3.href='https://www.google.com';
let add=document.querySelector('.child');
add.appendChild(element3);
// console.log(element3);