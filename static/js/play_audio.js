const play_ele = document.getElementById('play_audio')
const audio_source = document.getElementById('audio_src')

play_ele.addEventListener('click', (e) =>{
    audio_source.play()
})