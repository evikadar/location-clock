// The animate to function should have a parameter that tells it where it should point.
function rotateAround(degree, initialDegree) {
    $('#rotateBtn').click(function () {
        $('#smallHandle').rotate(
            {
                animateTo: degree,
                center: ["50%", "90%"],
                callback: function () {
                    let degreeChange = degree % 360 - initialDegree;
                }
            })
    });
}

function createNewHand(color, degree) {
    let newHand = $('#smallHandle').clone();
    newHand.children().css({fill: color});
    newHand.removeClass('floor1');
    if ($('.floor3').length < 1) {
        newHand.addClass('floor3');
    } else if ($('.floor4').length < 1) {
        newHand.addClass('floor4');
    } else if ($('.floor5').length < 1) {
        newHand.addClass('floor5');
    } else {
        alert("You can't add more than 4 people in this MVP version");
    }
    $('.handCloner').append(newHand);
}

function main() {
    rotateAround(240, 0);
    $('#newHandBtn').click(function () {
        createNewHand('#00da10')
    })
    $('#newHandBtnPurple').click(function () {
        createNewHand('#9400D3')
    })
}

main();
