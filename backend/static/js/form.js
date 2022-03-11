function add_deck(){
$(document).ready(function(){
    $('form').on('submit',function(event){
        $('#add_deck_error').hide();
        $('#add_deck_success').hide();
        $.ajax({
            data : {
                deck_name : $('#deck_name').val()
            },
            type : 'POST',
            url : "/add_decks"
        })
        .done(function(data){
            if(data.error_code){
                $('#add_deck_error').text('Deck not added :(')
                $('#add_deck_error').append('<br>Response from server: ');
                $('#add_deck_error').append(data.error_message);
                $('#add_deck_error').show();
                $('#add_deck_success').hide()
            }
            else{
                $('#add_deck_error').hide();
                $('#add_deck_success').show()
            }
        });

        event.preventDefault();
    });
});
}

function add_card(){
    $(document).ready(function(){
        $('form').on('submit',function(event){
            $('#add_card_error').hide();
            $('#add_card_success').hide();
            const form = $('form').serializeArray();    
            console.log(form);
                $.ajax({
                    data : {
                        decklist : form[0]["value"],
                        front : form[1]["value"],
                        back : form[2]["value"]
                    },
                    type : 'POST',
                    url : "/add_cards"
                })
                .done(function(data){
                    if(data.error_code){
                        $('#add_card_error').text('Card not added :(')
                        $('#add_card_error').append('<br>Response from server: ');
                        $('#add_card_error').append(data.error_message);
                        $('#add_card_error').show();
                        $('#add_card_success').hide()
                    }
                    else{
                        $('#add_card_error').hide();
                        $('#add_card_success').show()
                    }
                });
                event.preventDefault();
            });
    });
}