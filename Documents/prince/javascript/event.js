console.log('Events & Event Object in JavaScript');
//Event is use for when user interact with webpage click any line or copy we give certain response for that it is called event

let element=document.getElementById('heading').addEventListener('click',function (e) {
    console.log('you clicked on heading');
    let variable=e.target; //it will give tag/element that we click 
    variable=e.target.id;
    // variable=e.offsetX; //it will give position in where you click in x direction
    // variable=e.offsetY;
    variable=e.clientX;//it will give position in where you click in x direction With respect to browser
    // variable=e.clientY
    console.log(variable);
    //addEventlister(eventobj,function);
    // location.href='//google.com'
})
//add event listner use for event listing when that event occur we give certain response
//Event:
//1.click
//2.dblclick
//3.mouseover
//4.mouseup
//5.mousedown rightclick...
//6.mouseenter
//7.mouseleave
// let btn=document.getElementById('btn');
// btn.addEventListener('click',fun1);
// btn.addEventListener('dblclick',fun2);
// btn.addEventListener('mousedown',fun3);
// function fun1(e) {
//     console.log('Thanks for clicking',e);
//     e.preventDefault(); //it use when input type is form is submit it wil show propery in case of submisson 
// }
// function fun2(e) {
//     console.log('Thanks for double clicking',e);
//     e.preventDefault();
// }
// function fun3(e) {
//     console.log('Thanks for mouse down',e);
//     e.preventDefault();
// }

// document.querySelector('.hii').addEventListener
// ('mouseenter',function () {
//     console.log('you moused enterd hii');
// });
// document.querySelector('.hii').addEventListener
// ('mouseleave',function () {
//     console.log('you moused leaved hii');
// });
document.querySelector('.container').addEventListener
('mousemove',function (e) {
    document.body.style.backgroundColor=`rgb(${e.offsetX},${e.offsetY},154)`;
    console.log('you moused leaved hii');
});