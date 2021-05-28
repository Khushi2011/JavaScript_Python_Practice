/*
element selectors:
1. Single element selector
2. Multi element selector

*/

// 1. Single element selector
let element = document.getElementById("myfirst");
element.style.color = "violet";
console.log(element);
// element = element.className;//return className
// console.log(element);
element = element.childNodes;//return child node
console.log(element);
// element = element.parentNode;//return parent node
// console.log(element);

element.innerText = `khushi doshi`;
element.innerHTML = `<b>khushi doshi</b>`;
console.log(element.innerText);
console.log(element.innerHTML);

let sel = document.querySelector('#myfirst');
sel = document.querySelector('.child');
sel = document.querySelector('div');
sel.style.color = 'red';
console.log(sel);

// 2. Multi element selector
let elems = document.getElementsByClassName('child');
console.log(elems[2]);
elems = document.getElementsByClassName('container');
console.log(elems);
elems = document.getElementsByTagName('div');
console.log(elems);

for (let index = 0; index < elems.length; index++) {
    const element = elems[index];
    console.log(element);
   element.style.color = 'blue'; 
}

// Array.from(elems).forEach(element => {
//     console.log(element);
//    element.style.color = 'blue'; 
// });
console.log(elems[0].getElementsByClassName('child'));