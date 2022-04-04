searchEle = document.getElementById("search")

// console.log(searchEle)

searchEle.addEventListener("keyup", (e) => {
  // console.log(e.target.value)
  searchForWords(e.target.value)
})

function searchForWords(searchTo) {
  let allWords = document.querySelectorAll(".word-value")
  // console.log(allWords[10].textContent)
  // if (allWords[0].indexOf())
  allWords.forEach(word => {
    if (word.textContent.toLocaleLowerCase().indexOf(searchTo.toLocaleLowerCase()) != -1) {
      // console.log(word)
      word.parentElement.parentElement.style.display = "flex"
    } else {
      word.parentElement.parentElement.style.display = "None"
    }
    // console.log(word.textContent)
  })
}

// it is working very well
// today 13/10/2020