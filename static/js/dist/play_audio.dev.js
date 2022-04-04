"use strict";

var play_ele = document.getElementById('play_audio');
var audio_source = document.getElementById('audio_src');
play_ele.addEventListener('click', function (e) {
  audio_source.play();
});