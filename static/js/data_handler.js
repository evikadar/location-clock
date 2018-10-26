let dataHandler = {
    clockData: {
        locations: [],
        people: []
    },
    init: function () {
        $.ajax(
            {
                url: '/get-people-data',
                method: 'GET',
                dataType: 'json'
            }
        ).done(function (data) {
            dataHandler.clockData.people.push(data);
        }).fail(function () {
            alert('error')
        });
        $.ajax(
            {
                url: '/get-locations-data',
                method: 'GET',
                dataType: 'json'
            }
        ).done(function (data) {
            dataHandler.clockData.locations.push(data);
        }).fail(function () {
            alert('error')
        });
    }
};