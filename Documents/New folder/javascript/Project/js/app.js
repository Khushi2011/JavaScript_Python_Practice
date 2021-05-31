console.log('Welcome notes App');
let addBtn=document.getElementById('addBtn');
addBtn.addEventListener('click',function (e) {
    let addTxt=document.getElementById('addTxt');
    let notes=localStorage.getItem('notes');
    if(notes==0){
        notesObj=[];
    }
    else{
        notesObj=JSON.parse(notes);
    }

});
