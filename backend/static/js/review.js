function reveal_answer(event){
    var button = event.target;
    var difficulty = document.getElementById('difficulty');
    difficulty.style.display = "inline";
    button.disabled = true;
    console.log(button.id);
}


function difficulty(event){
    var diff = event.target.dataset.difficulty;
    console.log(diff);
}