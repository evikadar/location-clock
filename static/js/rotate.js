// Argument color should be added, getting it from the form the user provided.
function changeColor(color) {
    $('#colorRed').on('click', function () {
        $('#path1').css({fill: color})
    });
}

// The animate to function should have a parameter that tells it where it should point.
function rotateAround(degree, initialDegree) {
    $('#rotateBtn').click(function () {
        console.log('Rotate clicked');
        $('#clockhand').rotate(
            {
                animateTo: degree,
                center: ["50%", "100%"],
                callback: function () {
                    let degreeChange = degree % 360 - initialDegree;
                    console.log(degreeChange);
                }
            })
    });
}

function createNewHand(color, degree) {
    $('#newHandBtn').click(function () {
        let newHand = $('.clockHandDiv').clone();
        console.log(newHand);
    });
}

function main() {
    changeColor('#ff43aa');
    rotateAround(20, 0);
    createNewHand();
}

main();
