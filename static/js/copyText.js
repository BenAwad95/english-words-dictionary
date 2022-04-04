const $body = document.getElementsByTagName('body')[0];
const copyBtns = document.querySelectorAll('.fa-copy.not-especial')
const copyWordBtn = document.getElementById('copy-word-btn')
// console.log(copyBtns)
// const r = document.getElementById('d')
// r.addEventListener('click')
copyWordBtn.addEventListener('click', (e) =>{
    copyFuncEspecial(e.target)
})
copyBtns.forEach(btn =>{
    btn.addEventListener('click', (e) =>{
        // e.defaultPrevented
        // console.log(1)
        copyFunc(btn)
    })
})

function copyFuncEspecial(btn){
    let copyText = btn.parentElement.innerText
    copyText = (/\w+/i).exec(copyText)[0]
    let $tempInput = document.createElement('INPUT');
    $body.appendChild($tempInput);
    $tempInput.setAttribute('value', copyText)
    $tempInput.select();
    document.execCommand('copy');
    $body.removeChild($tempInput);
}

function copyFunc(btn){
    let copyText = btn.parentElement.innerText
    let $tempInput = document.createElement('INPUT');
    $body.appendChild($tempInput);
    $tempInput.setAttribute('value', copyText)
    $tempInput.select();
    document.execCommand('copy');
    $body.removeChild($tempInput);
}