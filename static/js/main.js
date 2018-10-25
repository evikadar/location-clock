$(function () {
    dataHandler.init();

    $('#new-person').on('submit', function (event) {
        let form = $(this);
        event.preventDefault();
        let data = form.serializeArray();
        $.ajax({
            url: '/save-new-person',
            type: 'POST',
            data: data,
            dataType: "json"
        }).done(function (data) {
            if (data.id) {
                dataHandler.clockData.people.push(data);
                let color = data.color;
                createNewHand(color, 330);
                $('#addPersonModal').modal('hide');
            } else {
                alert('DB error, try again')
            }
        });
    })
});