const titleInput=document.querySelector('input[name=title]');
const slugInput=document.querySelector('input[name=slug]');
const slugify=(val)=>{
    return val.toString().toLowerCase().trim()
    .replace(/&/g,'-and-') //replaces & with -and-
    .replace(/[\s\W]+/g,'-') //replaces spaces,non-word charcters wuth a single dash
};

titleInput.addEventListener('keyup',(e)=>{
     slugInput.setAttribute('value',slugify(titleInput.value));
});
