let toFind='khushi';
let vari='myScript.js';
let a=document.links;

for(let i=0;i<a.length;i++)
{

    if(a[i].href.includes(toFind)){
        console.log('Match');
    }else if(a[i].href.includes(vari)){
        console.log('Match '+a[i].href);
    }
    else{
        console.log('not match');
    }
}