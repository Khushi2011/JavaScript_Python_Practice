console.log('this is an exercise');
let str='prince';
let a=document.links;
Array.from(a).forEach(function (element) {
    if(element.href.includes(str))
    console.log(element.href);
});
// console.log(a);