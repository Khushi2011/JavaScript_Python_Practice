console.log('this is for DOM traversing');
let container=document.querySelector('.container');
console.log(container.nodeName); //name of the node 
console.log(container.nodeType);

//Node type
// 1.Element
// 2.Attribute
// 3.Text Mode
// 8. comment
// 9. document
// 10. docType
container=document.querySelector('div.container');
// console.log(container.childNodes); //it will shows ALL the children include comment,text...
// console.log(container.children); //it will show element in container contain
console.log(container.children[1].children[0].children);
console.log(container.firstChild); //to see into childnodes collection
console.log(container.firstElementChild); //to see into children
console.log(container.lastChild); //to see into childnodes collection
console.log(container.lastElementChild);
// find siblings we can use nextsiblings and nextelementsibiling
console.log(container.firstElementChild.nextElementSibling);