const age=35;//== will check the value only while === will check both value and datatype
if(age==18)
{
    console.log('Age is 18');
}
else if(age===35){
    console.log('Age is 35 and datatype is also same');
}
else if(age!=34)
{
    console.log('Age is not 34');
}
else{
    console.log('age is '+ age);
}

//to check if variable defined or not
const vari=67;
if(typeof vari === undefined)
{
    console.log('variable is not defined');
   
}
else{
    console.log('variable is defined');
}

// for boolean value
const vari1=true;
if(vari1){
    console.log(vari1);
}
else{
    console.log(vari1);
}

//ternary operator......(condition)? true:false;
const name='khushi';
console.log(name!='khushi'?'name is khushi':'name is not khushi');

//switch statement 
switch (age) {
    case 18:
        console.log("You are 18");
        break;

    case 28:
        console.log("You are 28");
        break;

    case 35:
        console.log("You are 35");
        break;

    default:
        console.log("You are "+ age);
        break;
}  

switch(name){
    case 'khushi':
        console.log('khushi');
        break;

    default:
        console.log('other');
}