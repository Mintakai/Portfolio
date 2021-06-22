function fuNav() {
    var x = document.getElementById("topnav");
    if (x.className === "topnav") {
        x.className += " responsive";
    } else {
        x.className = "topnav";
    }
}

$(document).ready(function logMod(){
    var mod = document.getElementById('logMod');
    var lnk = document.getElementById('login');

    lnk.onclick = function openModal() {
        /* $('#logMod').load("/login"); */
        mod.style.display = "block";

        $.get( "/login", function( data ) {
            $( ".mod" ).html( data );
            var cls = document.getElementsByClassName('close')[0];
            var fbut = document.getElementById('fbutton');

            fbut.onclick = function postResults() {
                var uname = $("#fusername").val();
                var pw = $("#fpassword").val();
        
                $( ".mod-result" ).html("<hr><p>Your username: " + uname + "</p><p>Your password: " + pw + "</p>");
            };

            cls.onclick = function closeModal() {
                mod.style.display = "none";
            }
            window.onclick = function closeModalFromWindow() {
                if(event.target == mod) {
                    mod.style.display = "none";
                }
            }
        });
    }
});