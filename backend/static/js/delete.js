function delete_card(event){
    card = event.target;
    card_id = card.dataset.card_id;
    deck_id = card.dataset.deck_id;
    deck_name = card.dataset.deck_name;
    console.log(card_id);
    href="/decks/cards/"+ deck_id +"/"+ deck_name +"/delete_card/"+ card_id;
    $('#'+card_id).hide();
    $(document).ready(function(){    
            $.ajax({
                type : 'DELETE',
                url : href
            })
            .done(function(data){
                if(data.error_code){
                    alert("Error occured while deleting card");
                    console.log("Error occured while deleting card");
                }
            });
            event.preventDefault();
    });
}