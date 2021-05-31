console.log('this is file for exercise purpose');
let replace;
let el=document.getElementById('myul').addEventListener('click',function (e) {
     replace=prompt('please enter  you want to replace word');
    // e.target.innerText=replace;
    // console.log(e.target);
});

document.getElementById('myul').addEventListener('mousedown',function (e) {
   e.target.innerText=replace;
});