
// The animate to function should have a parameter that tells it where it should point.
function rotateAround(degree, initialDegree) {
    $('#rotateBtn').click(function () {
        $('#smallHandle').rotate(
            {
                animateTo: degree,
                center: ["50%", "100%"],
                callback: function () {
                    let degreeChange = degree % 360 - initialDegree;
                }
            })
    });
}

function createNewHand(color, degree) {
    $('#newHandBtn').click(function () {
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
            alert('You cant add more than 4 persons in this MVP version');
        }
        $('.handCloner').append(newHand);
    });
}

function main() {
    rotateAround(20, 0);
    createNewHand('#00da10');
}

main();
