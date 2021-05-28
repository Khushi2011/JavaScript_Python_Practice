let persons=[
    {name:"khushi",age:"19"},
    {name:"rita",age:"50"},
    {name:"shalin",age:"23"},
    {name:"manish",age:"53"}
];
// console.log(persons);
function fetchPerson(person,callback){
    setTimeout(function()
    {   
        persons.push(person);
        console.log("in fetchperson function");
        callback();
    },1000);
}
function getPerson(){
    setTimeout(function () {
        let str=``;
        persons.forEach(function(person){
            str+=`<li>${person.name}</li>`;
        })
        document.getElementById("persons").innerHTML = str;

        let name=document.getElementById('name');
        console.log(name.value);
        console.log("in getPerson function");
    },5000);
}

let newPerson={name:"tithi",age:"20"};
fetchPerson(newPerson,getPerson);

