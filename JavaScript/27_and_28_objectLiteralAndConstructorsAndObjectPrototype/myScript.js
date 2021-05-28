person=function(givenName,givenAge,givenGender){
    this.name=givenName;
    this.age=givenAge;
    this.gender=givenGender;
    this.demo=function(){
        console.log(`function called for ${this.name}`);
    }
}

person.prototype.getName=function(){
    return this.name;
}
let obj1=new person('Khushi',19,'Female');
console.log(obj1);
console.log(obj1.age);
console.log(obj1.gender);
console.log(obj1.demo());
console.log(obj1.getName());
//If we write obj1.getName()....then it will return khushi