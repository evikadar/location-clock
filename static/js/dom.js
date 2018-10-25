$(function () {
    dataHandler.init();

    $('#new-person').on('submit', function (event) {
        let form = $(this);
        event.preventDefault();
        event.stopPropagation();
        let data = form.serializeArray();
        $.ajax({
            url: form.action,
            type: 'POST',
            data: data,
            dataType: "json"
        }).done(function (data) {
            dataHandler.clockData.people.push(data)
        });
    })
});