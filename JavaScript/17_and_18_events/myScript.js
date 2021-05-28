//creating event click
function change(){
    document.getElementById('heading').style.cursor='pointer';
}

// document.getElementById('heading').addEventListener('click',function(e){
   
//     console.log('You have clicked the heading');
//     //location.href="https://www.google.com/";
//     let abc=e.target;
//     abc=e.target.className;
//     abc=e.target.classList;
//     abc=Array.from(e.target.classList);
//     abc=e.offsetX;
//     console.log(abc);
//     abc=e.offsetY;
//     console.log(abc);
//     abc=e.clientX;
//     console.log(abc);
//     abc=e.clientY;
//     console.log(abc);
    
// });

let btn = document.getElementById('btn');
btn.addEventListener('click', func1);//only for left click
function func1(e) {
    console.log("Single Click", e);
    e.preventDefault();
}

// btn.addEventListener('dblclick', func2);
// function func2(e) {
//     console.log("Thanks its a double click", e);
//     e.preventDefault();
// }

// btn.addEventListener('mousedown', func3);//this will work for both left and right click
// function func3(e) {
//     console.log("Thanks its a mouse down ", e);
//     e.preventDefault();
// }

// document.querySelector('.no').addEventListener('mouseenter', function(){
//     console.log('You entered no')
// })

// document.querySelector('.no').addEventListener('mouseleave', function(){
//     console.log('You exited no')
// })

document.querySelector('.container').addEventListener('mousemove', function(e){
    // console.log(e.offsetX, e.offsetY);
    document.body.style.backgroundColor = `rgb(140,${e.offsetY},${e.offsetX})`;
    // console.log('You triggered mouse move event')
})