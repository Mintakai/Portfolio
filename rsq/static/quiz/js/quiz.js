var jsonLoc = "/static/quiz/data/qdata.json"
var jsonLocUrl = "http://aurorae.tk:8080/static/quiz/data/qdata.json"
var retryCounter = 0

$(function loadJSON() {
    $.getJSON( jsonLoc, function() {}).done( function( data ) {
        var items = [];
        $.each( data, function( key, val ) {
            if (key.includes("Question")) {
                items.push("<p class='question' id='" + key + "'>" + val + "</p>")
            } else {
                items.push("<input type='radio' id='" + key + "' name='" + key.slice(0, -1) + "' value='" + val + "' required>")
                items.push("<label for='" + key + "'>" + val + "</label><br>")
            }
        });

        $( "<div/>", {
            "class": "quiz",
            html: items.join( "" )
        }).prependTo( "form" );
    }).fail( function() {
        retryCounter += 1;
        if(retryCounter < 2) {
            alert("Could not load data, retrying...");
            jsonLoc = jsonLocUrl;
            loadJSON();
        } else {
            alert("Could not load data... try again later!");
        }
    });
});

/*
$(document).ready(function(){
    $("#subbutton").click(function(){        
        var q = $('input[name="Answer 1"]:checked').val();
        var w = $('input[name="Answer 2"]:checked').val();
        var e = $('input[name="Answer 3"]:checked').val();

        alert("Yay!");
    });
});
*/

$(function () {
    $( "form" ).submit(function ( event ) {
        if($(this).valid()) {
            var qVar = "questions"
            var aVar = ""
            var s = 0
            var q = $('input[name="Answer 1"]:checked').val();
            var w = $('input[name="Answer 2"]:checked').val();
            var e = $('input[name="Answer 3"]:checked').val();

            if (q != "Mercury") { s += 0; } else { s += 1 }
            if (w != "3") { s += 0; } else { s += 1 }
            if (e != "Burj Khalifa") { s += 0 } else { s += 1 }

            if (s == 0) { pic = "noob.svg" }
            else if (s == 1) { qVar = qVar.slice(0, -1); pic = "se.png" }
            else if (s == 2) { pic = "mg.png" }
            else { aVar = "all"; pic = "ge.png" }

            $( ".results" ).html("<p class='result_p'>You got " + aVar + " " + s + " " + qVar + " correct!</p>");
            $( "<hr>" ).prependTo( ".results" );
            $("<img class='result_img' src='/static/quiz/images/" + pic + "' alt='rankpic'></img>").appendTo( ".results" )
        }
        event.preventDefault();
    });
});