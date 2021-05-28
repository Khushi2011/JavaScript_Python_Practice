let a = "khushi";
a = undefined;
if (a !=undefined){
    throw new Error('This is not undefined');
}
else{
    console.log('This is undefined');
}


try {
    console.log("We are inside try block");

    let ans=50/0;
    console.log(ans);//any number/0=Infinity

    let ans1=ans/Infinity;//Infinity/Infinity=NAN
    console.log(ans1);
    functionFn();

    
    
} catch(error) {
    console.log(error)
    console.log("Are you okay?");
    console.log(error.name);
    console.log(error.message);
    
} finally {
    console.log("Finally we will run this")
}