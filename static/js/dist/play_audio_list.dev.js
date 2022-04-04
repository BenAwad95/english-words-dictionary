"use strict";

var play_eles = document.querySelectorAll('.word-audio');
play_eles.forEach(function (btn) {
  btn.addEventListener('click', function (e) {
    audio_element = e.target;
    audio_source = audio_element.parentElement.previousElementSibling;
    audio_source.play();
  });
});