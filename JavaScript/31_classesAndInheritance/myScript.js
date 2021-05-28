class Employee{

    constructor(givenName,givenExperience,givenDivision){
        this.name=givenName;
        this.experience=givenExperience;
        this.division=givenDivision;
    }

    slogan(){
        return `This company is best for ${this.name}`;
    }
}

let khushi=new Employee('khushi',20,'c');
let rita=new Employee('rita',30,'d');
console.log(khushi);
console.log(rita.slogan());
console.log(khushi.slogan());