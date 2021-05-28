async function khushi(){
    console.log('Inside khushi function');
    const response = await fetch('https://api.github.com/users');
    console.log('before response');
    const users = await response.json();
    console.log('users resolved')
    return users;

    // return "khushi";
}

console.log("Before calling khushi")
let a = khushi();
console.log("After calling khushi")
console.log(a);
a.then(data => console.log(data))
console.log("Last line of this js file")

//output flow:--
//myScript.js:12 Before calling khushi
// myScript.js:2 Inside khushi function
// myScript.js:14 After calling khushi
// myScript.js:15 Promise__proto__: Promise[[PromiseState]]: "fulfilled"[[PromiseResult]]: Array(30)
// myScript.js:17 Last line of this js file
// index.html:41 Live reload enabled.
// myScript.js:4 before response
// myScript.js:6 users resolved
// myScript.js:16 Array(30)