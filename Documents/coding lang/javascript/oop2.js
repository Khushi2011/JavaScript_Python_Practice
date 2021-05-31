console.log('This file for object prototype in JavaScript');
let obj={
    firstName:'Prince',
    lastName:'Vanani',
    branch:'CE'
}
console.log(obj);
function Obj(firstName,lastName,branch) {
    this.firstName=firstName;
    this.lastName=lastName;
    this.branch=branch;
}
// 
// console.log(obj1);

//prototype like function
//using object literal we cannot add prototype it will provide default prototype
//using constructor we can add prototy 
//Object is global object we cannot change it's prototype
//we inherit Object prototype
//we can add prototype for particular object not for global obejct(Object)
Obj.prototype.getName= function () {
    return this.firstName;
}
let obj1=new Obj('yash','vaghani','ce');
console.log(obj1.getName());