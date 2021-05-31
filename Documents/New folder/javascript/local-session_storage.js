console.log('this is for local-session Storage');
//local storage is not remove after window close we use clear method for this
//local storage store key,value in Application
//we cannot store array in as value we use jason.stringfy and viseversa json.parse
// localStorage.setItem('Name','Prince'); 
// localStorage.setItem('Name1','Vanani');
// let arr=['MI','RCB','CSK'];
// localStorage.setItem('Ipl',JSON.stringify(arr));
//clear local storage using clear method
// localStorage.clear();
//remove particular key
// localStorage.removeItem('Name');
//get Item from local Storage
//JSON.stringfy use for array into string
//JSON.parse use for string into array
let name=JSON.parse(localStorage.getItem('Ipl'));
console.log(name);
//similer local storage we can use session storage it clear after session over means browser close

// sessionStorage.setItem('Name','Prince'); 
// sessionStorage.setItem('Name1','Vanani');
// sessionStorage.setItem('Ipl',JSON.stringify(arr));
//clear local storage using clear method
// sessionStorage.clear();
//remove particular key
// sessionStorage.removeItem('Name');
//get Item from session storage
//JSON.stringfy use for array into string
//JSON.parse use for string into array