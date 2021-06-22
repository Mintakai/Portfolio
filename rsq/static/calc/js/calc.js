function getData() {
    var f = document.getElementById( 'function' ).value;
    var sX = document.getElementById( 'start_x' ).value;
    var eX = document.getElementById( 'end_x' ).value;
    var xS = document.getElementById( 'x_step' ).value;
    var exp = math.compile(f);

    var xVal = math.range(sX, eX, xS).toArray()
    var yVal = xVal.map(function (x) {
        return exp.evaluate({x: x})
    })

    draw(xVal, yVal);
};

var calcChart = undefined;

function draw(xVal, yVal) {
    var ctx = document.getElementById('testChart').getContext('2d');
    
    /* If I don't destroy the old chart here, it'll bug on mouseover */
    if (calcChart != undefined) {
        calcChart.destroy();
    };

    calcChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: xVal,
            datasets: [{
                label: 'f(x)',
                data: yVal,
                fill: false,
                borderColor: "#ac3b61",
                backgroundColor: "#123c69",
                pointBackgroundColor: "#123c69",
                pointBorderColor: "#123c69",
                pointHoverBackgroundColor: "#123c69",
                pointHoverBorderColor: "#123c69",
            }]},
        options: {
            responsive: true,
        }
    });

    write(xVal, yVal);
}

function write(xVal, yVal) {
    var i, valLen, valResult;
    valLen = yVal.length;

    valResult = "<ul>";
    for (i = 0; i < valLen; i++) {
        valResult += "<li class='valResults'>f(" + xVal[i] + ") = " + yVal[i] + "</li>";
    }
    valResult += "</ul>";

    document.getElementById('calc_text').innerHTML = valResult;
}