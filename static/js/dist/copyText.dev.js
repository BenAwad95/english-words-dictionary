"use strict";

var $body = document.getElementsByTagName('body')[0];
var copyBtns = document.querySelectorAll('.fa-copy.not-especial');
var copyWordBtn = document.getElementById('copy-word-btn'); // console.log(copyBtns)
// const r = document.getElementById('d')
// r.addEventListener('click')

copyWordBtn.addEventListener('click', function (e) {
  copyFuncEspecial(e.target);
});
copyBtns.forEach(function (btn) {
  btn.addEventListener('click', function (e) {
    // e.defaultPrevented
    // console.log(1)
    copyFunc(btn);
  });
});

function copyFuncEspecial(btn) {
  var copyText = btn.parentElement.innerText;
  copyText = /\w+/i.exec(copyText)[0];
  var $tempInput = document.createElement('INPUT');
  $body.appendChild($tempInput);
  $tempInput.setAttribute('value', copyText);
  $tempInput.select();
  document.execCommand('copy');
  $body.removeChild($tempInput);
}

function copyFunc(btn) {
  var copyText = btn.parentElement.innerText;
  var $tempInput = document.createElement('INPUT');
  $body.appendChild($tempInput);
  $tempInput.setAttribute('value', copyText);
  $tempInput.select();
  document.execCommand('copy');
  $body.removeChild($tempInput);
}