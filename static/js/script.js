$(document).ready(function() {
    $('#vote_bttn').click(function(event) {
        event.preventDefault();
        var formData = $('#votecontent').serialize();
        $.ajax({
            url: formActionUrl,
            type: "POST",
            data: formData,
            dataType: "html",
            success: function(response) {
                $('.poll-form-container').html(response);
            },
            error: function(xhr, status, error) {
                console.error("AJAX Error:", status, error);
            }
        });
    });
});
