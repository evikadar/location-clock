$(function () {
    $('#registration-form').on('submit', function (event) {
        let form = $(this);
        event.preventDefault();
        event.stopPropagation();
        let data = form.serializeArray();
        $.ajax({
            url: form.action,
            type: 'POST',
            data: data,
            dataType: "json"
        }).done(function () {
            if (arguments[0].valid_username) {
                $("#success-modal").modal('show');
            } else {
                $('#alert-text').text("This username is already in use. Please choose another one.");
                $('#alert').addClass("show");
                setTimeout(() => $('#alert').removeClass("show"), 5000);
            }
        })
    })
});