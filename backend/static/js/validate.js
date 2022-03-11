function isInt(value) {
    return !isNaN(value) && 
           parseInt(Number(value)) == value && 
           !isNaN(parseInt(value, 10));
  }

function validate_deckname(){
    var value = document.getElementById('deck_name').value;
    console.log(value)
    if(isInt(value)){
        alert("Deck name cannot be an integer");
        return false;
    }
}