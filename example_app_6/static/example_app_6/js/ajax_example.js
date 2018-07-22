/**
 *  Handles logging in user with Ajax.
 */


// Wait for full page load.
$(document).ready(function() {
    console.log("Loaded ajax_example.js file.");

    var dom_element = $('.random-number');
    var button_element = $('.rand-button');
    console.log(dom_element);
    console.log(button_element);


    function send_ajax_request() {
        console.log('Sending Ajax request.');

        // Send ajax request.
        $.ajax({
            url: '/ex6/ajax/number',
            dataType: 'json',
            success: function (result) {
                console.log(result);
                dom_element.empty();
                dom_element.append(result['rand_number']);
            },
            error: function (result) {
                console.log(result);
            },
        });
    }


    // Immediately send request on page load.
    send_ajax_request();


    // Button click handling. Send another ajax request for new number.
    button_element.on("click", function(event) {
        send_ajax_request();
    });

});
