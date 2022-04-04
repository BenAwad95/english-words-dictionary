const play_eles = document.querySelectorAll('.word-audio')

play_eles.forEach(btn => {
    btn.addEventListener('click', (e) =>{
        audio_element = e.target
        audio_source = audio_element.parentElement.previousElementSibling
        audio_source.play()
    })
})
