$(function () {
    $('#login-form').on('submit', function (event) {
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
            if (arguments[0].invalid_data) {
                $('#alert-text').text("Invalid username or password");
                $('#alert').addClass("show");
                setTimeout(() => $('#alert').removeClass("show"), 5000);
            } else {
                window.location.href = '/';
            }
        });
    })
});