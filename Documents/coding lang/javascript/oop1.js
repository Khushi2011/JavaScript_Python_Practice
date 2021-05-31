console.log('This for object literals,constructor and oop');
//object literals for create an objects
let car={
    name:'Nissan Sunny',
    topSpeed:120,
    run:function () {
        console.log('Car is running');
    }
}
// console.log(car);
//constructor for example new Date() create an objects
//use constructor for  create object

function buildCar(name,topSpeed) {
    this.name=name;
    this.topSpeed=topSpeed;
    this.run=function () {
        console.log(`${this.name}  is running`);
    }
    this.analyze=function () {
        console.log(`${this.name} is less speed ${200-this.topSpeed} than marcedes`);        
    }
    
}
let car1=new buildCar('Nano',70);
// console.log(car1);