function check_deck_selected(){
   selected_option = document.getElementById("decklist").selectedIndex
   if (selected_option == 0){
       alert("Please select a deck")
       return false;
   }
}