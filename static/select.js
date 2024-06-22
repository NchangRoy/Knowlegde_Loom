function selected(){
    output=document.getElementById('select').value
    document.getElementById('subject').setAttribute('placeholder',output)
    document.getElementById('subject').value=output
}
function selected2(){
    output=document.getElementById('select2').value
    document.getElementById('topic').setAttribute('placeholder',output)
    document.getElementById('topic').value=output
}
function selected3(){
    output=document.getElementById('select3').value
    document.getElementById('subtopic').setAttribute('placeholder',output)
    document.getElementById('subtopic').value=output
    
}